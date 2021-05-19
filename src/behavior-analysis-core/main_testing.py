from pprint import pprint
from time import sleep

import pandas as pd

from data_analysis.duplicates_entries import DuplicatesEntries
from data_preparation.data_cleaning import  calculate_null_values, get_cancellation_transactions

if __name__ == '__main__':
    # __________________
    # read the datafile
    df_initial = pd.read_csv('/home/cvg/Downloads/archive/data.csv', encoding="ISO-8859-1",
                             dtype={'CustomerID': str, 'InvoiceID': str})
    #print('Dataframe dimensions:', df_initial.shape)

    #print(df_initial[df_initial["InvoiceNo"].str.find('C') >= 0])
    #print(df_initial[df_initial["InvoiceNo"] == "C536379"])
    # pprint(df_initial["c" in df_initial["InvoiceNo"]])
    # Data Cleaning

    print("")
    duplicates_enries = DuplicatesEntries(df_initial)
    print("{} duplicates_enries entries".format(duplicates_enries.count()))

    duplicates_enries.remove_duplicates()

    print("{} duplicates_enries entries after deleting".format(duplicates_enries.count()))

    null_values_df = calculate_null_values(df_initial)



    #print(null_values_df)

    #print(get_cancellation_transactions(df_initial).head)

