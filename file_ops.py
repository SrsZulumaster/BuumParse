from pyexcel_odsr import get_data

'''
      sheet  line column
        |      |  |
data["Andmed"][0][1]
'''


def get_date_yesterday():
    data = get_data("müük Rocca.ods", start_row=30, row_limit=100, start_column=1, column_limit=11, sheet_name="Andmed")

    print(data["Andmed"][10][5])

    if data["Andmed"][23][5] == "":
        print("yeet")
    else:
        print("no")
    # return yesterday


get_date_yesterday()
