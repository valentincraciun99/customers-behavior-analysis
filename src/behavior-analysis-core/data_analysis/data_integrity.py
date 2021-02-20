import pandas as pd

from exceptions.exceptions import InvalidParameters


def check_integrity(data: pd.DataFrame):
    """
    check_integrity will raise an exception if
    data is not an instance of pandas DataFrame
    """
    if data is None or not isinstance(data, pd.DataFrame):
        raise InvalidParameters("dataset invalid")
