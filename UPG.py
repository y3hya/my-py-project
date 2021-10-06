from tools import tools
from sourcingMonthandPickle import Month
import numpy as np
def openFile():
    df = tools.openPickle(
        r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/detail.p')
        
    return df

if __name__ == "__main__":
    df = openFile()

# df = tools.openExcelFile(
#     r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Raw/202107_SanAntonio_17861233_CommissionDetail_MTZ^EXC^CELL_SHOP_INC^.xlsx')
# import os
# os.environ["MODIN_ENGINE"] = "dask"  # Modin will use Dask
# from distributed import Client
# client = Client()
# import modin.pandas as md
# md = [[df]]

#Replace 4 -- .Cut not working on dataframe -- need to research
# df['Activity Type'] = pd.cut(x=df['Value'], bins=[-9999, 0, 9999],labels=['DEACT', 0, 'ACT']) #-- Try 1
# df['Activity Type'] = df.groupby('Value').apply(lambda x:df.cut(x, [-np.inf, -9999, 9999, np.inf],labels=['DEACT', 0, 'ACT'], duplicates='drop')) #-- Try 2

# Replace 3
# df['Activity Type'] = np.where(df['Value'] > 0, 'ACT', 'DEACT')


#Replace 2
# df['Activity Type'] = df.replace(
#     df['Value'] > 0, 'ACT', 'DEACT', inplace=True)

#Replace 1
def new_func(df):
    a = []
    df = df[df['Value'].notnull()]
    for i in df['Value']:
        if i < 0:
            a += ['DEACT']
        else:
            if i > 0:
                a += ['ACT']

    df['Activity Type'] = a
    return df
if __name__ == "__main__":
    df = new_func(df)
# #########################################################################################
# eliteAct = df[
#     ((df['Transaction Type'] == 'AT&T NEXT ACTIVATION') |
#      (df['Transaction Type'] == 'NO-CONTRACT ACTIVATION') |
#      (df['Transaction Type'] == 'FIRSTNET ACTIVATION')) &
#     (df['Pay Method'] == 'QI_VOICE UNLIMITED ELITE') &
#     (df['Month'] != '')  # Filters
# ]

# x = []
# for i in eliteAct['Value']:
#     if i > 0:
#         x += [145]
#     else:
#         if i < 0:
#             x += [-145]

# eliteAct.drop(columns='Value', axis=1, inplace=True)  # removed Column
# eliteAct['Value'] = (x)  # added Column
# eliteAct['Type'] = 'Elite|Act'  # added Column
# #########################################################################################
# extraAct = df[
#     ((df['Transaction Type'] == 'AT&T NEXT ACTIVATION') |
#      (df['Transaction Type'] == 'NO-CONTRACT ACTIVATION') |
#      (df['Transaction Type'] == 'FIRSTNET ACTIVATION')) &
#     ((df['Pay Method'] == 'QI_FN VOICE PREMIUM') |
#      (df['Pay Method'] == 'QI_MS VOICE PREMIUM')) &
#     (df['Month'] != '')  # Filters
# ]

# x = []
# for i in extraAct['Value']:
#     if i > 0:
#         x += [145]
#     elif i < 0:
#         x += [-145]

# extraAct.drop(columns='Value', axis=1, inplace=True)  # removed Column
# extraAct['Value'] = (x)  # added Column
# extraAct['Type'] = 'Extra|Act'  # added Column
# #########################################################################################
# eliteExtra = eliteAct.append(extraAct)  # appended tables

# # Filtered Column
# eliteExtraAct = eliteExtra[eliteExtra['Activity Type'] == 'ACT']
# eliteExtraAct = eliteExtraAct[['Mobile']]  # remove other column
# eliteExtraAct = eliteExtraAct.drop_duplicates(
#     ['Mobile'], keep='first')  # remove duplicates


# # Filtered Column
# eliteExtraDeact = eliteExtra[eliteExtra['Activity Type'] == 'DEACT']
# eliteExtraDeact = eliteExtraDeact[['Mobile']]  # remove other column
# eliteExtraDeact = eliteExtraDeact.drop_duplicates(
#     ['Mobile'], keep='first')  # remove duplicates
# #########################################################################################
# otherAct = df[(df['Value'] == 145) &
#               (df['Transaction Type'].str.len() > 0 | df['Transaction Type'].notnull())]  # filtered 145 in Value and non blanks & non nulls in Transaction Type
# otherAct['Type'] = 'Other|Act'  # added Column
# otherAct['mob1'] = otherAct['Mobile'].map(dict(
#     zip(eliteExtraAct['Mobile'], eliteExtraAct['Mobile'])))  # Merge Tables
# otherAct = otherAct[(otherAct['mob1'].isnull())]  # Filtered Nulls
# otherAct = otherAct.drop(['mob1'], axis=1)  # Removed Column

# otherDeact = df[(df['Value'] == -145) &
#                 (df['Transaction Type'].str.len() > 0 | df['Transaction Type'].notnull())]  # filtered 145 in Value and non blanks & non nulls in Transaction Type
# otherDeact['Type'] = 'Other|Act'  # added Column
# otherDeact = otherDeact.merge(eliteExtraDeact, on=['Mobile'], how='right')
# #########################################################################################
# finalElite = otherAct.append(
#     [eliteAct, extraAct], ignore_index=True)
# finalElite = finalElite[finalElite['Activity Type'].notnull()]
# #########################################################################################
# eliteAct.info()
# if __name__ == "__main__":
# tools.exportToCsv(df, 'df.csv')
# tools.exportToCsv(otherAct, 'otherAct.csv')
# tools.exportToCsv(otherDeact, 'otherDeact.csv')
# tools.exportToCsv(eliteAct, 'eliteAct.csv')
# tools.exportToCsv(extraAct, 'extraAct.csv')
# tools.exportToCsv(eliteExtraAct, 'eliteExtraAct.csv')
# tools.exportToCsv(eliteExtraDeact, 'eliteExtraDeact.csv')
# tools.exportToCsv(finalElite, 'finalElite.csv')