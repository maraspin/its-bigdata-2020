import json

f = open("es-account-data.json", "w")
f.write("")
with open('es-account-data.json', 'a') as json_file:
    with open('source-data.json') as data_file:          
        data = json.load(data_file)
        for person in data:
            indexdict = {
               "index": { "_id": person["index"]} 
            }
            json.dump(indexdict, json_file)
            json_file.write("\r\n")
            json.dump(person, json_file)
            json_file.write("\r\n")
            print(person)
