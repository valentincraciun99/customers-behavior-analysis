import io
from concurrent import futures
import logging
from time import sleep

import pandas as pd

import grpc

from data_analysis.transactions import Transactions
from grpcGeneratedCode import main_pb2, main_pb2_grpc
from utils.base64_utils import Decode
from utils.data_validator import validate_columns


class TestClass(main_pb2_grpc.TestService):

    def testMethod(self, request, context):
        print(request.text + " " + str(request.number))
        t = 0
        for i in range(10):
            sleep(2)
            t = t + i
            print(t)
        return main_pb2.TestResponse(number=1, text="test service 1")

    def testMethod2(self, request, context):
        print(request.text + " " + str(request.number))
        return main_pb2.TestResponse(number=2, text="test service 1")


class TestClass2(main_pb2_grpc.TestService2):

    def testMethod(self, request, context):
        print(request.text + " " + str(request.number))
        t = 0
        for i in range(10):
            sleep(2)
            t = t + i
            print(t)
        return main_pb2.TestResponse(number=1, text="test service 2")

    def testMethod2(self, request, context):
        print(request.text + " " + str(request.number))
        return main_pb2.TestResponse(number=2, text="test service 2")


class Data(main_pb2_grpc.DataService):

    def ProcessesData(self, request, context):
        df_initial = pd.read_csv(io.StringIO(request.data.decode('utf-8')),
                                 dtype={'CustomerID': str, 'InvoiceID': str})
        df_initial = df_initial.dropna()
        transaction_processor = Transactions(df_initial)
        transaction_processor.compute_transactions()
        daily_income_points, daily_income_prediction, trend = transaction_processor.compute_linear_regression_points()

        tx = main_pb2.Transactions(dailyIncomePoints=daily_income_points, dailyIncomePrediction=daily_income_prediction,
                                   dailyIncomeTrend=trend,
                                   numberOfTranzactions=transaction_processor.compute_number_of_transactions(),
                                   tranzactionsAvgPrice=transaction_processor.compute_average_price(),
                                   tranzactionsMinPrice=transaction_processor.compute_min_price(),
                                   tranzactionsMaxPrice=transaction_processor.compute_max_price())

        return main_pb2.DatasetResponse(transactions=tx)

    def ProcessDataAsBase64(self, request, context):
        data_as_bytes = Decode(request.data)
        df_initial = pd.read_csv(io.StringIO(data_as_bytes.decode('utf-8')),
                                 dtype={'CustomerID': str, 'InvoiceID': str})

        print(validate_columns(df_initial))
        print(df_initial.head)

        return main_pb2.TestResponse(number=2, text="test service 2")


def serve():
    maxMsgLength = 1024 * 1024 * 1024
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[('grpc.max_message_length', maxMsgLength),
                                                                              ('grpc.max_send_message_length',
                                                                               maxMsgLength),
                                                                              ('grpc.max_receive_message_length',
                                                                               maxMsgLength)])
    main_pb2_grpc.add_TestServiceServicer_to_server(TestClass(), server)
    main_pb2_grpc.add_TestService2Servicer_to_server(TestClass2(), server)
    main_pb2_grpc.add_DataServiceServicer_to_server(Data(), server)
    server.add_insecure_port('[::]:1111')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
