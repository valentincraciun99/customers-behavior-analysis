import base64
import datetime
from pprint import pprint
from sklearn.linear_model import LinearRegression
from data_analysis.data_integrity import check_integrity
import pandas as pd
import matplotlib.pyplot as plt  # To visualize

from data_preparation import data_cleaning
from numpy import array

from utils.base64_utils import Array_To_Base64_String


def determine_trend(coefficient):
    if coefficient > 0:
        trend = "ascending"
    else:
        trend = "descending"
    return trend


class Transactions:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.transactions = []
        check_integrity(self.data)
        # TODO:This should be at data preparation section
        # data_cleaning.add_field_quantity_canceled_to_data(self.data)
        self.data['InvoiceDate'] = pd.to_datetime(self.data['InvoiceDate'])

    def compute_transactions(self) -> pd.DataFrame:
        self.data['TotalPrice'] = self.data['UnitPrice'] * (self.data['Quantity'] - self.data['QuantityCanceled'])

        temp = self.data.groupby(by=['CustomerID', 'InvoiceNo'], as_index=False)['TotalPrice'].sum()
        transactions = temp.rename(columns={'TotalPrice': 'Price'})

        self.data['InvoiceDate_int'] = self.data['InvoiceDate'].astype('int64')
        temp = self.data.groupby(by=['CustomerID', 'InvoiceNo'], as_index=False)['InvoiceDate_int'].mean()
        self.data.drop('InvoiceDate_int', axis=1, inplace=True)
        transactions.loc[:, 'InvoiceDate'] = pd.to_datetime(temp['InvoiceDate_int'])

        self.transactions = transactions[transactions['Price'] > 0]

    def compute_linear_regression_points(self):
        amounts = self._calculate_daily_amount_collected()
        indexes = [*range(len(amounts))]

        X = array(indexes).reshape((-1, 1))
        Y = array(amounts)

        linear_regressor = LinearRegression()
        linear_regressor.fit(X, Y)
        y_prediction = linear_regressor.predict(X)  # make predictions# perform linear regression

        trend = determine_trend(linear_regressor.coef_)

        return Array_To_Base64_String(amounts), Array_To_Base64_String(y_prediction), trend

    def compute_number_of_transactions(self):
        statistics = self.transactions.describe()
        return int(statistics['Price'][0])

    def compute_average_price(self):
        statistics = self.transactions.describe()
        return statistics['Price'][1]

    def compute_min_price(self):
        statistics = self.transactions.describe()
        return statistics['Price'][3]

    def compute_max_price(self):
        statistics = self.transactions.describe()
        return statistics['Price'][7]

    def _calculate_daily_amount_collected(self):
        self.transactions['InvoiceDate'] = self.transactions['InvoiceDate'].dt.date
        date = self.transactions['InvoiceDate'].min()
        end_date = self.transactions['InvoiceDate'].max()
        delta = datetime.timedelta(days=1)
        amounts = []
        while date <= end_date:
            day_transactions = (self.transactions[self.transactions['InvoiceDate'] == date])
            amounts.append(day_transactions['Price'].sum())
            date += delta
        return amounts
