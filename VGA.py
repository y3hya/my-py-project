import pandas as pd
from tools import tools
from Statement import Month

pd = tools.openPickle(r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/detail.p')
# pd = tools.openPickle() # -- To pcik pickle from desktop
eliteAct = pd[
    ((pd['Transaction Type'] == 'AT&T NEXT ACTIVATION') |
     (pd['Transaction Type'] == 'NO-CONTRACT ACTIVATION') |
     (pd['Transaction Type'] == 'FIRSTNET ACTIVATION')) &
    (pd['Pay Method'] == 'QI_VOICE UNLIMITED ELITE') &
    (pd['Month'] != '')
]

# C:\Dropbox\OpSupport Team Folder\Cell Shop\Commission\AT&T Reports\2021-07\Formatted  --

x = []
for i in eliteAct['Value']:
    if i > 0:
        x += [145]
    else:
        if i < 0:
            x += [-145]
eliteAct.drop(columns='Value', axis=1, inplace=True)
eliteAct['Value'] = (x)
eliteAct['Type'] = 'Elite|Act'  # added Column

extraAct = pd[
    ((pd['Transaction Type'] == 'AT&T NEXT ACTIVATION') |
     (pd['Transaction Type'] == 'NO-CONTRACT ACTIVATION') |
     (pd['Transaction Type'] == 'FIRSTNET ACTIVATION')) &
    ((pd['Pay Method'] == 'QI_FN VOICE PREMIUM') |
     (pd['Pay Method'] == 'QI_MS VOICE PREMIUM')) &
    (pd['Month'] != '')
]

x = []
for i in extraAct['Value']:
    if i > 0:
        x += [145]
    else:
        if i < 0:
            x += [-145] 
extraAct.drop(columns='Value', axis=1, inplace=True)  # removed Column
extraAct['Value'] = (x)  # added Column
extraAct['Type'] = 'Extra|Act'  # added Column

# append eliteAct & extraAct here

otherAct = pd[(pd['Value'] == 145) &
              (pd['Transaction Type'].str.len() > 0 | pd['Transaction Type'].notnull())]  # filtered 145 in Value and non blanks & non nulls in Transaction Type
otherAct['Type'] = 'Other|Act'  # added Column

eliteExtraAct = eliteAct.append(extraAct)
eliteExtraAct = eliteExtraAct.drop_duplicates(['Mobile'])
eliteExtraAct = eliteExtraAct[['Mobile']]


otherAct = otherAct.merge(eliteExtraAct, left_on='Mobile', right_on='Mobile') #--To Merge at the end

finalElite = otherAct.append([eliteAct, extraAct], ignore_index=True)

# eliteAct.info()
# tools.exportToCsv(otherAct, 'otherAct.csv')
# tools.exportToCsv(eliteAct, 'eliteAct.csv')
# tools.exportToCsv(extraAct, 'extraAct.csv')
# tools.exportToCsv(eliteExtraAct, 'eliteExtraAct.csv')
tools.exportToCsv(finalElite, 'finalElite.csv')
