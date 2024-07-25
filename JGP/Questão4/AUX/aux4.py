import os 
import pandas as pd
import re

## auxiliary code so we can merge some of the output DATA from question1 and make a bigger CSV

ls =os.listdir()
ls_csv = []

for file in ls:
    if re.search(".*.csv", file):
        ls_csv.append(file)

ls_csv.sort()

df = pd.concat(map(pd.read_csv, ls_csv),ignore_index= True)
df.to_csv('DATA.csv')

print(ls_csv)
