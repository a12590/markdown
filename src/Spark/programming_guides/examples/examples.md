## 一. Spark Example
这篇文章会快速的介绍Spark的API, Spark是基于分布式的数据集, 可以包含任意的Java或Python项目. 用户可以从外部的数据生成数据集, 同时可以进行并行的操作.Spark内建的API就是RDD API. RDD API有2种操作: transformations 定义一个新的RDD基于前面的RDD; actions 在集群上开行执行job. Spark RDD提供了高级的API, DataFrame API 和 Machine Learning API. 这些API提供简单的方式进行数据操作, 在这篇文章中我们会使用这些高级的API进行演示.

## 二. RDD API Example
### 1. Word Count
这个例子中, 使用transformations去操作string pair计算word counts并存储到文件
```
text_file = sc.textFile("hdfs://...")
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://...")

a. sc.textFile用来读取hdfs文件返回RDD
b. flatMap把一个RDD数据映射为多个, map把一个单词映射为(word,1) pair, reduceByKey把相同的key进行累加
c. saveAsTextFile把RDD持久化存储到hdfs文件

代码: ./code/Spark_0_code.py
提交: spark-submit  --master yarn --num-executors 1 --executor-cores 2 --executor-memory 500M Spark_0_code.py
      默认用client方式执行这样才能在当前机器看到print信息
      spark-submit  --master yarn --deploy-mode cluster --num-executors 1 --executor-cores 2 --executor-memory 500M Spark_0_code.py
      这种方式执行的话driver print的信息不会打在当前机器的console
```

### 2. Pi Estimation
Spark还可以执行计算密集型任务, 采取"掷非镖"的方式画出单位圆, 随机选取点(x,y)观测有多少点落于圆内, 落于圆内的概率为 pi/4, 因此可以通过这个来预测pi值
```
def sample(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)

a. parallelize用于把python的collection序列化为Spark的RDD, map根据随机点的位置返回1或0, reduce把所有的值相加

代码: ./code/Spark_1_code.py
提交: spark-submit  --master yarn --num-executors 1 --executor-cores 1 --executor-memory 500M Spark_1_code.py
      默认用client方式执行这样才能在当前机器看到print信息
```

## 三. DataFrame API Example
Spark的DataFrame对象是一个以列组织的分布式数据对象, 用户可以使用DataFrame API在外部数据源和Spark内置的分布式数据集上执行各种关系型操作. 同时程序基于Spark的DataFrame API将会由Spark内置的优化器进行优化

### 1. Text Search
这个例子我们在log文件里面搜索错误信息
```
textFile = sc.textFile("hdfs://...")

# Creates a DataFrame having a single column named "line"
df = textFile.map(lambda r: Row(r)).toDF(["line"])
errors = df.filter(col("line").like("%ERROR%"))

# Counts all the errors
errors.count()

# Counts errors mentioning MySQL
errors.filter(col("line").like("%MySQL%")).count()

# Fetches the MySQL errors as an array of strings
errors.filter(col("line").like("%MySQL%")).collect()

a. textFile从hdfs读取log文件
b. map把每一行映射为Row对象, 同时利用toDF函数转化成DataFrame对象
c. 通过col("line")找到line这一列再调用like函数找到error信息
d. count函数计算rdd对象record个数

代码: ./code/Spark_2_code.py
      例子和Spark_2_code有差异 Spark2.0之后rdd没有toDF函数
提交: spark-submit  --master yarn --num-executors 1 --executor-cores 1 --executor-memory 500M Spark_2_code.py
      默认用client方式执行这样才能在当前机器看到print信息
```

### 2. Simple Data Operations
在这个例子中, 从数据库的表中读取数据并计算每个人的平均年龄. 最后把数据按照json格式存储在S3. 一个简单的Mysql表"people"有2列"name"和"age"
```
# Creates a DataFrame based on a table named "people"
# stored in a MySQL database.
url = "jdbc:mysql://yourIP:yourPort/test?user=yourUsername;password=yourPassword"
df = sqlContext.read.format("jdbc").option("url", url).option("dbtable", "people").load()

# Looks the schema of this DataFrame.
df.printSchema()

# Counts people by age
countsByAge = df.groupBy("age").count()
countsByAge.show()

# Saves countsByAge to S3 in the JSON format.
countsByAge.write.format("json").save("s3a://...")
```

## 四. Machine Learning Example
Spark机器学习库MLlib提供了很多分布式的机器学习算法. 这些算法覆盖了 特征抽取, 分类, 回归, 聚类, 推荐等等. MLlib同时也提供了机器学习pipeline工具用于构建工作流程, 模型训练和参数调优, 同时也支持模型加载和模型离线存储.

### 1. Prediction with Logistic Regression
在这例子里, 使用"标签"和"特征"数据集, 使用逻辑回归算法去预测标签值.
```
# Every record of this DataFrame contains the label and
# features represented by a vector.
df = sqlContext.createDataFrame(data, ["label", "features"])

# Set parameters for the algorithm.
# Here, we limit the number of iterations to 10.
lr = LogisticRegression(maxIter=10)

# Fit the model to the data.
model = lr.fit(df)

# Given a dataset, predict each point's label, and show the results.
model.transform(df).show()
```
