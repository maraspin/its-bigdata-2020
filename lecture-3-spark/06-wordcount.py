import pyspark

# Creates context - local implies localhost is used, * is to enable parallelism on all available cores
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////srv/apps/its-bigdata-2020/samples/simple.txt')

counts = txt.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a +b)

counts.saveAsTextFile("file:////srv/apps/its-bigdata-2020/wc-results")
