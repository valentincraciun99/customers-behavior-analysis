import pandas as pd

from data_analysis.data_integrity import check_integrity


class DuplicatesEntries:
    def __init__(self, data: pd.DataFrame):
        """
        Create a new instance of DuplicatesEntries and raise
        exception if data is not an instance of pandas Dataframe
        """
        self.data = data
        check_integrity(self.data)

    def count(self) -> int:
        """
        Count duplicates values of pandas
        Dataframe provided by constructor

        :return:
        number duplicates rows in df
        """
        return self.data.duplicated().sum()

    def remove_duplicates(self):
        """
        Remove duplicates values of pandas
        Dataframe provided by constructor

        :return:
        it modify df provided by constructor
        """
        self.data.drop_duplicates(inplace=True)

