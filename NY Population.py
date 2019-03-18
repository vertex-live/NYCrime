import pandas as pd
import json, csv, datetime, requests

r = requests.get('https://data.ny.gov/resource/34dd-6g2j.json?$limit=1800')
json_data = json.loads(r.text)
df = pd.DataFrame(json_data)
df.columns
df_export = df[['year', 'county', 'population', 'firearm_count']]
df_export.to_csv('NY_Population.csv', index = False, mode = 'w')
