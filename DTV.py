from tools import tools
from sourcingMonthandPickle import Month
import numpy as np
import pandas as pd


df = tools.openPickle(
    r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/detail.p')

# Filtered nulls in Comments column
df = df[df['Comments'].isnull()]
# Added Activity Type column
df['Activity Type'] = pd.cut(
    df.Value, bins=[-np.inf, 0, np.inf], labels=['DEACT', 'ACT'])  # -- Try 1


df = df[
    (df['Transaction Type'] == 'OTT') |
    (df['Transaction Type'] == 'WIRED ACTIVATION') &
    (df['Month'] != '')
]

df = df[
    (df['Pay Method'] == 'ATT TV_COMP') |
    (df['Pay Method'] == 'DTV_COMP')
]

DTV = df

DTV['Type'] = 'Direct|TV'  # added Column

# DTV.info()
# hints to replace any number of spaces with single space
DTV['Customer Name'] = DTV['Customer Name'].str.replace(r'\W+', ' ')

# ________________________________________________________________________

tools.exportToCsv(DTV, 'DTV.csv')
