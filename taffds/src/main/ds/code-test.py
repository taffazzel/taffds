from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession().builder.getOrCteate()
input_file_location='/home/jovyan/work/green_tripdata_2021-01.csv'
df = spark.read.csv(input_file_location,inferSchema=True,header=True)
df.printSchema()
df.count()
df.select('payment_type').distinct()
from pyspark.sql.window import Window
from pyspark.sql.functions import *
windowSpec = Window.partitionBy(col('VendorID')).orderBy(col('trip_distance').desc())
''' avegare of the whole column using agg '''
df.select('total_amount').show()
df.filter(col('total_amount')>10.00).agg(avg(col('trip_distance')))
df.agg(avg(col("total_amount"))).show()
df.agg(sum(col("total_amount"))).show()
df.groupBy('VendorID').agg(avg(col("total_amount"))).show()

''' using window function. with orderBy analytical functions work but not rank '''
df = df.withColumn("avg_price", avg("price").over(windowSpec))
df.withColumn('test4', avg(col("total_amount")).over(windowSpec)).show()
df.withColumn('rank', rank().over(windowSpec)).select('VendorID','rank').show()
df.withColumn("rank", rank().over(windowSpec)).show()


data=[('Taffazzel','CS',645),('Hossain','CS',644),('Abdul','ECE',641),('Gaffar','ECE',641),('Alex','CS',641),('Abdul','ECE',641),('Abdul','ECE',641),\
      ('Tom','CV',641),('Cruise','EE',641),('Abdul','ECE',641),('Abdul','CV',641),('Abdul','CV',65)]
df = spark.createDataFrame(data=data,schema=['Name','subject','roll'])
df.printSchema()
df.groupBy('subject','Name').agg(sum(col('roll'))).show()
df.groupBy('subject','Name').agg(max(col('roll'))).show()
df.groupBy('subject','Name').agg(min(col('roll'))).show()
df.agg(max(col('roll'))).show()

windowSpec=Window.partitionBy(col('subject'))
from pyspark.sql.functions import rank


df.withColumn('test1',avg('roll').over(windowSpec)).show()
df.withColumn('test2',max('roll').over(windowSpec)).show()
windowSpec=Window.partitionBy('subject').orderBy('Roll',desc('Roll'))
df = df.coalesce(1).withColumn('increasing_id',monotonically_increasing_id())
df.withColumn('row_number',row_number().over(windowSpec)).\
    withColumn('Rank',rank().over(windowSpec)).withColumn('dense_rank',dense_rank().over(windowSpec)).show()

'''

pandas


import pandas as pd
file = '/Users/taffazzelhossain/Downloads/test1.csv'
df = pd.read_csv(file)
print("The dataframe is ..")
print(df.head())
print("Hello..")
print(list(df.columns))
print("World..")
print(df['Marks'])
print("Log1")
print(df.shape)
print(df)
df2 = df.drop_duplicates()
print(df2.shape)

import numpy as np
data=pd.DataFrame({'Name:':['Taffazzel','','ABC','DEF'],
                   'Marks':[65,36,0,7],
                   'Roll':[7,np.nan,2,6]})


data.fillna('Taff')
df.replace(to_replace=np.nan,value=-88)
print(df.iloc[0:2])
print(df.loc[2])


df['Roll'].isin([0,2,8])
df[df['Roll'].to_string(index=False)]
'''
def lambda_test(x):
    print("CC")
    return x*2

'''lambda_test()'''

'''lambda_test=lambda x:print('Hello',x)'''
lambda_test = list(map(lambda x:x*3,range(0,10)))

print(lambda_test)

lambda_test2=filter(lambda x:x>5,list(map(lambda x:x*2,range(0,10))))
print(list(lambda_test2))

[i*2 for i in range(0,10) if i>5]

df.write.parquet('/home/jovyan/work/result.csv')

df.write.parquet('/home/jovyan/work/resul1')
df.write.option("sep", "\t").option("nullValue", "n/a").parquet('/home/jovyan/work/resul1')
df.write.format("csv").option("sep","\t").mode("overwrite").save("/home/jovyan/work/resul1")
df.write.mode("overwrite").parquet()


'''join types'''
# Prapare data
import pyspark
from pyspark.sql import SparkSession

emp = [(1,"Smith",-1,"2018","10","M",3000), \
    (2,"Rose",1,"2010","20","M",4000), \
    (3,"Williams",1,"2010","10","M",1000), \
    (4,"Jones",2,"2005","10","F",2000), \
    (5,"Brown",2,"2010","40","",-1), \
      (6,"Brown",2,"2010","50","",-1) \
  ]
empColumns = ["emp_id","name","superior_emp_id","year_joined", \
       "emp_dept_id","gender","salary"]

empDF = spark.createDataFrame(data=emp, schema = empColumns)
empDF.printSchema()
empDF.show(truncate=False)

dept = [("Finance",10), \
    ("Marketing",20), \
    ("Sales",30), \
    ("IT",40),\
    ("IT",70),\
    ("IT",40)\
  ]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)

'''Inner join'''
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"inner") \
     .show(truncate=False)
empDF.join(broadcast(deptDF),empDF.emp_dept_id==deptDF.dept_id).show(truncate=False)
empDF.join(broadcast(deptDF),empDF.emp_dept_id==deptDF.dept_id,"left").show(truncate=False)
empDF.join(broadcast(deptDF),empDF.emp_dept_id==deptDF.dept_id,"right").show(truncate=False)
empDF.withColumn('emp_dept_id',col('emp_dept_id').cast('string'))

'''RDD'''
rdd = sc.textFile('/home/jovyan/work/test-text.txt')
rdd.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortByKey(lambda x:x[1]).collect()
rdd.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortByKey(lambda x:x[1]).collect()
rdd.map(lambda x:x.split(' ')).map(lambda x:(x,1))


rdd.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).groupByKey(lambda x,y:x+y).sortByKey(lambda x:x[1]).collect()

sp_list=[1, 2, 3, 4, 5]
input_rdd = sc.parallelize(sp_list)
output_rdd = input_rdd.map(lambda x: x * 2)
input_rdd.flatMap(lambda x:[i for i in sp_list if i > 2]).collect()

words_rdd = text_rdd.flatMap(tokenize)
rdd.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)


