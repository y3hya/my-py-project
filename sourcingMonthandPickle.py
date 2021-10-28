from tools import tools
import pandas as pd


Month = tools.dateFormatter('09/01/2021', '%Y-%m')


file = tools.getLatestFileFromFolder(
    'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/', 'wired', '.xlsx')
df = tools.openExcelFile(file, 'Table1')
df = pd.read_csv('my_csv_file.csv', skiprows=1)
tools.picklr(
    df, r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/wired.p')
