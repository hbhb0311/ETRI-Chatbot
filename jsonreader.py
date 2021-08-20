import json

with open('./korquad2.1_train_00.json', 'r', encoding="UTF-8") as f:
    json_data = json.load(f)

data = json.dumps(json_data, ensure_ascii = False)
print(data)
