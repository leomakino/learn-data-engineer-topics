# Course Description
A good database design is crucial for a high-performance application. Just like you wouldn't start building a house without the benefit of a blueprint, you need to think about how your data will be stored beforehand. Taking the time to design a database saves time and frustration later on, and a well-designed database ensures ease of access and retrieval of information. While choosing a design, a lot of considerations have to be accounted for. In this course, you'll learn how to process, store, and organize data in an efficient way. You'll see how to structure data through normalization and present your data with views. Finally, you'll learn how to manage your database and all of this will be done on a variety of datasets from book sales, car rentals, to music reviews.

# Processing, Storing, and Organizing Data
Start your journey into database design by learning about the two approaches to data processing, OLTP and OLAP. In this first chapter, you'll also get familiar with the different forms data can be stored in and learn the basics of data modeling. 

Motivating questions
- **How should we organize and manage data?** *It depends on the intended use of the data*
- How should my data be logically organized? Schemas
- Should my data have minimal dependency and redundancy? Normalization
- What joins will be done most often? Views
- Should all users of the data have the same level of access? Access control
- How do I pick between all the SQL and no SQL options? DBMS

## OLTP
Online Transaction Processing (OLTP) applications are focused on transaction-oriented tasks that process a very large number of transactions per minute. Relational databases are well suited for OLTP applications. Also, the nature of SQL makes it easy for users to perform ad-hoc (made or happening only for a particular purpose or need, not planned before it happens: ) queries over data.



## OLAP
Online analytical processing (OLAP) is a technology that organizes large business databases and supports complex analysis. It can be used to perform complex analytical queries without negatively affecting transactional systems.

## OLTP and OLAP

Example tasks:
| OLTP tasks                         | OLAP tasks                             |
|------------------------------------|----------------------------------------|
| Find the price of a book           | Calculate book with best profit margin |
| Update latest customer transaction | Find most loyal customers              |
| Keep track of employee hours       | Decide employee of the month           |

|         | OLTP                                   | OLAP                                         |
|---------|----------------------------------------|----------------------------------------------|
| Purpose | support daily transactions             | report and analyze data                      |
| Design  | application-oriented                   | subject-oriented                             |
| Data    | up-to-date, operational                | consolidated, historical                     |
| Size    | snapshot, gigabytes                    | archive, terabytes                           |
| Queries | simple transactions & frequent updates | complex, aggregate queries & limited updates |
| Users   | thousands                              | hundreds                                     |
| Normalization| Highly normalized| less normalized|
| Write/Read | Write-intensive | Read-intensive |
| Prioritize |  quicker and safer insertion of data| quicker queries for analytics|

## Structuring data
1. Structured data
- Follows a schema
- Defined data types
- e.g. SQL, tables in a relational database

2. Unstructured data
- Schemaless
- Makes up most of data in the world
- e.g. photos, chat logs, MP3

3. Semi-structured data
- Does not follow larger schema
- Self-describing structure
- e.g. NoSQL, XML, JSON

**Traditional databases** for storing real-time relational structured data - OLPT

**Data warehouses** for analyzing archived structured data - OLAP
- Optimized for analytics (OLAP): organized for reading/aggregating data and usually read-only
- Contains data from multiple sources
- Massively Parallel Processing (MPP)
- Typically uses a denormalized schema and dimensional modeling
- Data marts:
    - Subset of data warehouse
    - Dedicated to a specific topic

**Data lakes** for storing data of all structures and for analyzing big data
- Store all types of data at a lower cost
- Retains all data and can take up petabytes
- Schema-on-read as opposed to schema-on-write
- Need to catalog data otherwise becomes a data swamp
- Run big data analytics using services such as Apache Spark and Hadoop

## Database design
Database Design 
- Determines how data is logically stored
- Uses database models: high-level specifications for database structure
- Uses schemas: blueprint of the database
    - defines tables, fields, relationships, indexes, and views.


