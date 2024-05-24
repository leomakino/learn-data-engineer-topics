## Manipulating Data 
In this chapter, the course explores the pyspark.sql module, which provides optimized data queries to your Spark session.

*sc - SparkContext - connection to the cluster
spark - SparkSession - interface with that connection, platform for cluster computing.* 

--------------

Updating a Spark DataFrame is somewhat different than working in pandas because the Spark DataFrame is immutable. This means that it can't be changed, and so columns can't be updated in place. To overwrite the original DataFrame you must reassign the returned DataFrame using the method like below:

```python
df = df.withColumn("newCol", df.oldCol + 1)
```

The withColumn method creates a DataFrame with the same columns plus a new column. The filter method correspond to the SQL's `WHERE` clause. The .filter() method takes either an expression that would follow the WHERE clause of a SQL expression as a string, or a Spark Column of boolean (True/False) values. In other words, Spark's .filter() can accept any expression that could go in the WHERE clause of a SQL query.


The Spark variant of SQL's SELECT is the `.select()` method. The arguments can either be the column name as a string (one for each column) or a column object (using the df.colName syntax). This method returns a column.

It is possible to use `alias()` method to rename a column. `.selectExpr()` takes SQL expressions as a string and can be used to alter a column too.

```python
# Create the DataFrame flights
flights = spark.table("flights")

# Filter something case A: String that could go in the WHERE clause
filtered_df = table_name.filter("column_name > 1000")

# Filter something case B: Spark Column
filtered_df2 = table_name.filter(table_name.sparkColumn > 1000)

# Define a column using select and alias
selected_df1 = table_name.select((table_name.columnA+20).alias("NewColumnA"))

# Create the same table above using a SQL expression
selected_df2 = table_name.selectExpr("columnA + 20 as NewColumnA")
```

### Aggregating
aggregation methods, like `.min(), .max(), and .count()` are GroupedData methods. These are created by calling the `.groupBy()` method.


PySpark has a whole class devoted to grouped data frames: pyspark.sql.GroupedData.


The `.agg()` method allows to pass an aggregate column expression that uses any of the aggregate functions from the pyspark.sql.functions submodule. All the aggregation functions in this submodule take the name of a column in a GroupedData table.

```python
# Find the minimum value of a column called col
df.groupBy().min("col").show()

# Group by col
grouped_data = table_name.groupBy("col")

# Execute an aggregate method into a grouped data
grouped_data.count().show()
```


### Joining
In PySpark, joins are performed using the `.join()` method.

```
tableA_with_tableB = tableA.join(tableB,"columnX","leftouter")
```
