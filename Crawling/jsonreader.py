import json
import pandas as pd
data = pd.read_csv('deposit.csv')
data.to_json('depositJson.json', orient = 'records')

with open('depositJson.json', 'r', encoding="UTF-8") as f:
    json_data = json.load(f)

data = json.dumps(json_data, ensure_ascii = False)
print(data)
