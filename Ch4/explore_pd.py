import pandas as pd

df = pd.read_csv('./data/evolution_of_data_analysis.csv',
    header = 0, sep= "|")

dfj = pd.read_json('./data/evolution_of_data_analysis.json')

# print(df.sort_index(1))
print(dfj)
