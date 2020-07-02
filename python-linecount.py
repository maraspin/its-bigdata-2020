import pyspark
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////srv/apps/its-bigdata-2020/example.txt')

print("Il file contiene " +  str(txt.count()) + " righe")
python_lines = txt.filter(lambda line: 'its' in line.lower())
print("Le righe che contengono la stringa ITS sono: " + str(python_lines.count()))

