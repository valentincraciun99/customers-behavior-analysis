import pytest
from data_analysis.data_integrity import check_integrity
from exceptions.exceptions import InvalidParameters
from tests.fixture_load_mock_data import mock_data


class TestDataIntegrity:

    def test_data_integrity_null_data(self):
        with pytest.raises(InvalidParameters):
            check_integrity(None)

    def test_data_integrity_invalid_data(self):
        with pytest.raises(InvalidParameters):
            check_integrity([2, 2, 3])

    def test_data_integrity_valid_data(self, mock_data):
        check_integrity(mock_data)
