# Course Description
# Course Description
There's been a lot of buzz about Big Data over the past few years, and it's finally become mainstream for many companies. But what is this Big Data? This course covers the fundamentals of Big Data via PySpark. Spark is a "lightning fast cluster computing" framework for Big Data. It provides a general data processing platform engine and lets you run programs up to 100x faster in memory, or 10x faster on disk, than Hadoop. You’ll use PySpark, a Python package for Spark programming and its powerful, higher-level libraries such as SparkSQL, MLlib (for machine learning), etc. You will explore the works of William Shakespeare, analyze Fifa 2018 data and perform clustering on genomic datasets. At the end of this course, you will have gained an in-depth understanding of PySpark and its application to general Big Data analysis.

# Introduction to Big Data analysis with Spark 
this chapter introduces the exciting world of Big Data, as well as the various concepts and different frameworks for processing Big Data. You will understand why Apache Spark is considered the best framework for BigData. 

## Fundamentals of Big Data
Big data is a term to refer to the study and applications of data sets that are too complex for traditional data-processing software

The 3V's of Big Data:
- **Volume:** Size of the data
- **Variety:** Different sources and formats
- **Velocity:** Speed of the data

Concepts and Terminologies
- **Clustered computing:** Collection of resources of multiple machines
- **Parallel computing:** Simultaneous computation
- **Distributed computing:** Collection of nodes (networked computers) that run in parallel
- **Batch processing:** Breaking the job into small pieces and running them on individual machines
- **Real-time processing:** Immediate processing of data

Big data processing systems
- **Hadoop/MapReduce:** Scalable and fault tolerant framework written in Java
    - Open source and batch processing
- **Apacha Spark** General purpose and lightning fast cluster computing system
    - Open source and both batch and real-time data processing

Features of Apache Spark framework
- Distributed cluster computing framework
- Efficient in-memory computations for large data sets
- Lightning fast data processing framework
- Provides support for Java, Scala, Python, R and SQL.

Apache Spark Components:
- Spark SQL
- MLlib
- GraphX
- Spark Streaming
- Resilient Distributed Datasets (RDD) API (Apache Spark Core)
- *Note: RDDs in PySpark are a collection of partitions.*

Spark modes of deployment
- **Local mode:** Single machine, such as your laptop
    - Local model convenient for testing, debugging and demonstration
- **Cluster mode:** Set of pre-defined machines
    - Good for production
- Workflow: Local -> clusters
- No code change necessary

Pyspark: Spark with Python
- To support Python with Spark, Apache Spark Community released Pyspark
- Similar computation speed and power as Scala
- Pyspark APIs are similar to pandas and scikit-learn

Spark shell
- Interactive environment for running Spark jobs
- Helpful for fast interactive prototyping
- Spark's shells allow interacting with data on disk or in memory
- Three different Spark shells:
    - Spark-shell for Scala
    - Pyspark-shell for Python
    - SparkR for R

PySpark shell
- is the Python-based command line tool
- allows data scientists interface with Spark data structures
- support connecting to a cluster

Understanding SparkContext
- Spark Context is an entry of point into the world of Spark
- An entry point is where control is transferred from the OS to the provided program
- An entry of point is a way of connecting to Spark cluster
- An entry of point is like a key to the house
- Pyspark has a default SparkContext called sc

Inspecting SparkContext
```Python
# Print the version of SparkContext
print("The version of Spark Context in the PySpark shell is", sc.version)

# Print the Python version of SparkContext
print("The Python version of Spark Context in the PySpark shell is", sc.pythonVer)

# Print the master of SparkContext
print("The master of Spark Context in the PySpark shell is", sc.master)
```

Loading data in Pyspark

In PySpark, we express our computation through operations on distributed collections that are automatically parallelized across the cluster.

In the code below, you'll load the data from a local file in PySpark shell. 

```python
# SparkContext's parallelize() method
rdd = sc.parallelize([1,2,3,4,5])

# SparkContext's textFile() method
rdd2 = sc.textFile("text.txt")
```
What are anonymous functions in Python?
- Lambda functions are anonymous functions in Python
- Very powerful and used in Python. Quite efficient with ```map()``` and ```filter```()
- Lambda functions create functions to be called later similar to ```def```
- It returns the functions instead of assigning it to a namew. It returns functions without any name (i.e. anonymous)
- In practice, they are used as a way to inline a function definition or to defer execution of a code

Lambda function syntax
```python
# The general form of lambda function
lambda arguments: expression

# Example of lambda function
double = lambda x: x * 2
```

Difference between def vs lambda functions
- No return statement for lambda
- Can put lambda function anywhere
- Lambda function doesn't need to assign it to a variable, unlike def

```python
def cube(x):
    return x ** 3
g = lambda x: x ** 3
print(cube(10))
print(g(10))
```

Map() - Use of Lambda function in Python
- map() function takes a function and a list and returns a new list which contains items returned by that function for each item
```python
# General syntax of map()
map(function, list)

# Example of map()
items = [1,2,3,4]
list(map(lambda x: x + 3, items))
```

Filter() - Use of Lambda function in Python
- filter() function takes a function and a list and returns a new list for which the function evaluates as true

```python
# General syntax of filter()
filter(function, list)

# Example of filter()
items = [1,2,3,4]
list(filter(lambda x: x%2 != 0, items))
```

# Programming in PySpark RDD’s 
Chapter description: The main abstraction Spark provides is a resilient distributed dataset (RDD), which is the fundamental and backbone data type of this engine. This chapter introduces RDDs and shows how RDDs can be created and executed using RDD Transformations and Actions. 

RDDs
- resilient distributed dataset
- It is an immutable collection of data distributed across the cluster
- Spark's core abstraction for working with data
- Resilient: the ability to withstand failures and recompute missing or damaged partitions 
- Distributed: spanning the jobs across multiple nodes in the cluster (for efficient computation)
- Datasets: a collection of partitioned data

When Spark starts processing data, it divides the data into partitions and distributes the data across cluster nodes, with each node containing a slice of data.

How to create RDDs
- Parallelizing an existing collection of objects
    - RDDs are created from a list or a set using SparkContext's parallelize method (parallelize())
- External datasets
    - A more common way to do it is to load data from external datasets such as files stored in HDFS or objects in buckets
    - textFile() for creating RDDs from external datasets
    - lines in a text file:
- From existing RDDs

```python
# RDD created from a Python list
num_RDD = sc.parallelize([1,2,3,4])

# RDD created from a Python string
str_RDD = sc.parallelize("This is a string")

# RDD created using textFile method
file_RDD = sc.textFile("README.md")

# getNumPartitions()
file_RDD.getNumPartitions()
```

Partitions
- A partition is a logical division of a large distributed data set



# PySpark SQL & DataFrames 
In this chapter, you'll learn about Spark SQL which is a Spark module for structured data processing. It provides a programming abstraction called DataFrames and can also act as a distributed SQL query engine. This chapter shows how Spark SQL allows you to use DataFrames in Python. 

# Machine Learning with PySpark MLlib 
PySpark MLlib is the Apache Spark scalable machine learning library in Python consisting of common learning algorithms and utilities. Throughout this last chapter, you'll learn important Machine Learning algorithms. You will build a movie recommendation engine and a spam filter, and use k-means clustering. 