import pandas as pd
from tools import tools


# xyz = ''.join([x for x in folderPath if re.search('Stat', x)])
Month = tools.dateFormatter('07/01/2021', '%Y-%m')
file = tools.getLatestFileFromFolder(
    r'C:/Dropbox/OpSupport Team Folder/Cell Shop/Commission/AT&T Reports/' + Month + '/Formatted/', 'stat', '.xlsx')
