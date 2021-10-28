import pandas as pd
import glob
import os.path
import sys
from datetime import datetime
import openpyxl
# import os

# os.environ["MODIN_ENGINE"] = "dask"  # Modin will use Dask
# from distributed import Client
# client = Client()
# import modin.pandas as pd


# import dask.dataframe as dd
# ddf = dd.pandas_from(dd)


class tools:

    def getAllFilesFromFolder(folder_path, filename_contains, extension=''):

        # matching
        filename_contains = ('\*' + filename_contains + '*' + extension)
        files_matching = glob.glob(folder_path + filename_contains)

        # ignoring
        filename_contains = '~*'
        files_ignoring = glob.glob(folder_path + filename_contains)

        files = set(files_matching) - set(files_ignoring)

        if len(files) == 0:
            print('\033[91m'
                  + "No such file found"
                  + '\033[0m')
            sys.exit()

        return files

    def getLatestFileFromFolder(folder_path, filename_contains, extension=''):
        files = tools.getAllFilesFromFolder(
            folder_path, filename_contains, extension)

        return max(files, key=os.path.getctime)

    def toDate(date, format='%Y-%m-%d'):
        return datetime.strptime(date, format)

    def exportToCsv(df, file_name='Statement.csv', folder_path=r"C:/Users/TMP-Yahya/Desktop/"):
        df.to_csv(folder_path + file_name, index=False)

    def exportToExcel(df, file_name='Statement.xlsx', folder_path=r"C:/Users/TMP-Yahya/Desktop/"):
        df.to_excel(folder_path + file_name, index=False)

    def dateFormatter(Month, Frmt):
        x = datetime.strftime(datetime.strptime(
            Month + ' 00:00:00', '%m/%d/%Y %H:%M:%S'), Frmt)
        return x

    def openExcelFile(fileLink, sheet_name=0, header=0, skiprows=None):
        df = pd.read_excel(fileLink, sheet_name, header, skiprows=skiprows)
        return df

    def openPickle(path=r"C:/Users/TMP-Yahya/Desktop/Stat.p"):
        d = path
        df = pd.read_pickle(d)
        # df = pd.dask.read_pickle(d)
        return df

    def picklr(df, path):
        df.to_pickle(path)

    def openTableFromFile(folder_path, filename_contains, extension, tableName):
        path = tools.getLatestFileFromFolder(
            folder_path, filename_contains, extension)
        wb = openpyxl.load_workbook(path, data_only=True)

        for ws in wb.worksheets:
            for tbl in ws._tables:
                if tbl == tableName:
                    tableRange = ws.tables[tbl].ref.split(":")
                # print(ws.title)
                    sheet = wb[ws.title]

        table = []
        for row in sheet[tableRange[0]:tableRange[1]]:
            data_cols = []
            for cell in row:
                data_cols.append(cell.internal_value)
            table.append(data_cols)

        return pd.DataFrame(table)
