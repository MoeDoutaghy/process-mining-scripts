import csv
import pandas as pd


df = pd.DataFrame(pd.read_csv("Sepsis Cases - Event Log.csv"))
res = df.pivot_table(index=['case'], columns='event',
                     values='startTime', aggfunc='first').reset_index()
print(res)
res.to_csv('sepsisTransormed.csv', index = False)

