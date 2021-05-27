import pytest

from data_analysis.transactions import Transactions
from exceptions.exceptions import InvalidParameters
from tests.fixture_load_mock_data import mock_data
import pandas as pd
from numpy import array


class TestTransactions:

    def test_countries_invalid_constructor_params(self):
        with pytest.raises(InvalidParameters):
            Transactions(None)

    def test_compute_transactions(self, mock_data: pd.DataFrame):
        transactions = Transactions(mock_data)
        transactions.compute_transactions()

        assert transactions.transactions.first_valid_index() > 0

    def test_compute_linear_regression_points(self, mock_data: pd.DataFrame):
        transactions = Transactions(mock_data)
        transactions.compute_transactions()
        sol1, sol2, sol3 = transactions.compute_linear_regression_points()

        assert not sol1 == ""
        assert not sol2 == ""
        assert sol3 == "ascending"

    def test_compute_number_of_transactions(self, mock_data: pd.DataFrame):
        transactions = Transactions(mock_data)
        transactions.compute_transactions()
        assert transactions.compute_number_of_transactions() == 18432

    def test_compute_average_price(self, mock_data: pd.DataFrame):
        transactions = Transactions(mock_data)
        transactions.compute_transactions()
        assert transactions.compute_average_price() == 458.6925045572916

    def test_compute_min_price(self, mock_data: pd.DataFrame):
        transactions = Transactions(mock_data)
        transactions.compute_transactions()
        assert transactions.compute_min_price() == 0.38

    def test_compute_max_price(self, mock_data: pd.DataFrame):
        transactions = Transactions(mock_data)
        transactions.compute_transactions()
        assert transactions.compute_max_price() == 30757
