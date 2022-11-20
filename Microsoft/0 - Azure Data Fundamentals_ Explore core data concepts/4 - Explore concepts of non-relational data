neat (tidy):tidy, with everthing in its place 
block blob:  a large, round drop block
encompassing: to include different types of things
all-encompassing: including or covering everything or everyone; comprehensive.
sparse: small in numbers or amount, often spread over a large area: 
\--Explore characteristics of non-relational data

What are the characteristics of non-relational data?
A:
A key aspect of non-relational databases is that they enable you to store data in a very flexible manner. They focus on the data itself rather than how to structure it. 
The data retrieval capabilities of a non-relational database can vary. Each entity should have a unique key value. 

Non-relational systems:
	Azure Cosmos DB

Non-relational databases often provide their own proprietary language for managing and querying data. This language may be procedural (follow a set of commands, in order), or it may be similar to SQL; it depends on how the database is implemented by the database management system.

Identify non-relational database use cases:
	IoT and telematics. These systems typically ingest large amounts of data in frequent bursts of activity. Non-relational databases can store this information very quickly. 
	Retail and marketing.
	Gaming: 
	Web and mobile applications: A non-relational database such as Azure Cosmos DB is commonly used within web and mobile applications, and is well suited for modeling social interactions, integrating with third-party services, and for building rich personalized experiences.

A relational database restructures the data into a fixed format that is designed to answer specific queries. When data needs to be ingested very quickly, or the query is unknown and unconstrained, a relational database can be less suitable than a non-relational database.

\--Describe types of non-relational data
Non-relational data generally falls into two categories:
	semi-structured;
	non-structured.
	
What is semi-structured data?
A: Semi-structured data is data that contains fields. The fields don't have to be the same in every entity. You only define the fields that you need on a per-entity basis.

Examples of semi-structured:
	JSON (JavaScript Object Notation): it's the format used by JavaScript applications to store data in memory, but can also be used to read and write documents to and from files. A JSON document is enclosed in curly brackets ({ and }). Each field has a name (a label), followed by a colon, and then the value of the field. Fields can contain simple values, or subdocuments (each starting and ending with curly brackets). Fields can also have multiple values, held as arrays and surrounded with square brackets ([ and ]). Literals, or fixed values, in a field are enclosed in quotes, and fields are separated with commas.
	Avro is a row-based format. It was created by Apache. 
	ORC (Optimized Row Columnar format) organizes data into columns rather than rows. It was developed by HortonWorks for optimizing read and write operations in Apache Hive. 
	Parquet is another columnar data format. It was created by Cloudera and Twitter. 
	
What is unstructured data?
A: Unstructured data is data that doesn't naturally contain fields. Examples include video, audio, and other media streams. Each item is an amorphous blob of binary data. You can't search for specific elements in this data.

\--Describe types of non-relational and NO SQL databases
Non-relational data is an all-encompassing term that means anything not structured as a set of tables.
There are many different types of non-relational database management systems, each oriented towards a specific set of scenarios.
*some non-relational databases support a version of SQL adapted for documents rather than tables (examples include Azure Cosmos DB).

What is NoSQL?
A: NoSQL is a rather loose term that simply means non-relational. NoSQL (non-relational) databases generally fall into four categories:
	key-value stores;
	document databases;
	column family databases;
	graph databases.

What is a key-value store?
A:Each data item in a key-value store has two elements, a key and a value. The key uniquely identifies the item, and the value holds the data for the item. The value is opaque to the database management system.
*opaque means that the database management system just sees the value as an unstructured block. E.g. Value: 1101011100011...


What is a document database?
A:each document has a unique ID, but the fields in the documents are transparent to the database management system. Document databases typically store data in JSON format.
*transparent: the database management system understands how the fields in the data are organized.

What is a column family database?
A: It organizes data into rows and columns. Examples: ORC and Parquet files. In its simplest form, a column family database can appear very similar to a relational database, at least conceptually. The real power of a column family database lies in its denormalized approach to structuring sparse data.

The diagram of the example shows some sample data. In this example, customer 1 and customer 3 share the same address, and the schema ensures that this address information is not duplicated.

You can think of a column family database as holding tabular data comprising rows and columns, but you can divide the columns into groups known as column-families. Each column family holds a set of columns that are logically related together.

The most widely used column family database management system is Apache Cassandra. Azure Cosmos DB supports the column-family approach through the Cassandra API.


What is a graph database?
A: A graph database stores two types of information: nodes that you can think of as instances of entities, and edges, which specify the relationships between nodes. 
The purpose of a graph database is to enable an application to efficiently perform queries that traverse the network of nodes and edges, and to analyze the relationships between entities.

Azure Cosmos DB supports graph databases using the Gremlin API. The Gremlin API is a standard language for creating and querying graphs.

