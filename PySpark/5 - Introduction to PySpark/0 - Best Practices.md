## Getting to know PySpark

cluster computing: A cluster is a group of inter-connected computers or hosts that work together to support applications and middleware (e.g. databases). In a cluster, each computer is referred to as a “node”.

Splitting up your data makes it easier to work with very large datasets because each node (separate computer) only works with a small amount of data. The data processing and computation are performed in parallel over the nodes in the cluster.

Deciding whether or not Spark is the best solution for your problem:
- Is my data too big to work with on a single machine?
- Can my calculations be easily parallelized?

sc - SparkContext - connection to the cluster
spark - SparkSession - interface with that connection, platform for cluster computing.

for the rest of this course:
	sc is a SparkContext
	spark is a SparkSession

SparkSession
	is a platform for cluster computing
	lets you spread data and computations over clusters with multiple nodes (think of each node as a separate computer)
	data processing and computation are performed in parallel over the nodes in the cluster



Master & Worker concept
	The master sends the workers data and calculations to run, and they send their results back to the master.

Resilient Distributed Dataset (RDD): This is a low level object that lets Spark work its magic by splitting data across multiple nodes in the cluster.

You can think of the SparkContext as your connection to the cluster and the SparkSession as your interface with that connection.

SparkSession.builder.getOrCreate()
	returns an existing SparkSession if there's already one in the environment, or creates a new one if necessary

spark.catalog.listTables()
	catalog lists all the data inside the cluster
	listTables() returns the names of all the tables in your cluster as a list.

.toPandas() 
	Calling this method on a Spark DataFrame returns the corresponding pandas DataFrame
	
.createDataFrame()
	pandas DataFrame and returns a Spark DataFrame.

.createTempView()
.createOrReplaceTempView()

why deal with pandas at all? 
Wouldn't it be easier to just read a text file straight into Spark? 
A: Of course it would!