Data modeling: Process of creating a data model for the data to be stored
1. Conceptual data model: describes entities, relationships, and attributes.
    - Tools: data structure diagrams, e.g., entity-relational diagrams and UML diagrams
2. Logical data model: defines tables, columns relationships
    - Tools: database models and schemas, e.g., relational model and star schema
3. Physical data model: describes physical storage
    - Tools: partitions, CPUs, indexes, backup systems, and tablespaces.
4. Dimensional modeling: Adaptation of the relational model for data warehouse design
    - Optimized for OLAP queries: aggregate data, not updating (OLTP)
    - Built using the star schema
    - Easy to interpret and extend schema
    - Elements of dimensional modeling 
        - **Fact Tables**: 
        - Hold records of a metric; 
        - Changes regularly;
        - Connects to dimensions via foreign keys;
        - Decided by business use-case.
        - **Dimension tables**:
        - Holds descriptions of attributes;
        - Does not change as often.


# Database Schemas and Normalization
In this chapter, you will take your data modeling skills to the next level. You'll learn to implement star and snowflake schemas, recognize the importance of normalization and see how to normalize databases to different extents. 

Star Schema
- It is the simplest form of the dimensional model
- It's made up of two tables: fact and dimension tables
- Fact tables hold records of metrics that are described further by dimension tables

Snowflake schema (an extension)
- It has more than one dimension

What is normalization?
Normalization is a technique that divides tables into smaller tables and connects them via relationships
- A database design technique
- Divides tables into smaller tables and connects them via relationships
- Goal: reduce redundancy and increase data integrity

How to normalize data? A: Identify repreating groups of data and create new tables for them.

Normalized data, usually snowflake schema, needs more join to query a information than denormalized data.

*So why we want to normalize a database? (Advantages)*

1. Normalization saves space, denormalized databases enable data redundancy
1. Enforces data consistency: Must respect naming conventions because of referential integrity.
1. Safer updating, removing, and inserting: Less data redundancy = less records to alter
1. Easier to redesign by extending: Smaller tables are easier to extend than larger tables

Disadvantages
1. complex queries require more CPU


The Goals of normalization are to:
- Be able to characterize the level of redundancy in a relational schema
- Provide mechanisms for transforming schemas in order to remove redundancy

Normal forms (NF)
- First normal form (1NF)
    - Each record must be unique - no duplicate rows
    - Each cell must hold one value
- Second normal form (2NF)
    - Must satisfy 1NF AND
        - If PK is one column, then automatically satisfies 2NF
        - If there is a composite PK, then each non-key column must be dependent on all the keys
- Third normal form (3NF)
    - requires 2NF to satisfied
    - No transitive dependencies: non key columns can't depend on other non-key columns
- Elementary key normal form (EKNF)
- Boyce-Codd normal form (BCNF)
- Forth normal form (4NF)
- Essential tuple normal form (ETNF)
- Fifth normal form (5NF)
- Domain-key Normal form (DKNF)
- Sixth normal form (6NF)

*What is risked if we on't normalize enough?* A: Data anomalies

A database that isn't normalized enough is prone to three types of anomaly errors: 
1. update, 
1. insertion, and 
3. deletion.


# Database Views
Get ready to work with views! In this chapter, you will learn how to create and query views. On top of that, you'll master more advanced capabilities to manage them and end by identifying the difference between materialized and non-materialized views. 

In a database, a view is the result set of a stored query on the data, which the database users can query just as they would in a persistent database collection object.

Virtual table that is not part of the physical schema
- Query, not data, is stored in memory
- Data is aggregated from data in tables
- Can be queried like a regular database table
- No need to retype common queries or alter schemas

Benefits of views:
- Doesn't take up storage
- A form of access control.
    - E.g.: Hide sensitive columns and restrict what user can see
- Masks complexity of queries
    - Useful for highly normalized schemas

Granting and revoking access to a view. To give and remove user permissions, we use the SQL GRANT and REVOKE command

