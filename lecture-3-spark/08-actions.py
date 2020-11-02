import pyspark
sc = pyspark.SparkContext('local[*]')

big_list = range(100000)
rdd = sc.parallelize(big_list, 2)

# By using the RDD filter() method, that operation occurs in a distributed manner across several CPUs or computers.
odds = rdd.filter(lambda x: x % 2 != 0)
res = odds.take(5)
print(res)
