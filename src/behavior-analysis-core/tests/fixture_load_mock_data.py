import pytest
import pandas as pd


@pytest.fixture(scope="session", autouse=True)
def mock_data():
    df = pd.read_csv('./assets/data_without_cancelation.csv', encoding="ISO-8859-1",
                     dtype={'CustomerID': str, 'InvoiceID': str})
    return df
