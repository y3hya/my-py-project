import pandas as pd
from pandas.core.frame import DataFrame


# def openExcelFile():
#     d = r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/2021-07/Raw/202107_SanAntonio_17861233_CommissionDetail_MTZ^EXC^CELL_SHOP_INC^.xlsx'
#     df = pd.read_excel(d, sheet_name='TRANSACTIONS')
#     return df

class newbieWars:


    def openPickle(file=r"C:/Users/TMP-Yahya/Desktop/Stat.p"):
        d = file
        df = pd.read_pickle(d)
        return df


def filterNotNullColumn(df: DataFrame, columnName):
    df = df[df[columnName].notnull()]
    return df


def filterNan(df: DataFrame, columnName):
    df = df[df[columnName].notna()]
    return df


def exportToExcel(df, file_name='Statement.xlsx'):
    df.to_excel(r"C:/Users/TMP-Yahya/Desktop/" + file_name, index=False)


def exportToCsv(df, file_name='Statement.csv', folder_path=r"C:/Users/TMP-Yahya/Desktop/"):
    df.to_csv(folder_path + file_name, index=False)


def filterColumnByAbsNumber(df, columnName, number):
    df = df[(df[columnName].abs() == number)]
    return df


def exportToPickle(df):
    file_name = 'Stat.p'
    df.to_pickle(r"C:/Users/TMP-Yahya/Desktop/" + file_name)


print("Running...")

# df = openExcelFile()
df = openPickle()

df = filterNotNullColumn(df, 'Month')
print(df.tail())

df = df[
    (df['Adj Desc2'] != 'INV HANDLING FEE') &
    (df['Adj Desc2'] != 'INVENTORY SHRINK') &
    (df['Adj Desc2'] != 'TREASURY VARIANCE')
]

df = df.transpose()
df = filterNotNullColumn(df, 0)
df = df.transpose()

exportToCsv(df)
# exportToExcel(df)
# exportToPickle(df)

print("Done")
