import pyspark
import json
from pyspark.sql import SparkSession

sc = pyspark.SparkContext('local[*]')
spark = SparkSession.builder.getOrCreate()

data = spark.read.json('../samples/sales.json', multiLine=True)

counts = data.rdd.map(lambda row: (str(row["year"]) + "-" + str(row["month"]),row["value"])) \
             .reduceByKey(lambda a, b: a +b)

counts.saveAsTextFile("file:////srv/apps/its-bigdata-2020/balance-results")
