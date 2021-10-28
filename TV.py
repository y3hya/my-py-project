from tools import tools
from sourcingMonthandPickle import Month
import numpy as np
import pandas as pd

df = tools.openPickle(
    r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/wired.p')

# Filtered nulls in Comments column
df = df[df['Comments'].isnull()]
# Added Activity Type column
df['Activity Type'] = pd.cut(
    df.Value, bins=[-np.inf, 0, np.inf], labels=['DEACT', 'ACT'])  # -- Try 1
df = df[
    (df['Transaction Type'] == 'AT&T NEXT ACTIVATION') |
    (df['Transaction Type'] == 'NO-CONTRACT ACTIVATION') |
    (df['Transaction Type'] == 'FIRSTNET ACTIVATION') &
    (df['Month'] != '')
]
# ________________________________________________________________________________________
eliteAct = df[(df['Pay Method'] == 'QI_VOICE UNLIMITED ELITE')  # Filters
              ]

eliteAct['Value'] = pd.cut(
    eliteAct.Value, bins=[-np.inf, -0.00001, 0.00001, np.inf], labels=[-145, 0, 145])
eliteDeact = eliteAct[(eliteAct['Activity Type'] == 'DEACT')].drop_duplicates(
    ['Mobile'], keep='first')  # -- make copy of deacts and remove duplicates
eliteAct = eliteAct[(eliteAct['Activity Type'] == 'ACT')]
eliteAct = eliteAct.append([eliteDeact], ignore_index=True)
eliteAct['Type'] = 'Elite|Act'  # added Column
# ________________________________________________________________________________________
extraAct = df[((df['Pay Method'] == 'QI_FN VOICE PREMIUM') |
               (df['Pay Method'] == 'QI_MS VOICE PREMIUM'))  # Filters
              ]

extraAct['Value'] = pd.cut(
    extraAct.Value, bins=[-np.inf, -0.00001, 0.00001, np.inf], labels=[-145, 0, 145])
extraDeact = extraAct[(extraAct['Activity Type'] == 'DEACT')].drop_duplicates(
    ['Mobile'], keep='first')  # -- make copy of deacts and remove duplicates
extraAct = extraAct[(extraAct['Activity Type'] == 'ACT')]
extraAct = extraAct.append([extraDeact], ignore_index=True)
extraAct['Type'] = 'Extra|Act'  # added Column
# ________________________________________________________________________________________
eliteExtra = eliteAct.append(extraAct)  # appended tables

# Filtered Column
eliteExtraAct = eliteExtra[eliteExtra['Activity Type'] == 'ACT']
eliteExtraAct = eliteExtraAct[['Mobile']]  # remove other column
eliteExtraAct = eliteExtraAct.drop_duplicates(
    ['Mobile'], keep='first')  # remove duplicates


# Filtered Column
eliteExtraDeact = eliteExtra[eliteExtra['Activity Type'] == 'DEACT']
eliteExtraDeact = eliteExtraDeact[['Mobile']]  # remove other column
eliteExtraDeact = eliteExtraDeact.drop_duplicates(
    ['Mobile'], keep='first')  # remove duplicates
# ________________________________________________________________________________________
otherAct = df[(df['Value'] == 145) &
              (df['Transaction Type'].str.len() > 0 | df['Transaction Type'].notnull())]  # filtered 145 in Value and non blanks & non nulls in Transaction Type
otherAct['Type'] = 'Other|Act'  # added Column
otherAct['mob1'] = otherAct['Mobile'].map(dict(
    zip(eliteExtraAct['Mobile'], eliteExtraAct['Mobile'])))  # Merge Tables
otherAct = otherAct[(otherAct['mob1'].isnull())]  # Filtered Nulls
otherAct = otherAct.drop(['mob1'], axis=1)  # Removed Column

otherDeact = df[(df['Value'] == -145) &
                (df['Transaction Type'].str.len() > 0 | df['Transaction Type'].notnull())]  # filtered 145 in Value and non blanks & non nulls in Transaction Type
otherDeact['Type'] = 'Other|Act'  # added Column
otherDeact = otherDeact.merge(eliteExtraDeact, on=['Mobile'], how='right')
# ________________________________________________________________________________________
VGAs = otherAct.append(
    [eliteAct, extraAct], ignore_index=True)
VGAs = VGAs[VGAs['Activity Type'].notnull()]
# ________________________________________________________________________________________

tools.exportToCsv(VGAs, 'VGAs.csv')
