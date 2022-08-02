from pyexcel_odsr import get_data  # pyexcel_odsr is really heavy on pc might be better to dump it

'''
leaving this to idea stage, gotta figure out getting data from ODS format.

      sheet  line column
        |      |  |
data["Andmed"][0][1]
'''


def get_date_yesterday():
    with open ("müük Rocca.ods", "r", encoding="idna")as sale_r:
        data = sale_r.read()
        print(data)

    data = get_data("müük Rocca.ods", row_limit=100, start_column=1, column_limit=11, sheet_name="Andmed")

    # print(data["Andmed"][30][5])  # first line of sales numbers

   # if data["Andmed"][52][5] == "":
        # print(data["Andmed"][30][1])
    #    date = data["Andmed"][52][1].strftime("%d.%m.%Y")
     #   print(date)
      #  return date
   # else:
    #    print("no")
    # return yesterday


get_date_yesterday()