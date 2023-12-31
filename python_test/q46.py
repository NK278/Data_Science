import json

def read_json(file_path,key):
    with open(file_path,'r') as file:
        data=json.load(file)
    val=data[key]
    return val
file_path='dwsample1-json.json'
key="fruit"
print(read_json(file_path, key))            