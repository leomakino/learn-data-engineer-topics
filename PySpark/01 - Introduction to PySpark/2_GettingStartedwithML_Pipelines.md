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
Spark requires numeric data for modeling. When strings are needed to model, there isn't any obvious way to convert them to a numeric data type. PySpark has functions for handling this built into the `pyspark.ml.features`. With this submodule, it is possible to create a *one-hot vector*. It is a way of representing a categorical feature where every observation has a vector in which all elements are zero except for at most one element, which has a value of one (1).

```python
# Create a StringIndexer
columnA_indexer = StringIndexer(inputCol="columnA", outputCol="columnA_index")

# Create a OneHotEncoder
columnA_encoder = OneHotEncoder(inputCol="columnA_index", outputCol="columnA_fact")

# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["ColumnX", "columnY", "columnA_fact"], outputCol="features")

# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])

# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)

# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])
```
