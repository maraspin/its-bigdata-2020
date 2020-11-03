import pyspark

es_conf = {
    "es.nodes" : 'localhost', # master node
    "es.port" : '9200',
    "es.resource" : 'bank/_doc',
    "es.input.json" : "yes",
}

es_wconf = es_conf
es_wconf.es.resource = 'state/_doc'

# Creates context - local implies localhost is used, * is to enable parallelism on all available cores
sc = pyspark.SparkContext('local[*]')

# Reading stuff from Elasticsearch
dd = sc.newAPIHadoopRDD("org.elasticsearch.hadoop.mr.EsInputFormat",
                             "org.apache.hadoop.io.NullWritable",
                             "org.elasticsearch.hadoop.mr.LinkedMapWritable",
                            conf=es_conf)

# useful for debugging
#print(dd.first())

# Map function
def estrai(record):
    return (record[1]["state"], { "balance" : record[1]["balance"], "people": 1, "average" : record[1]["balance"] } )
    
# Reduce function
def unisci(a, b):
    return { "balance": (a["balance"] + b["balance"]), 
             "people": (a["people"] + b["people"]), 
             "average": ((a["balance"] + b["balance"]) / (a["people"] + b["people"])) 
           }

cleanCol = dd.map(estrai).reduceByKey(unisci).sortByKey()

results = cleanCol.map(lambda item: ('key', { 
    'state': item[0], 
    'accounts': item[1]["people"],
    'total': item[1]["balance"],
    'average': item[1]["average"]
}))

print(results.collect())

results.saveAsNewAPIHadoopFile(
path='-',
outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
keyClass="org.apache.hadoop.io.NullWritable",
valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
conf=es_wconf
)

# instead of, as before...
#cleanCol.saveAsTextFile("./accountresult")
