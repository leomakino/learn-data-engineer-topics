## Getting to know PySpark
**What is Spark?**
It is an open-source, distributed processing system used for big data workloads.

**What is cluster computing?**

A cluster is a group of inter-connected computers or hosts that work together to support applications and middleware (e.g. databases). In a cluster, each computer is referred to as a “node”.

Splitting up your data makes it easier to work with very large datasets because each node (separate computer) only works with a small amount of data. The data processing and computation are performed in parallel over the nodes in the cluster.

**When to use Spark?**

Deciding whether or not Spark is the best solution for your problem:
- Is my data too big to work with on a single machine?
- Can my calculations be easily parallelized?

*Running simpler computations might take longer than expected. That's because all the optimizations that Spark has under its hood are designed for complicated operations with big data sets. That means that for simple or small problems Spark may actually perform worse than some other solutions.*


--------------------
### Using Spark in Python
The first step in using Spark is connecting to a cluster.

In large organizations, the cluster will be hosted on a remote machine that's connected to all other nodes. There will be one computer, called the master that manages splitting up the data and the computations.

The master is connected to the rest of the computers in the cluster, which are called worker. The master sends the workers data and calculations to run, and they send their results back to the master.

When getting started with Spark it's simpler to just run a cluster locally.


Creating the connection is as simple as creating an instance of the **SparkContext** class. The class constructor takes a few optional arguments that allow you to specify the attributes of the cluster you're connecting to. An object holding all these attributes can be created with the **SparkConf** constructor.

**How do you connect to a Spark cluster from PySpark?**

Creating an instance of the **SparkContext** class



--------------------------------------------

Spark's core data structure is the **Resilient Distributed Dataset (RDD)**.  This is a low level object that lets Spark splitting data efficiently across multiple nodes in the cluster. **DataFrames** are also more optimized for complicated operations than RDDs.


To start working with Spark DataFrames, you have to create a SparkSession object from your SparkContext. **The SparkContext is the connection to the cluster and the SparkSession is the interface with that connection.** 


**Which of the following is an advantage of Spark DataFrames over RDDs?**
When using RDDs, it's up to the person to figure out the right way to optimize the query, but the DataFrame implementation has much of this optimization built in.


---------------------------


Creating multiple SparkSessions and SparkContexts can cause issues, so it's best practice to use the SparkSession.builder.getOrCreate() method.

SparkSession has an attribute called catalog which lists all the data inside the cluster.

It's possible to run SQL queries on the tables in your Spark cluster when using DataFrame interface.

Sometimes it makes sense to then take that table and work with it locally using a tool like pandas. Spark DataFrames make that easy with the .toPandas() method. 

To put a pandas DataFrame into a Spark cluster, use the .createDataFrame() method taking a pandas. The output of this method is stored locally, not in the SparkSession catalog. This means that you can use all the Spark DataFrame methods (e.g. sql()) on it, but you can't access the data in other contexts.


**Why deal with pandas at all?**

```python
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print the tables in the catalog
print(spark.catalog.listTables())

# Variable to execute a query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()

# Convert the results to a pandas DataFrame
pd_df = flights10.toPandas()

# Print the head of pd_counts
print(pd_df.head())

# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(spark.catalog.listTables())

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")

# Examine the tables in the catalog again
print(spark.catalog.listTables())

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()

```



----------------------

sc - 
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
