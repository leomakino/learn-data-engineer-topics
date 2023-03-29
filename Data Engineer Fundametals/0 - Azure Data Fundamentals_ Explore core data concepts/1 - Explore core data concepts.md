# Identify types of data and data storage
You can classify data as structured, semi-structured, or unstructured.
Structured data is typically tabular data that is represented by rows and columns in a database. Databases that hold tables in this form are called relational databases 


A transaction is a sequence of operations that are atomic. This means that either all operations in the sequence must be completed successfully, or if something goes wrong, all operations run so far in the sequence must be undone. 

# Describe the difference between batch and streaming data
Data processing is the conversion of raw data to meaningful information through a process. you could process each data item as it arrives (streaming), or buffer (batch) the raw data and process it in groups.

1. Batch processing
data elements are collected into a group. The whole group is then processed at a future time as a batch. You can process data based on a scheduled time interval (for example, every hour), or it could be triggered when a certain amount of data has arrived, or as the result of some other event.

Advantages:
- Large volumes of data can be processed at a convenient time.
- It can be scheduled to run at a time when computers or systems might otherwise be idle{not working or being used}, such as overnight, or during off-peak hours.
	
Disadvantages: 
- The time delay between ingesting the data and getting the results.
- All of a batch job's input data must be ready before a batch can be processed.

Effective example of use:
- A connection to a mainframe system with a vast amount of data, which need to be transferred into a data analysis system that not require to be real-time. Cotesa example, batch all the data generation to construct generation report in the next day.
	
Ineffective example of use:
- transfer small amounts of critical and real-time data, such as financial stock-ticker.	

2. Streaming and real-time data
Streaming handles data in real time. It is beneficial in most scenarios where new, dynamic data is generated on a continual basis. It is ideal for time-critical operations that require an instant real-time response.

3. Differences between batch and streaming data
-Data Scope{to watch or examine something carefully}:Batch processing can process all the data in the dataset. Stream processing typically only has access to the most recent data received;
-Data Size: Batch handle with large datasets and Stream is intended for individual records or micro batches;
-Performance: The latency{being present but needing particular conditions to become active, obvious, or completely developed} for batch processing is typically a few hours. Stream processing typically occurs immediately, with latency in the order of seconds or milliseconds. 
-Analysis: atch processing for performing complex analytics, Stream for simple response functions, aggregates, or calculations

