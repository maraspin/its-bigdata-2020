import pyspark
sc = pyspark.SparkContext('local[*]')

l=["spark is super fast","hive is sql on hadoop","hadoop is slow", "spark is awesome"]
rdd=sc.parallelize(l)
r1 = rdd.collect()
print(r1)
rddm=rdd.map(lambda line:line.split())
r2 = rddm.collect()
print(r2)
rddf=rdd.flatMap(lambda line:line.split())
r3 = rddf.collect()
print(r3)
