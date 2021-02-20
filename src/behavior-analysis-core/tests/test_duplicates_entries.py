import pytest

from data_analysis.duplicates_entries import DuplicatesEntries
import pandas as pd

from exceptions.exceptions import InvalidParameters
from tests.fixture_load_mock_data import mock_data


class TestDuplicatesEntries:

    def test_duplicates_entries_invalid_constructor_params(self):
        with pytest.raises(InvalidParameters):
            DuplicatesEntries(None)

    def test_count(self, mock_data: pd.DataFrame):
        duplicates_entries = DuplicatesEntries(mock_data)
        expected = mock_data.duplicated().sum()
        actual = duplicates_entries.count()
        assert actual == expected

    def test_remove_duplicates(self, mock_data):
        duplicates_entries = DuplicatesEntries(mock_data)
        duplicates_before_deletion = mock_data.duplicated().sum()
        assert duplicates_before_deletion > 0

        duplicates_entries.remove_duplicates()
        duplicates_after_deletion = mock_data.duplicated().sum()
        assert duplicates_after_deletion == 0
