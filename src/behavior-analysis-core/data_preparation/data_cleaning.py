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
