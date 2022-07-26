from pyexcel_odsr import get_data


def get_date_yesterday():
    data = get_data("müük Rocca.ods", start_row=30, row_limit=2, start_column=1, column_limit=11, sheet_name="Andmed")
    print(data["Andmed"][0][5])
    # return yesterday


get_date_yesterday()
