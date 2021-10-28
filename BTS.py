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
    df.Value,
    bins=[-np.inf, 0, np.inf],
    labels=['DEACT', 'ACT']
)  # -- Try 1

btsAct = df.copy()
btsAct = btsAct[
    (btsAct['Transaction Type'] == 'CONNECTED DEVICE') |
    (btsAct['Transaction Type'] == 'FIRSTNET AT&T DEVICE') |
    (btsAct['Transaction Type'] == 'TABLET ACTIVATION') |
    (btsAct['Transaction Type'] == 'WEARABLE ACTIVATION') |
    (btsAct['Transaction Type'].isnull()) |
    (btsAct['Transaction Type'] == 'NO-CONTRACT ACTIVATION') |
    (btsAct['Transaction Type'] == 'FIRSTNET OTHER DEVICE') |
    (btsAct['Transaction Type'] == 'FIRSTNET ACTIVATION')
]

btsAct = btsAct[(btsAct['Contract Name'] == 'DIGITAL_INCENTIVE') |
                (btsAct['Contract Name'] == 'WIRELESS_ACTS_UPGDS')
                ]

btsAct = btsAct[btsAct['Adj Desc2'].isnull() |
                (btsAct['Adj Desc2'] == 'WEARABLE')
                ]
btsAct = btsAct[(btsAct['Pay Method'] == 'ACTIVATIONS_DATA DEVICES_BYOD') |
                (btsAct['Pay Method'] == 'ACTIVATIONS_TABLETS_WEARABLES')
                ]
btsAct = btsAct[(btsAct['Month'] != '')
                ]

btsAct['Type'] = 'Data|Act'  # added Column
# ________________________________________________________________________________________
btsUpg = df.copy()

btsUpg = btsUpg[(btsUpg['Contract Name'] == 'WIRELESS_ACTS_UPGDS') &
                (btsUpg['Transaction Type'] == 'TABLET UPGRADE') |
                (btsUpg['Transaction Type'] == 'WEARABLE UPGRADE') |
                (btsUpg['Transaction Type'] == 'FIRSTNET AT&T DEVICE') &
                (btsUpg['Pay Method'] == 'UPGRADES_TABLETS_WEARABLES')
                ]
btsUpg['Type'] = 'Data|Upg'

BTS = btsAct.append(btsUpg)

tools.exportToCsv(BTS, 'BTS.csv')
