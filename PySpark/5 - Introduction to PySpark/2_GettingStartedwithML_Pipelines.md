## Getting started with machine learning pipelines
PySpark has built-in, cutting-edge machine learning routines, along with utilities to create full machine learning pipelines. 

At the core of the pyspark.ml module are the Transformer and Estimator classes. 

**Transformer** classes have a `.transform()` method that takes a DataFrame and returns a new DataFrame; 


**Estimator** classes all implement a `.fit()` method. These methods also take a DataFrame, but instead of returning another DataFrame they return a model object. 

Spark only handles numeric data. That means all of the columns in your DataFrame must be either integers or decimals (called 'doubles' in Spark).

Spark doesn't always infer corretly the data types. Therefore, there are methods to convert datatypes. `.cast()` is used to convert string to integer.

```python
# Cast the column to integers
dataframe = dataframe.withColumn("col", dataframe.col.cast("new_type"))

# Create a column that subtracts columnA from columnB
model_data = model_data.withColumn("columnA_B", model_data.columnA - model_data.columnB)
```


Strings and factors:
	Spark requires numeric data for modeling.
	These are values coded as strings and there isn't any obvious way to convert them to a numeric data type
	PySpark has functions for handling this built into the pyspark.ml.features submodule
		You can create what are called 'one-hot vectors' 
	A one-hot vector is a way of representing a categorical feature where every observation has a vector in which all elements are zero except for at most one element, which has a value of one (1).
	The first step to encoding your categorical feature is to create a StringIndexer
	Estimators that take a DataFrame with a column of strings and map each unique string to a number.
	Estimator returns a Transformer
	Transformer takes a DataFrame and returns a new DataFrame with a numeric column corresponding to the string column.
	The second step is to encode this numeric column as a one-hot vector using a OneHotEncoder
	All you have to remember is that you need to create a StringIndexer and a OneHotEncoder
	
VectorAssembler
	takes all of the columns you specify and combines them into a new vector column.
