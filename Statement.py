# test 2 commit

import pandas as pd
from datetime import datetime
import os

def dateFormatter(Month, Frmt):
    x = datetime.strftime(datetime.strptime(Month + ' 00:00:00', '%m/%d/%Y %H:%M:%S'), Frmt)
    return x

Month = dateFormatter('07/01/2021', '%Y-%m')
#myPath=os.listdir(r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + datetime.Month(_, '%Y-%m') + '/Formatted') 

# these are my git learning changes
