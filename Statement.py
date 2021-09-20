import pandas as pd
from datetime import datetime
import os

def dateFormatter(Month, Frmt):
    x = datetime.strftime(datetime.strptime(Month + ' 00:00:00', '%m/%d/%Y %H:%M:%S'), Frmt)
    return x

Month = dateFormatter('07/01/2021', '%Y-%m')
folderPath = os.listdir(r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/'+ Month + '/Formatted')
filePicked = folderPath [folderPath.index('Stat')]
print(filePicked)