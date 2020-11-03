import pyspark
import json
from pyspark.sql import SparkSession

sc = pyspark.SparkContext('local[*]')
spark = SparkSession.builder.getOrCreate()

data = spark.read.json('../samples/sales.json', multiLine=True)

def mapF (row):
    return (
            ( str(row["year"]) + "-" + str(row["month"]) ), 
            (row["value"], 1) 
           )

counts = data.rdd.map(mapF) \
             .reduceByKey(lambda a, b: ((a[0] +b[0]),(a[1] + b[1])))
# print(counts.collect())

res = counts.map(lambda a: (a[0],(a[1][0] / a[1][1]))) 
print(res.collect())

# res.saveAsTextFile("file:////srv/apps/its-bigdata-2020/lecture-3-spark/solutions/ave")
