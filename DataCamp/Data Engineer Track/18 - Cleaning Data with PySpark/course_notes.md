# Course Description

Working with data is tricky - working with millions or even billions of rows is worse. Did you receive some data processing code written on a laptop with fairly pristine data? Chances are you’ve probably been put in charge of moving a basic data process from prototype to production. You may have worked with real world datasets, with missing fields, bizarre formatting, and orders of magnitude more data. Even if this is all new to you, this course helps you learn what’s needed to prepare data processes using Python with Apache Spark. You’ll learn terminology, methods, and some best practices to **create a performant, maintainable, and understandable data processing platform**.


# Dataframe details
This chapter is a review of DataFrame fundamentals and the importance of data cleaning. 



# Manipulating Dataframes in the real world
A look at various techniques to modify the contents of DataFrames in Spark.


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

# Complex processing and data pipelines 
Learn how to process complex real-world data using Spark and the basics of pipelines.