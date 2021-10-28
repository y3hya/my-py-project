import pandas as pd
from tools import tools
import openpyxl

df = tools.openTableFromFile(
    r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + tools.dateFormatter('8/1/2021', '%Y-%m') + '/Formatted/', 'stat', '.xlsx', 'For_ServiceCom')
df = df.iloc[0:, :]
tools.exportToExcel(df, 'Table2.xlsx')
