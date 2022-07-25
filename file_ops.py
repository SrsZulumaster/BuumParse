import pandas as pd


def get_date_yesterday():

    df = pd.read_excel("müük Rocca.ods", engine="odf",sheet_name="Andmed", usecols= "A:L")

    print(df)
    #return yesterday


get_date_yesterday()