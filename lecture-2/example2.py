import datetime
import requests
import json

def insertwithin(a, v, s):
    if s>10:
        return
    for p in range(s,10):
        if len(a) <= p:
            a.append(v)
            return
        if len(a) > p and a[p]['population'] < v['population']:
            temp = a[p]
            a[p] = v
            insertwithin(a, temp, p+1)
            return
        
res = requests.get('https://restcountries.eu/rest/v2/all', verify=False)
data = res.content

begin_time = datetime.datetime.now()

countries = json.loads(res.content)
result = []

for i in countries: 
    insertwithin(result, i, 0)

end_time = datetime.datetime.now()

print("Most populous countries in the world: ")
for c in result:
    print(c['name'] + ": " + str(c['population']))
    
print((end_time - begin_time))    

