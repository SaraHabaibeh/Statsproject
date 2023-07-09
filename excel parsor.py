import pandas as pd

dictionary = {'Dem': 0, 'Rep': 1}
df = pd.read_csv("StatsProject.csv")
df.loc[df['Affiliation'] =='Dem', 'Affiliation'] = '0'
df.loc[df['Affiliation'] =='Rep', 'Affiliation'] = '1'
df.to_excel('Updated.xlsx')
