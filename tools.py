import glob
import os.path
import sys
from datetime import datetime
import pandas as pd


class tools:

    def getAllFilesFromFolder(folder_path, filename_contains, extension=''):

        filename_contains = '\*'+filename_contains+'*'+extension

        files = glob.glob(folder_path+filename_contains)

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

    def exportToCsv(df, file_name, folder_path):
        df.to_csv(folder_path + file_name, index=False)

    def dateFormatter(Month, Frmt):
        x = datetime.strftime(datetime.strptime(
            Month + ' 00:00:00', '%m/%d/%Y %H:%M:%S'), Frmt)
        return x

    def openExcelFile(fileLink):
        df = pd.read_excel(fileLink)
        return df
