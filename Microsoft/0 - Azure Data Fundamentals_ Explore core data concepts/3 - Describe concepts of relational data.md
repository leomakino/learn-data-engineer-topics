retrieve: to get stored information from a computer.

statement: an act/something you write officially to express an opinion

fetches(GET):to go to another place to get something or someone and bring it, him, or her back

spans: to exist or continue for a particular length of time: 

Ad hoc: made or happening only for a particular purpose or need, not planned before it happens

Comprise: to consist of, be made up of

Apart from: except for 

paramount: More important than anything else

Scalability: The ability of a business or system to grow larger
Expenditure

index: like a summary. A collection of information stored on a computer, in alphabetical order.
# Explore the characteristics of relational data

In a relational database, you model collections of entities from the real world as tables.

An entity is described as a thing about which information needs to be known or held.

A table contains rows, and each row represents a single instance of an entity.

Columns define the properties of the entity.

All rows in the same table have the same columns. 

Some columns are used to maintain relationships between tables.

Examples:
1. each row in the customers table contains the data for a single customer 
1. each column a property such as the customer name.

The primary key indicates the column (or combination of columns) that uniquely identify each row. Every table should have a primary key.

There are the relationships between the tables.

The lines connecting the tables indicate the type of relationship. In this case, the relationship from customers to orders is 1-to-many (one customer can place many orders, but each order is for a single customer). the relationship between orders and products is many-to-1 (several orders might be for the same product).

Foreign Key (FK) columns reference, or link to, the primary key of another table, and are used to maintain the relationships between tables. A foreign key also helps to identify and prevent anomalies, such as orders for customers that don't exist in the Customers table.

All data is tabular. Entities are modeled as tables, each instance of an entity is a row in the table, and each property is defined as a column.

Normalization: split an entity into more than one table.

SQL Commands
- CREATE TABLE - create tables, command to create a table;
- INSERT - insert, statement to store data in a table;
- UPDATE - update, statement to modify data in a table;
- DELETE - delete statement to remove rows from a table;
- SELECT - to query, statement retrieves data from a table;
- WHERE - filter data;
- JOIN - combine the data from multiple tables in a query.


Online Transaction Processing (OLTP) applications are focused on transaction-oriented tasks that process a very large number of transactions per minute. Relational databases are well suited for OLTP applications. Also, the nature of SQL makes it easy for users to perform ad-hoc (made or happening only for a particular purpose or need, not planned before it happens: ) queries over data.

# Explore relational data structures
Define relationships between tables using primary and foreign keys.

What is an index?
A: Think of an index over a table like an index at the back of a book. It contains a sorted set of references, with the pages on which each reference occurs. 

When you create an index in a database, you specify a column from the table. When the user runs a query that specifies this column in the WHERE clause, the database management system can use this index to fetch the data more quickly than if it had to scan through the entire table row by row. 

You can create many indexes on a table. However, indexes aren't free. An index might consume additional storage space, additional work, and incur additional processing charges.

Therefore, when deciding which indexes to create, you must strike a balance between having indexes that speed up your queries versus the cost of performing other operations.


In a table that is read only, or that contains data that is modified infrequently, more indexes will improve query performance. If a table is queried infrequently, but subject to a large number of inserts, updates, and deletes (such as a table involved in OLTP), then creating indexes on that table can slow your system down.

What is clustered index?
A:

What is a view?
A: A view is a virtual table based on the result set of a query.
```SQL	
	CREATE VIEW P1Orders AS
	SELECT CustomerID, OrderID, Quantity
	FROM Orders
	WHERE ProductID = "P1"
```

# Choose the right plataform for a relational workload
Cloud computing:
- flexibility;
- Save time and money;
- Improve agility and scalability.

On-premises applications:
- reliable;
- secure;
- allow enterprises to maintain close control.
	
What is IaaS?
A:Infrastructure-as-a-Service; Virtual infrastructure in the cloud that mirrors the way an on-premises data center might work. Azure enables you to create it.
Eg.:
- virtual machines;
- virtual network;
- virtual devices;

You can think of IaaS as a transition to fully managed operations in the cloud; you don't have to worry about the hardware, but running and managing the software is still very much your responsibility: installing and configuring the software, patching, taking backups, and restoring data.

What is Paas?
A:Platform-as-a-service. Rather than creating a virtual infrastructure, and installing and managing the database software yourself, a PaaS solution does this for you. 

You specify the resources that you require (based on how large you think your databases will be, the number of users, and the performance you require), and Azure automatically creates the necessary virtual machines, networks, and other devices for you.

Azure PaaS solutions:
- Azure SQL Database;
- Azure Database for PostgreSQL;
- Azure Database for MySQL;
- Azure Database for MariaDB.
	
These services run managed versions of the database management systems on your behalf. You just connect to them, create your databases, and upload your data

