from concurrent import futures
import logging

import grpc

import main_pb2
import main_pb2_grpc


class TestClass(main_pb2_grpc.TestService):

    def testMethod(self, request, context):
        print(request.text + " " + str(request.number))
        return main_pb2.TestResponse(number=1, text="test service 1")

    def testMethod2(self, request, context):
        print(request.text + " " + str(request.number))
        return main_pb2.TestResponse(number=2, text="test service 1")


class TestClass2(main_pb2_grpc.TestService2):

    def testMethod(self, request, context):
        print(request.text + " " + str(request.number))
        return main_pb2.TestResponse(number=1, text="test service 2")

    def testMethod2(self, request, context):
        print(request.text + " " + str(request.number))
        return main_pb2.TestResponse(number=2, text="test service 2")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_TestServiceServicer_to_server(TestClass(), server)
    main_pb2_grpc.add_TestService2Servicer_to_server(TestClass2(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
