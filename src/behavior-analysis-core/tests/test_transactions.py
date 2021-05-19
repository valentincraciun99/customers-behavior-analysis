import pytest

from data_analysis.transactions import Transactions
from exceptions.exceptions import InvalidParameters
from tests.fixture_load_mock_data import mock_data
import pandas as pd


class TestTransactions:

    def test_countries_invalid_constructor_params(self):
        with pytest.raises(InvalidParameters):
            Transactions(None)

    def test_compute_transactions(self, mock_data: pd.DataFrame):
        transactions = Transactions(mock_data)
        sol = transactions.compute_transactions()
        assert sol.first_valid_index() > 0


