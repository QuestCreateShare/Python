import json

number = '21'

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
