from data_analysis.data_integrity import check_integrity
import pandas as pd

from data_preparation import data_cleaning


class Transactions:
    def __init__(self, data: pd.DataFrame):
        self.data = data
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

        transactions = transactions[transactions['Price'] > 0]

        return transactions