A user can update a view if they have the necessary privilege.

Even a view isn't a physical table, when you run an update, you are updating the tables behind the view.

**Not** all views are updatable. The conditions to an updatable view are:
1. It needs to be made up of one table
1. It can't rely on a window or aggregate function.

*The same criteria for the insertable tables*

Drop view parameters:
- RESTRICT (Default): returns an error if there are objects that depend on the view.
- CASCADE: drop the view and any object that depends on that view

```SQL
-- Create a view
CREATE VIEW view_name AS (SELECT column_name FROM table_name)

-- Viewing views
SELECT * FROM INFORMARTION_SCHEMA.views;

-- Grant privilege
GRANT UPDATE ON table_name to PUBLIC;

-- REVOKE privilege
REVOKE INSERT ON table_name FROM db_user;

-- Drop view
DROP VIEW view_name [RESTRICT | CASCADE]

-- Alter view
Alter view view_name ...
```
**Materialized views**
- Materialized views are physically materialized, in other words, materialized views stores the query results, not the query.
- Querying a materialized view means accessing the stored query results
- They are refreshed or rematerialized when prompted.

When to use materialized views
- They are great if you have queries with long execution time but that not is being updated ofeten.
- They allow data scientists and analysts to run long queries and get results very quickly.

Managing dependencies
- Materialized views often depend on other materialized views
- Creates a dependency chain when refreshing views
- Not the most efficient to refresh all views at the same time
- **Excelent Solution**: Airflow, Luigi


```SQL
-- Create MATERIALIZED VIEW
CREATE MATERIALIZED VIEW mv_name as SELECT * FROM table_name

-- refreshed/rematerialized MATERIALIZED VIEW
REFRESH MATERIALIZED VIEW mv_name
```


# Database Management
This final chapter ends with some database management-related topics. You will learn how to grant database access based on user roles, how to partition tables into smaller pieces, what to keep in mind when integrating data, and which DBMS fits your business needs best. 

Granting and revoking access to a view

**GRANT** or **REVOKE** privilege **ON** object **To** or **FROM** role

- Privileges: SELECT, INSERT, UPDATE, DELETE
- Objects: table, view, schema, etc.
- Roles: a database user or a group of database users

Database roles
- Manage database access permissions
- A batabase role is an entity that contains information that (i) Defines the role's privilges (ii) Interact with the client authentication system.
- Roles can be assigned to one or more users
- Roles are global across a database cluster installation

Benefits of roles
- Roles live on after users are deleted
- Roles can be created before user accounts
- Save DBAs time


```SQL
-- Create role
CREATE Role role_name;

```

**Data partitioning**
Split a table up into multiple smaller parts is the process of partitioning.


Why partition?
When tables grow, hundreds of gigabytes or even terabytes, queries tend to become slow.

Even when we-ve set indices correctly, these indices can become so large they don't fit into memory.

**Problem**: queries/upates become slower
**Because**: e.g. indicates don't fit memory
**Solution**: split table into smaller parts (=partitioning)

Data modeling refresher
1. Conceptual data model
2. Logical data model (*For partitioning, logical data model is the same*)
3. Physical data model (*Partitioning is part of physucal data model*)

## Vertical and Horizontal partitioning

### Vertical partitioning

For vertical partitioning, there is no specific syntax in PostgreSQL. You have to create a new table with particular columns and copy the data there. Afterward, you can drop the columns you want in the separate partition.

Vertical partitioning goes one step further and splits up a table vertically by its columns, even when it's already fully normalized. After a vertical partitioning, you could end up with two tables which can be linked through a shared key.
- Split table even when fully normalized

### Horizontal partitioning: slipt tables up over the rows.

Pros of horizontal partitioning
- Indices of heavily-used partitions fit in memory
- Move to specific medium: slower vs faster
- Used for both OLAP as OLTP

Cons
- Partitioning existing table can be a hassle
- Some constraints can not be set

**Sharding**: Distribute the partitions over several machines.