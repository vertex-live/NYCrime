import pandas as pd
import json, requests

r = requests.get('https://data.ny.gov/resource/nacg-rg66.json?$limit=2000')
json_data = json.loads(r.text)
df = pd.DataFrame(json_data)
mask1 = df['state'] == 'New York'
df_export = df[mask1]
df_export2 = df_export[['tax_year', 'county', 'average_ny_agi_of_all_returns']]
df_export2.set_index('county', inplace = True)
drop_vals = ['Total, New York City',
             'Total, Counties Outside of New York City',
             'NYS Unclassified +',
             'Residence Unknown ++',
             'Grand Total, Full-Year Resident']
df_export2.drop(drop_vals, inplace = True)
df_export2.rename(index = {'St. Lawrence' : 'St Lawrence', 'Manhattan' : 'New York'}, inplace = True)
df_export2.to_csv('NY_AGI.csv', mode = 'w')

