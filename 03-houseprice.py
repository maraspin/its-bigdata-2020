# An example based upon the famous Boston Housting Dataset
# https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html

from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
spark = SparkSession.builder.getOrCreate()

# Data is imported in tabular "fashion"
data = spark.read.csv('samples/BostonHousing.csv', 
                       header=True, inferSchema=True)
# data.show()

# We omit the final column, MEDV, the Median value of owner-occupied homes (our LABEL)
# The FEATURES of our dataset are therefore all but the last one:
feature_columns = data.columns[:-1] 
# feature_columns.show()

from pyspark.ml.feature import VectorAssembler

# https://spark.apache.org/docs/latest/ml-features#vectorassembler
# we create a unique column named "features" where data from all feature_columns is imported

# assembler definition
assembler = VectorAssembler(inputCols=feature_columns,
                            outputCol="features")

# assembler is applied to data, and data_2 is created
data_2 = assembler.transform(data)
#data_2.show()


# Two datasets are created. One for the TRAIN and one for the TEST phase
train, test = data_2.randomSplit([0.7, 0.3])

# training dataset
#train.show()

# testing dataset
# test.show()

# Linear regression algorithm is declared
# "medv" identifies our pregression field, while "features" is feature data
algo = LinearRegression(featuresCol="features", 
                       labelCol="medv")

# model is filled with train data
model = algo.fit(train)

# test is performed with test data
evaluation_summary = model.evaluate(test)

# Evaluation parameters are extracted
#evaluation_summary.meanAbsoluteError
# Output: 3.39
#evaluation_summary.rootMeanSquaredError
# Output: 5.16
#evaluation_summary.r2
# Output: 0.58


# This is what we would do on real, new data. We only have this dataset here.
# But this is actually where the real Machine Learning Takes place. 
# Use this to apply it to newly generated data
predictions = model.transform(test)
# predictions.show()

# we are only interested in relevant columns 
# predictions.select(predictions.columns[13:]).show() 
