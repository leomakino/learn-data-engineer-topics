## Manipulating Data 
In this chapter, the course explores the pyspark.sql module, which provides optimized data queries to your Spark session.

--------------

Updating a Spark DataFrame is somewhat different than working in pandas because the Spark DataFrame is immutable. This means that it can't be changed, and so columns can't be updated in place. To overwrite the original DataFrame you must reassign the returned DataFrame using the method like below:

```python
df = df.withColumn("newCol", df.oldCol + 1)
```

The withColumn method creates a DataFrame with the same columns plus a new column. The filter method correspond to the SQL's `WHERE` clause. The .filter() method takes either an expression that would follow the WHERE clause of a SQL expression as a string, or a Spark Column of boolean (True/False) values. In other words, Spark's .filter() can accept any expression that could go in the WHERE clause of a SQL query.


The Spark variant of SQL's SELECT is the `.select()` method. The arguments can either be the column name as a string (one for each column) or a column object (using the df.colName syntax).

```python
# Create the DataFrame flights
flights = spark.table("flights")

# Filter something case A: String that could go in the WHERE clause
filtered_df = table_name.filter("column_name > 1000")

# Filter something case B: Spark Column
filtered_df2 = table_name.filter(table_name.sparkColumn > 1000)
```


All the sql methods return new DataFrames. 

in a nutshell: using as few words as possible

sc - SparkContext - connection to the cluster
spark - SparkSession - interface with that connection, platform for cluster computing.

\--
Spark DataFrame is immutable
Pandas DataFrame is mutable

DataFrame.withColumn(colName, col)
	can make new columns derived from the old ones!
	
GROUP BY origin tells SQL that you want the output to have a row for each unique value of the origin column

It's possible to GROUP BY more than one column. When you do this, the resulting table has a row for every combination of the unique values in each column. 

Filtering Data
	.filter() = WHERE clause
	.select() = SELECT
	.alias() = AS
	
flights.filter("air_time > 120").show()
	can accept any expression that could go in the WHEREclause of a SQL query, as long as it is passed as a string
flights.filter(flights.air_time > 120).show()
	pass a column of boolean values. It returns a column of boolean values that has True in place of those records in flights.air_time that are over 120, and False otherwise.
	
temp = flights.select(flights.origin, flights.dest, flights.carrier)
selected1 = flights.select("tailnum", "origin", "dest")

flights.select((flights.air_time/60).alias("duration_hrs"))
flights.selectExpr("air_time/60 as duration_hrs")

All of the common aggregation methods, like .min(), .max(), and .count() are GroupedData methods. These are created by calling the .groupBy()
	df.groupBy().min("col").show()
	
.agg()
	lets you pass an aggregate column expression that uses any of the aggregate functions from the pyspark.sql.functions submodule.
	
.join()
		
