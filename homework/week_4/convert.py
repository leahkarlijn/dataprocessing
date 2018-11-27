import csv
import pandas as pd

input_csv = "chopstick-effectiveness.csv"

df = pd.read_csv(input_csv)
df2 = df[['Food', 'Individual', 'Chopstick']]
outfile = open('data.json','w')
outfile.write(df2.to_json(orient='index'))
outfile.close()
