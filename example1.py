import datetime
import requests
import redis

# redis = redis.Redis(host='34.243.5.189', port=16379, db=0)

begin_time = datetime.datetime.now()

res = requests.get('https://www.mocky.io/v2/5ed60dcf3400007b0006d626?mocky-delay=1000ms', verify=False)
data = res.content
end_time = datetime.datetime.now()

print(data)
print((end_time - begin_time))
