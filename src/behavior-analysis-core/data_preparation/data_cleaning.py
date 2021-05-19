import pandas as pd


def calculate_null_values(data: pd.DataFrame) -> pd.DataFrame:
    null_values_df = pd.DataFrame(data.dtypes).T.rename(index={0: 'column type'})
    null_values_df = null_values_df.append(
        pd.DataFrame(data.isnull().sum()).T.rename(index={0: 'null values (number)'}))
    null_values_df = null_values_df.append(pd.DataFrame(data.isnull().sum() / data.shape[0] * 100).T.
                                           rename(index={0: 'null values (%)'}))

    return null_values_df


def get_cancellation_transactions(data: pd.DataFrame) -> pd.DataFrame:
    cancellation_transactions = data[data["UnitPrice"] < 0]
    return cancellation_transactions


def add_field_quantity_canceled_to_data(data):
    data['QuantityCanceled'] = 0

    entry_to_remove = []
    doubtfull_entry = []

    for index, column in data.iterrows():
        if (column['Quantity'] > 0) or column['Description'] == 'Discount': continue
        possible_counterpart_data = data[(data['CustomerID'] == column['CustomerID']) &
                                         (data['StockCode'] == column['StockCode']) &
                                         (data['InvoiceDate'] < column['InvoiceDate']) &
                                         (data['Quantity'] > 0)].copy()

        # _________________________________
        # Cancelation WITHOUT counterpart
        if possible_counterpart_data.shape[0] == 0:
            doubtfull_entry.append(index)
        # ________________________________
        # Cancelation WITH a counterpart
        elif possible_counterpart_data.shape[0] == 1:
            index_order = possible_counterpart_data.index[0]
            data.loc[index_order, 'QuantityCanceled'] = -column['Quantity']
            entry_to_remove.append(index)
            # ______________________________________________________________
        # Various counterparts exist in orders: we delete the last one
        elif possible_counterpart_data.shape[0] > 1:
            possible_counterpart_data.sort_index(axis=0, ascending=False, inplace=True)
            for ind, val in possible_counterpart_data.iterrows():
                if val['Quantity'] < -column['Quantity']: continue
                data.loc[ind, 'QuantityCanceled'] = -column['Quantity']
                entry_to_remove.append(index)
                break

    data.drop(entry_to_remove, axis=0, inplace=True)
    data.drop(doubtfull_entry, axis=0, inplace=True)
