import json
import sys

print(sys.argv[1])
exit

f = open("es-" + sys.argv[1], "w")
f.write("")
with open("es-" + sys.argv[1], 'a') as json_file:
    with open(sys.argv[1]) as data_file:          
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
