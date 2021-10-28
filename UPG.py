from tools import tools
from sourcingMonthandPickle import Month
import numpy as np
import pandas as pd

df = tools.openPickle(
    r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/detail.p')


df = df[
    ((df['Transaction Type'] == 'AT&T NEXT UPGRADE') |
     (df['Transaction Type'] == 'FIRSTNET UPGRADE') |
     df['Transaction Type'].isnull()) &
    ((df['Contract Name'] == 'DIGITAL_INCENTIVE') |
     (df['Contract Name'] == 'WIRELESS_ACTS_UPGDS')) &
    (df['Month'] != '')
]

# Filtered nulls in Comments column
df = df[df['Comments'].isnull()]
# Added Activity Type column
df['Activity Type'] = pd.cut(
    df.Value, bins=[-np.inf, 0, np.inf], labels=['DEACT', 'ACT'])  # -- Try 1
# ________________________________________________________________________________________
eliteUpg = df[((df['Pay Method'] == 'QI_VOICE UNLIMITED ELITE UPG') |
               (df['Pay Method'] == 'VOICE_PREM_FN_UPG'))  # Filters
              ]
eliteUpg['Type'] = 'Elite|Upg'  # added Column
# ________________________________________________________________________________________
extraUpg = df[((df['Pay Method'] == 'QI_WRL FN VOICE PREM UPG') |
               (df['Pay Method'] == 'QI_WRLS VOICE PREM UPG'))  # Filters
              ]
extraUpg['Type'] = 'Extra|Upg'  # added Column
# ________________________________________________________________________________________
# appended tables

# Filtered Column
eliteFilter = eliteUpg[['Mobile']]  # remove other column
eliteFilter = eliteFilter.drop_duplicates(
    ['Mobile'], keep='first')  # remove duplicates


# Filtered Column
extraFilter = extraUpg[['Mobile']]  # remove other column
extraFilter = extraFilter.drop_duplicates(
    ['Mobile'], keep='first')  # remove duplicates

eliteExtra = eliteFilter.append(extraFilter)
# ________________________________________________________________________________________
otherUpg = df[((df['Value'] == -85) | (df['Value'] == 85) | (df['Value'] == -100))
              ]  # filtered columns
otherUpg['Type'] = 'Other|Upg'  # added Colu-mn
otherUpg['mob1'] = otherUpg['Mobile'].map(dict(
    zip(eliteExtra['Mobile'], eliteExtra['Mobile'])))  # Merge Tables
otherUpg = otherUpg[(otherUpg['mob1'].isnull())]  # Filtered Nulls
otherUpg = otherUpg.drop(['mob1'], axis=1)  # Removed Column

# ________________________________________________________________________________________
UPGs = otherUpg.append(
    [eliteUpg, extraUpg], ignore_index=True)
UPGs = UPGs[UPGs['Activity Type'].notnull()]
# ________________________________________________________________________________________

tools.exportToCsv(UPGs, 'UPGs.csv')
