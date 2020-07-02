import pyspark
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////srv/apps/its-bigdata-2020/example.txt')

counts = txt.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a +b)

# print("Il file contiene " +  txt.count() + " righe")
# python_lines = txt.filter(lambda line: 'its' in line.lower())
#print("Le righe che contengono la stringa ITS sono: " + python_lines.count())

counts.saveAsTextFile("file:////srv/apps/its-bigdata-2020/result-folder")
