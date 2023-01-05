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


# Database Views
Get ready to work with views! In this chapter, you will learn how to create and query views. On top of that, you'll master more advanced capabilities to manage them and end by identifying the difference between materialized and non-materialized views. 


# Database Management
This final chapter ends with some database management-related topics. You will learn how to grant database access based on user roles, how to partition tables into smaller pieces, what to keep in mind when integrating data, and which DBMS fits your business needs best. 