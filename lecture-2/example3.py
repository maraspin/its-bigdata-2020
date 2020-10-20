import datetime
import requests
import json
import redis

redis = redis.Redis(host='localhost', port=6379, db=0)        
res = requests.get('https://restcountries.eu/rest/v2/all', verify=False)
data = res.content

begin_time = datetime.datetime.now()

countries = json.loads(res.content)
result = []

for c in countries: 
    dict = {}
    dict[c['name']] = c['population']
    redis.zadd("result", dict)

end_time = datetime.datetime.now()

print("Most populous countries in the world: ")
result = redis.zrevrange("result", 0, 10, withscores=True)
for c in result:
    print(c)
    
print((end_time - begin_time))    

