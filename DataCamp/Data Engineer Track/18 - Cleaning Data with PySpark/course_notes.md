# Course Description

Working with data is tricky - working with millions or even billions of rows is worse. Did you receive some data processing code written on a laptop with fairly pristine data? Chances are you’ve probably been put in charge of moving a basic data process from prototype to production. You may have worked with real world datasets, with missing fields, bizarre formatting, and orders of magnitude more data. Even if this is all new to you, this course helps you learn what’s needed to prepare data processes using Python with Apache Spark. You’ll learn terminology, methods, and some best practices to **create a performant, maintainable, and understandable data processing platform**.

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


# Improving performance
Improve data cleaning tasks by increasing performance or reducing resource requirements. 

# Complex processing and data pipelines 
Learn how to process complex real-world data using Spark and the basics of pipelines.