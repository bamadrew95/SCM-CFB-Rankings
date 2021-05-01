import pandas as pd
from openpyxl import load_workbook


def excel(year, folder, ws_name, df):
    filename = (
        "C:/Users/bamadrew95/Documents/Rankings/SCM Development/FBS-Stats-Scraper-master/data/"
        + folder
        + "/"
        + year
        + folder
        + ".xlsx"
    )
    book = load_workbook(filename)
    writer = pd.ExcelWriter(filename, engine="openpyxl")
    writer.book = book

    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, ws_name, index=False)
    writer.save()