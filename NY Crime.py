
import pandas as pd
import requests, json, datetime

r = requests.get('https://data.ny.gov/resource/ca8h-8gjq.json?$limit=20000')
json_data = json.loads(r.text)
df = pd.DataFrame(json_data)
df.columns
df.sort_values(['year', 'county'], inplace = True)
mask1 = df['county'] != 'Region Total'
mask2 = df['agency'] == 'County Total'
df_export = df[mask1 & mask2]
df_export.reset_index(inplace = True)
del df_export['index']
df_export.fillna(value = 0, inplace = True)
df_export['property'] = df_export['property'].astype(int)
df_export['violent'] = df_export['violent'].astype(int)
df_export['total_index_crimes'] = df_export['total_index_crimes'].astype(int)
df_pivot = df_export.pivot_table(index = ['year', 'county'], aggfunc = 'sum')

df_pivot.to_csv('NY_Crime.csv', mode = 'w')

