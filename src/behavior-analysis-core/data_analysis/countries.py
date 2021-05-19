from data_analysis.data_integrity import check_integrity
import pandas as pd


class Countries:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        check_integrity(self.data)

    def count_distinct(self) -> int:
        all_countries = self.data[['CustomerID', 'InvoiceNo', 'Country']].groupby(
            ['CustomerID', 'InvoiceNo', 'Country']).count()
        all_countries = all_countries.reset_index(drop=False)
        countries = all_countries['Country'].value_counts()
        return len(countries)
