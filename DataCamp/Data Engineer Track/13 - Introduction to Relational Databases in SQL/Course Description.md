# Course Description

You’ve already used SQL to query data from databases. But did you know that there's a lot more you can do with databases? You can model different phenomena in your data, as well as the relationships between them. This gives your data structure and consistency, which results in better data quality. In this course, you'll experience this firsthand by working with a real-life dataset that was used to investigate questionable university affiliations. Column by column, table by table, you'll get to unlock and admire the full potential of databases. You'll learn how to create tables and specify their relationships, as well as how to enforce data integrity. You'll also discover other unique features of database systems, such as constraints.

# First Database
In this chapter, you'll create your very first database with a set of simple SQL commands. Next, you'll migrate data from existing flat tables into that database. You'll also learn how meta-information about a database can be queried. 

## Introduction to relational databases

Advantages over flat files like CSVs or Excel sheets:
- real-life entities become tables: store different real-world entities in different tables;
- reduced redundancy: each table only contains data from a single entity type;
- data integrity by relationships: relationships between entities;
- use constraints, keys and referential integrity in order to assure data quality.

Query information_schema with SELECT (PostgreSQL)

information_schema:
- is a meta-database that holds information about your current database
- has multiple tables you can query with the known SELECT * FROM

```
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'table_name'
```