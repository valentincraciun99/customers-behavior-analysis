import pytest
import pandas as pd
from data_analysis.countries import Countries
from data_analysis.data_integrity import check_integrity
from exceptions.exceptions import InvalidParameters
from tests.fixture_load_mock_data import mock_data


class TestCountries:
    def test_countries_invalid_constructor_params(self):
        with pytest.raises(InvalidParameters):
            Countries(None)

    def test_count(self, mock_data: pd.DataFrame):
        countries = Countries(mock_data)
        assert countries.count_distinct() == 37
