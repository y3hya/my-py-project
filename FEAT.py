from tools import tools
from sourcingMonthandPickle import Month
import numpy as np

df = tools.openPickle(
    r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/detail.p')

df['Contract Name'] = df['Contract Name'].str.upper()

df = df[df['Contract Name'].str.contains('FEATURE') == True]

# Filtering Column based on multiple Conditions with Numpy
conditions = ((df['Value'].abs() == 50), (df['Value'].abs() == 15))
results = ['FEAT|For4', 'FEAT|For1']
df['Type'] = np.select(conditions, results, default=None)
df = df[df['Type'].notnull()]

tools.exportToCsv(df, 'FEAT.csv')
