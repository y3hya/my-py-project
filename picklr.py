# CLI PICKER
from tools import tools
import pandas as pd
import sys

print(sys.argv)

if(len(sys.argv)) != 2:
    print("YOU HAVE NOT PROVIDED FILE PATH")
    quit()

file_link = sys.argv[1]
print(file_link)


def exportToPickle(df):
    file_name = 'Stat.p'
    df.to_pickle(r"C:/Users/TMP-Yahya/Desktop/" + file_name)


df = tools.openExcelFile(file_link)
exportToPickle(df)

# write in terminal = picklr filePath
