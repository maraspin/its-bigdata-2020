import datetime
import requests
import redis

redis = redis.Redis(host='localhost', port=6379, db=0)

begin_time = datetime.datetime.now()
data = redis.get('italy')
end_time = datetime.datetime.now()

if (data == None):
    res = requests.get('https://www.mocky.io/v2/5ed60dcf3400007b0006d626?mocky-delay=1000ms', verify=False)
    data = res.content
    redis.set('italy', data)
    end_time = datetime.datetime.now()

print(data)
print((end_time - begin_time))
