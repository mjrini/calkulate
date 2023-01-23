
import pandas as pd

#data = pd.read_csv("T40356_20221215_1607_100_Tsum.csv")

import csv

filename = "T40356_20221215_1607_100_Tsum.csv"

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        print(row)



import pandas as pd

filename = 'T40356_20221215_1607_100_Tsum.csv'
df = pd.read_csv(filename)

for index, row in df.iterrows():
    print(row)
