# from https://cognitus.fr/mllib-p1-regression/

from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
spark = SparkSession.builder.getOrCreate()

data = spark.read.csv('samples/BostonHousing.csv', header=True, inferSchema=True)
# data.show()

feature_columns = data.columns[:-1] # here we omit the final column
from pyspark.ml.feature import VectorAssembler
assembler = VectorAssembler(inputCols=feature_columns,outputCol="features")

data_2 = assembler.transform(data)
#data_2.show()

train, test = data_2.randomSplit([0.7, 0.3])
algo = LinearRegression(featuresCol="features", labelCol="medv")
model = algo.fit(train)

evaluation_summary = model.evaluate(test)
evaluation_summary.meanAbsoluteError
# Output: 3.39
evaluation_summary.rootMeanSquaredError
# Output: 5.16
evaluation_summary.r2
# Output: 0.58

predictions = model.transform(test)
predictions.select(predictions.columns[13:]).show() # filtering columns just to fit
