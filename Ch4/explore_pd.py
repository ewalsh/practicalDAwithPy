import pandas as pd

df = pd.read_csv('./data/evolution_of_data_analysis.csv',
    header = 0, sep= "|")

print(df.sort_index(1))
