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
-- Lookat the columns pf a certain table
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'table_name'

-- Create new tables
CREATE TABLE table_name (
    column_a data_type,
    column_b data_type,
    column_c data_type
)

-- Add an empty column
ALTER TABLE mytable
ADD COLUMN new_column text;

-- Alter column type after table creation
ALTER TABLE table_name
ALTER COLUMN column_a
-- Type changes the data type of the column_a column in table_name to integer
TYPE integer
-- USING specifies a transformation that should happen before the type is altered
USING ROUND(column_a)

-- Add new rows to table
INSERT INTO mytable (column_a, column_b)
VALUES ("v_a", "v_b")

-- Copy data from a existing table to a new one
INSERT INTO table_name
SELECT * FROM table_2

-- Rename Column
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;

-- Drop a column
ALTER TABLE
DROP COLUMN column_name;
```

## Enforce data consistency with attribute constraints
Now it's finally time to delve into the real advantages of databases with many cool features that ultimately lead to better data consistency and quality, such as domain constraints, keys, and referential integrity.

Integrity constraints:
1. Attribute constraints: data types
1. Key constraints: primary keys
1. Referencial integrity constraints, enforced through foreign keys

Advantages of constraints:
- gives the data structure
- helps with consistency, and thus data quality
- data quality is a business advantage/ data science prerequisite

The use of the data types as attribute constraints. **[Check The PostGresql Data types](https://www.postgresql.org/docs/10/datatype.html)**.
- Enforced on columumns
- Define domain of a column
- Define what operations are possible
- Enfore consistent storage of values

The not-mull constraint
- Disallow NULL values in a certain column
- Must hold true for the current and future state
- Useful Codes: 
``` 
-- Disallow null value when creating table
Create TABLE mytable (column_1 integer not null);

-- Disallow null values after the table has been created
ALTER TABLE mytable
ALTER COLUMN column1
SET NOT NULL;

-- Remove a not-null constraint
ALTER TABLE mytable
ALTER COLUMN column1
DROP NOT NULL;

-- Adding unique constraints
Create TABLE mytable (column_1 Unique);

-- Adding unique constraints after the table has been created
ALTER TABLE mytable
ADD CONSTRAINT some_name UNIQUE(column_name);
```

NULL can mean a couple of things:
- unknown
- does not exist
- does not apply

