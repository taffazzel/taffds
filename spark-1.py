from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder.master("local[*]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()
df = spark.read.csv("dbfs:/FileStore/tables/test.csv",inferSchema=True,header=True).printSchema()
