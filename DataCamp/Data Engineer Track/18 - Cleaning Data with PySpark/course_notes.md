# Course Description

Working with data is tricky - working with millions or even billions of rows is worse. Did you receive some data processing code written on a laptop with fairly pristine data? Chances are you’ve probably been put in charge of moving a basic data process from prototype to production. You may have worked with real world datasets, with missing fields, bizarre formatting, and orders of magnitude more data. Even if this is all new to you, this course helps you learn what’s needed to prepare data processes using Python with Apache Spark. You’ll learn terminology, methods, and some best practices to **create a performant, maintainable, and understandable data processing platform**.


# Dataframe details
This chapter is a review of DataFrame fundamentals and the importance of data cleaning. 

What is Data Cleaning?
- Preparing raw data for use in data processing pipelines.
- Possible tasks in data cleaning
    - Reformatting or replacing text
    - Performing calculations
    - Removing garbage or incomplete data
- It is a necessary part of any production data system, *because if your data isn't clean, it's not trustworthy and could cause problemas later on*

Why perform data cleaning with Spark?
- Performance
- Organizing data flow
- Scalable (The primary limit to Spark's abilities is the level of RAM in the Spark cluster)
- Powerful framework for data handling
- *Most data cleaning systems have two big problems: optimizing performance and organizing the flow data*

Spark Schemas:
- Define the format of a DataFrame
- May contain various data types:
    - strings, dates, integers, arrays...
- Can filter garbage data during import
- improves read performance

```python
# Import schema
import pyspark.sql.types
peopleSchema = StructType([
    # Define the name field
    StructField('name', StringType(), True),
    # Add the age field
    StructField('age', IntegerType(), True),
    # Add the city field
    StructField('city', StringType(), True)
])

# read csv file containing data
people_df = spark.read.format('csv').load(name='rawdata.csv', schema=peopleSchema)
```

## Immutability and Lazy Processing
Python mutable variables:
- Mutable: the values can be changed at any given time
- Potential for issues with concurrency

*Unlike typical Python variables, Spark DFs are immutables*. Immutability: 
- A component of functional programming
- Spark DFs are Defined once and are not modifiable after initialization
- Unable to be directly modified
- Re-created if reassigned ( if the variable name is reused, the original data is removed, and the variable name is reassigned to the new data)
- Able to be shared efficiently

Lazy Processing
- In Spark, it is the idea that very little actually happens until an action is performed
- This functionality allows Spark to perform the most efficient set of operations to get the desired result.
- Transformations (update the instructions for what we wanted Spark do; No data was read/added/modified)
- Actions (e.g. ```voter_df.count()```)
- *Lazy processing operations will usually return in about the same amount of time regardless of the actual quantity of data. Remember that this is due to Spark not performing any transformations until an action is requested.*

```python
# Immutability example

# Define a new data frame
voter_df = spark.read.csv('voterdata.csv')

# Making changes
voter_df = voter_df.withColumn('fullyear',
    voter_df.year + 2000)
voter_df = voter_df.drop(voter_df.year)
```

## Understanding Parquet
Difficulties with CSV files
- No defined schema
- Nested data requires special handling
- Enconding format limited

Spark and CSV files
- Slow to parse.*The file cannot be shared between workers during the import process*
- Files cannot be filtered (no "predicate pushdown")
    - *pushdown: This means Spark will only process the data necessary to complete the operations you define versus reading the entire dataset./*
- Any intermediate use requires redefining schema

The Parquet Format
- A columnar data format
- Supported in Spark and other data processing frameworks
- Supports predicate pushdown
- Automatically stores schema information
- Parquet files are a binary file format and can only be used with the proper tools

```python
# Reading parquet files
df = spark.read.format('parquet').load('filename.parquet')
df = spark.read.parquet('filename.parquet')

# writing parquet files
df.write.format('parquet').save('filename.parquet')
df.write.parquet('filename.parquet')

# Parquet and SQL
flight_df = spark.read.parquet('flights.parquet')
flight_df.createOrReplaceTempView('flights')
short_flights_df = spark.sql('SELECT * FROM flights WHERE flightduration < 100')
```

```python
# View the row count of df1 and df2
print("df1 Count: %d" % df1.count())
print("df2 Count: %d" % df2.count())

# Combine the DataFrames into one
df3 = df1.union(df2)

# Save the df3 DataFrame in Parquet format
df3.write.parquet('AA_DFW_ALL.parquet', mode='overwrite')

# Read the Parquet file into a new DataFrame and run a count
print(spark.read.parquet('AA_DFW_ALL.parquet').count())
```
# Dataframe details
This chapter is a review of DataFrame fundamentals and the importance of data cleaning. 

## DataFrame column operations
DataFrame recap:
- Made up of rows and columns
- Immutable
- Use various transformation operations to modify data

Common DataFrame transformations
- Filter/where
- Select
- withColumn
- drop

ArrayType() column functions
- Various utility functions / transformations to interact with ArrayType()
- .size(<column>) - returns length of arrayType() column
- .getItem(<index>) - used to retrieve a specific item at index of list column.

```python
# Return rows where name starts with "L"
voter_df.filter(voter_df.name.like('M%'))

# Return name and position only
voters = voter_df.select('name', 'position')


# Filter/where
voter_df.filter(voter_df.date > '1/1/2019') # or voter_df.where(...)

# Select
voter_df.select(voter_df.name)

# withColumn
voter_df.withColumn('year', voter_df.date.year)

# drop
voter_df.drop('unused_column')

# Remove nulls
voter_df.filter(voter_df['name'].isNotNull())

# Remove odd entries
voter_df.filter(voter_df.date.year > 1800)

#Split data from combined sources
voter_df.where(voter_df['_c0'].contains('VOTE'))

# Negate with ~
voter_df.where(~ voter_df._c1.isNull())


# Contained in pyspark.sql.functions
import pyspark.sql.functions as F

# Applied per column as transformation
voter_df.withColumn('upper', F.upper('name'))

# create intermediary columns
voter_df.withColumn('splits', F.split('name', ' '))

# cast to other types
voter_df.withColumn('year', voter_df['_c4'].cast(IntegerType()))

```

# Manipulating Dataframes in the real world
A look at various techniques to modify the contents of DataFrames in Spark.


## Conditional DataFrame column operations

Conditional clauses are:
- inline version of if then and else
- ```.when({if condition}, {then x})```. The when() clause lets you conditionally modify a Data Frame based on its content. 
- ```.otherwise()```; it's like else.

```python
df.select(df.Name, df.Age,
    .when(df.Age >= 18, "Adult")
    .otherwise("Minor"))
```

## User Defined Functions (UDFs)

User defined functions:
- Python method
- Wrapped via the pypark.sql.functions.udf method
- Stored as a variable
- Called like a normal Spark function

```python
# Step 1 Define a Python method
def reverseString(mystr):
    return mystr[::-1]

# Step 2 Wrap the function and store as a variable
udfReverseString = udf(reverseString, StringType())

# Step 3 Use with Spark
user_df = user_df.withColumn('ReverseName',
    udfReverseString(user_df.Name))

# Other example:
def sortingCap():
    return random.choice(['G', 'H', 'R', 'S']) # Step 1
udfSortingCap = udf(sortingCap, StringType()) # Step 2
user_df = user_df.withColumn('Class', udfSortingCap()) # Step 3
```

## Partitioning and lazy processing

Partitioning:
- DataFrame are broken up into partitions
- Partition size can vary
- Each partition is handled independently

Lazy processing
- Transformations are lazy
- **Nothing is actually done until an action is performed**
- Transformation can be re-ordered for best performance
- Sometimes causes unexpected behavior 

Adding IDs (Monotonically increasing IDs)
- ```pyspark.sql.functions.monotonically_increasing_id()```
- Integer (64-bit), increases in value, unique
- Not necessarily sequential (gaps exist)
- Completely parallel
- Occasionally out of order
- If performing a join, ID may be assigned after the join
- Test your transformations


# Improving performance
Improve data cleaning tasks by increasing performance or reducing resource requirements. 

## Caching


What is caching? 
- Caching in Spark refers to storing the results of a DataFrame in memory or on disk of the processing nodes in a cluster
- It improves speed on later transformations/actions because the data no longer needs to be retrieved from the original data source.
- Using caching reduces the resource utilization of the cluster. There is less need to access the storage, networking, and CPU of the Spark nodes.

What is the disavantages of caching?
- Very large data sets may not fit in memory
- Depending on the later transformations requested, the cache may not do anything to help performance.
    - If you're reading from a local network resource and have slow local disk I/O, it may better to avoid caching the objects
- Cached objects may not be available. The lifetime of a cached object is not guaranteed

When developing Spark tasks:
- Caching is incredibly useful, but only if you plan to use the DataFrame again
- Try caching DataFrames at several configurations and determine if your performance improves
- Cache in memory and fask SSD/NVM3 storage
- Cache to slow local disk if needed
- Use intermediate files
- Stop caching objects when finished

Implementing caching
- Call ```.cache()``` on the DataFrame before Action


```python
# Implementing caching
voter_df = spark.read.csv('voter_data.txt.gz')
voter_df.cache().count()

voter_df = voter_df.withColumn('ID', monotonically_increasing_id())
voter_df = voter_df.cache()
voter_df.show()

# Determine cache status
print(voter_df.is_cached)

# Call .unpersist() when finished with DataFrame
voter_df.unpersist()
```

## Improve import performance

Spark clusters are made of two types of processes
- Driver process
    - The driver handles task assignments and consolidation of the data results from the workers
- Worker processes
    - The workers typically handle the actual transformation/action tasks of a Spark job

Important parameters to import performance:
- Number of objects (Files, Network locations, etc)
    - More objects better than larger ones. Using split files runs more quickly than using one large file for import. 
        *Note that in certain circumstances the results may be reversed. This is a side effect of running as a single node cluster.*
    - Can import via wildcard: ```airport_df = spark.read.csv('airports-*.txt.gz')```
- General size of objects
    - Spark performs better if objects are of similar size


A well-defined schema will drastically improve import performance
- Avoids reading the data multiple times
- Provides validation on import

How to split objects
- Use OS utilities/scripts (e.g.: split, cut, awk)
    ```bash
    split -l 10000 0d 00additional-suffix=.csv largefile largefile_output_name

    ```
- Use custom scripts
- Write out to Parquet
```python
df_csv = spark.read.csv('singlelargefile.csv')
df_csv.write.parquet('data.parquet')
df = spark.read.parquet('data.parquet')
```

## Cluster sizing tips
The configurations are available in the configuration files, via the Spark web interface, and via the run-time code
Configuration options
- Spark contains many configuration settings
- These can be modified to match needs
- Reading configuration settings ```spark.conf.get(<configuration name>)```
- Writing configuration settings ```spark.conf.set(<configuration name>)```

Cluster Types
- Single node
- Standalone
- Managed (components are handled by a third party cluster manager such the items below)
    - YARN
    - Mesos
    - Kubernetes

Driver
The driver is responsible for several things, including:
- Handling task assignment to the various nodes/processes in the cluster
- The driver monitors the state of all processes and tasks and handles any task retries
- also responsable for consolidating results from the other processes in the cluster.
- The driver handles any access to shared data and verifies each worker process has the necessary resources (code, data, etc.)
- Tips:
    - Driver node should have double the memory of the worker
    - Fast local storage helpful

Worker
A Spark worker handles running tasks assigned by the driver and communicates those results back to the driver
- Runs actual tasks
- Ideally has all code, data, and resources for a given task. *If any of these are unvailable, the worker must pause to obtain the resources*
- Recommendations
    - More worker nodes is often better than larger workers
    - Test to find the balance
    - Fast local storage extremely useful

Using the spark.conf object allows you to validate the settings of a cluster without having configured it initially. This can help you know what changes should be optimized for your needs.
```python
# Name of the Spark application instance
app_name = spark.conf.get('spark.app.name')

# Driver TCP port
driver_tcp_port = spark.conf.get('spark.driver.port')

# Number of join partitions
num_partitions = spark.conf.get('spark.sql.shuffle.partitions')

# Show the results
print("Name: %s" % app_name)
print("Driver TCP port: %s" % driver_tcp_port)
print("Number of partitions: %s" % num_partitions)
```

## Performance improvement
Explaining the Spark execution plan. Learning to parse a query plan will help you understand what Spark is doing and when.

The easiest way to see what the Spark is doing under the hood is using the explain() function on a Dataframe. 
The results is the estimated plan that will be run to generate results from the DataFrame


What is shiffling?
Spark distributes data amongst the variours nodes in the clster. A side effect of this is what is known as shuffling.Shuffing refers to moving data fragments to various workers to complete a task
- Hides complexity from the user ( The user doesn't have to know which nodes have what data)
- Can be slow to complete
- Lowers overall throughput
- If often necessary but try to minimize

How to limit shuffling?
Repartitioning requires a full shuffle of data between nodes & processes and is quite costly.
- Limit use of .repartition(num_partitions)
    - Use .coalesce(num_partitions) instead, if you need to reduce the number of partitions
    - coalesce function takes a number of partitions smaller than the current one and consolidates the data without requiring a full data shuffle
- Use care when calling .join. Calling join() indiscriminately can often cause shuffle operations leading to increased cluster load & slower processing times.
- Use broadcast() to avoid some of the suffle operations when joining Spark DataFrames
- May not need to limit it


Broadcasting
- Provides a copy of an object to each worker
- Prevents undue/excess communication between nodes
    - When each worker has its own copy of the data, there is less need for communication between nodes
- Can drastically speed up .join() operations
- Broadcasting can drastically speed up join operations, especially if one of the DataFrames being joined is much smaller than the other.
- Broadcasting can slow operations when using very small DataFrames or if you broadcast the larger DataFrame in a join.


A couple tips:

- Broadcast the smaller DataFrame. The larger the DataFrame, the more time required to transfer to the worker nodes.
- On small DataFrames, it may be better skip broadcasting and let Spark figure out any optimization on its own.
- If you look at the query execution plan, a broadcastHashJoin indicates you've successfully configured broadcasting

```python
# Use the .broadcast(<DataFrame>) method
from pyspark.sql.functions import broadcast
combined_df = df_1.join(broadcast(df_2))


# Show the query plan
normal_df.explain()


# Comparing broadcast vs normal joins
start_time = time.time()
# Count the number of rows in the normal DataFrame
normal_count = normal_df.count()
normal_duration = time.time() - start_time

start_time = time.time()
# Count the number of rows in the broadcast DataFrame
broadcast_count = broadcast_df.count()
broadcast_duration = time.time() - start_time

# Print the counts and the duration of the tests
print("Normal count:\t\t%d\tduration: %f" % (normal_count, normal_duration))
print("Broadcast count:\t%d\tduration: %f" % (broadcast_count, broadcast_duration))
```

# Complex processing and data pipelines 
Learn how to process complex real-world data using Spark and the basics of pipelines.

## Introduction to data pipelines
What is a data pipeline?(Focus on Spark)
- A set of steps to process data from source(s) to final output
- Can consist of any number of steps or components
- Can span many systems

What does a data pipeline look like?
1. Inputs
    - csv, json, web services, databases
1. Transformations
    - withColumn(), filter(), drop()
1. Outputs
    - csv, parquet, database
1. Validation
1. Analysis

Pipeline details
- Not formally defined in Spark
- Typically all normal Spark code required for task. E.g:


```python
# Example 1
schema = StructType([
StructField('name', StringType(), False),
StructField('age', StringType(), False)
])
df = spark.read.format('csv').load('datafile').schema(schema)
df = df.withColumn('id', monotonically_increasing_id())
...
df.write.parquet('outdata.parquet')
df.write.json('outdata.json')

# Example 2
# Import the data to a DataFrame
departures_df = spark.read.csv('2015-departures.csv.gz', header=True)

# Remove any duration of 0
departures_df = departures_df.filter(departures_df['Actual elapsed time (Minutes)'] != 0)

# Add an ID column
departures_df = departures_df.withColumn('id', F.monotonically_increasing_id())

# Write the file out to JSON format
departures_df.write.json('output.json', mode='overwrite')
```

## Data handling techniques
parse meaning: to examine computer data and change it into a form that can be easily read or understood 

Situations of data parses:
- Incorrect data
    - Empty rows
    - Commented lines
    - Headers
- Nested structures
    - Multiple delimiters
- Non-regular data
    - Differing numbers of columns per row

Removing blank lines, headers, and comments. Spark's CSV parser:
- Automatically removes blank lines
- Can remove comments using an optional argument
- Handles header fields
    - Defined via argument
    - Ignored if a schema is defined



Automatic column creation. Spark will:
- Automatically create columns in a DataFrame based on sep argument
- Can still successfully parse if sep is not in string
- Stores data in column defaulting to _c0
- Allows you to properly handle nested separators
- *Spark's CSV parser can't handle advanced types (Arrays or Maps) so it wouldn't process correctly. Use a schema to define the content layout*

```python
# Remove comments
df1 = spark.read.csv('datafile.csv.gz', comment='#')

# Handle header field
df1 = spark.read.csv('datafile.csv.gz', header='True')

# Automatically create columns
df1 = spark.read.csv('datafile.csv.gz', sep=',')
```

## Data Validation
Let's look at how to implement validation steps in a data cleaning pipeline.

The definition of data validation  is:
- Verifying that a dataset complies with the expected format
- Number of rows / columns is as expected
- Data types
- Complex validation rules

Validating via joins:

Validating  via join will compare data against a set of known values
- Compares data against known values
- Easy to find data in a given set
- Joins are also comparatively fast, especially vs validating individual rows against a long list of entries.
    - The simplest example of this is using an inner join of two DataFrames to validate the data.
    - In the # validating via join code, only rows from parsed_df with company names that are present in company_df would be included in the verified_df DataFrame. This has the effect of automatically filtering out any rows that don't meet the specified criteria.
- Another example of filtering data is using joins to remove invalid entries.

**Complex rule validation** is the idea of using Spark components to validate logic:
- Calculations
- Verifying against external source
- Likely uses a UDF to modify/verify the DataFrame

Analysis calculations are the process of using the columns of data in a dataframe to compute some useful value using Spark's functionality

```python
# validating via joins
parsed_df = spark.read.parquet('parsed_data.parquet')
company_df = spark.read.parquet('companies.parquet')
verified_df = parsed_df.join(company_df, parsed_df.company == company_df.company)
# This automatically removes any rows with a company not in the valid_df !


#Analysis calculations (UDF)
def getAvgSale(saleslist):
    totalsales = 0
    count = 0
    for sale in saleslist:
        totalsales += sale[2] + sale[3]
        count += 2
    return totalsales / count
udfGetAvgSale = udf(getAvgSale, DoubleType())
df = df.withColumn('avg_sale', udfGetAvgSale(df.sales_list))


# inline calculations
df = df.read.csv('datafile')
df = df.withColumn('avg', (df.total_sales / df.sales_count))
df = df.withColumn('sq_ft', df.width * df.length)
df = df.withColumn('total_avg_size', udfComputeTotal(df.entries) / df.numEntries)
```