import pandas as pd
from tools import tools

Month = tools.dateFormatter('07/01/2021', '%Y-%m')
file = tools.getLatestFileFromFolder(
    'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/', 'detail', '.xlsx')

pd = tools.openExcelFile(file)
pd = tools.picklr(pd, r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/', 'detail.p')
# pd = tools.picklr(pd) # -- To create pickle copy on desktop 