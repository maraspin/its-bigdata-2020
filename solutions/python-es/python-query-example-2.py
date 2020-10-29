from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'bigdata.its', 'port': 9200}])

if es.ping():
        print('Connected!')
else:
        print('Damn!')

# res = es.get(index="bank", id=14)
res = es.search(index="bank", body={"query": { "match": {"state": "AZ"}}, "size": 3})
print(res)



