# Innovating with Data and Google Cloud
Traditionally, data analysis could take days or months, generally incomplete, and complex reports were often done by specialized teams, but Cloud technology can disrupt traditional data analysis.

Cloud tecnology allows data to be consumed, analyzed, and used at speed and scale never before possible.

Course summary:
- Module 1: define data and its role in digital transformation
- Module 2: Database, data warehouse and data lakes
- Module 3: Machine learning and Artificial Intelligence

## The Value of Data

Traditional IT infrastructures faces several limitations about data, like:
- Processing volumes and varieties of new data;
- finding cost effective solutions, e.g. setting up and maintaining data centers;
- scaling resource capacity up and down, e.g. regulating their capacity globally, especially during peak demand times throughout the year;
- accessing historical data;
- and deriving insights from historical and new data.

Businesses now have access to data like never before, internal information (e.g. organization digitized operations) and external information (e.g. benchmarking reports) and capturing and leveraging internal and external data is central to unlock business value (e.g. accurate insights and predict behavior to solve problems).

With Cloud technology, businesses can consume, store and process terabytes of data in real-time, and run queries instantly. Google Cloud offers:
- Economies of scale
- Automation
- Rapid elasticity
- Data access
- data centers across a global network, which creates resilience against data loss or service disruption.

A data map is a chart of all the data used in end-to-end business processes.
- User data: This category contains all data from customers who use or purchase your services and products.
- corporate data: This category includes data about the company such as sales patterns and operations. E.g. overall sales performance of each store, and store staffing structure.
- industry data: it is the data found outside of an individual organization that everyone in the sector needs to view or access to gain knowledge about a specific domain. E.g. trends, purchasing patterns, and publicly available research papers

Data can be categorized in two main types:
1. Structured: Can be easily stored and managed in databases, it's tabular data.
1. Unstructured: Non relational data. Two categories:
    1. Semi-structured: it contains fields, which don't have to be the same in every entity and are defined according of use. E.g.: JSON, ORC, Parquet
    1. Unstructured data is the data that doesn't naturally contain fields. E.g. video, audio; they are stored in a format called BLOB (Binary Large OBject).

Data is stored as objects (blobs) in the data lake. An object consists of the data itself, a variable amount of metadata, and a globally unique identifier.

With the right cloud tools, businesses can extract value from unstructured data by using APIs to create structure.

APIs are a set of functions that integrate different platforms, with different types of data.

Any conversation about data needs to include a reference to security, privacy, compliance, and ethics.

Personal or sensitive data about a customer or an employee need to be securely collected, encrypted when stored in the cloud, and protected from external threats. Further, only a subset of users should be granted permission to view or access the private data.

Regional or industry-specific regulations often guide data policies. GCP offers a range of solutions and best practice resources that companies can leverage.

Ethical and fair considerations are important when working with AI and machine learning.

Human bias can influence the way datasets are collected, combined and used. It's important to include strategies to remove unconsicious biases when leveraging data to build business value

Quiz Answer:
1. It is required to operate efficiently at all the time. The alternative that corroborate with this requirement is "Evaluate real-time data to predict maintenance requirements"
1.  For traditional enterprises, the key benefits of using cloud technology to unlock value from data are: process terabytes of data in real-time; query data and retrieve results instantly
1. Learner demographics, their purchases, and browsing history can be stored in the corporate data
1. Education and Years of experience are appropriate and relavant data to improve recruitment efficiency using machine learning.
1. Images and videos are example of unstrustured data.

## Data Consolidation and Analytics
In the previous module, I learned that unlocking the value of data is central to digital transformation.

It was discussed the different types of data that businesses can access, and how you can combine them to generate insights and take intelligent action.

This module will start by considering where data is now and the benefits of migrating your data to the Cloud.

Then it will define key terms related to data storage, including database, data warehouse, and data lake.

Finally, it will close the module by exploring business intelligence solutions like Looker
### Migrating data to the cloud

When the company stores data on-premises
    - It is responsible for the IT infrastructure, security, processing the data, maintaining and expading the capacity of the IT infrastructure.
    - Risk downtime, resulting in dissatisfied users.
When the company stores data on cloud
    - The company 'rent' space from Google Cloud
    - Data storage and compute power is elastic
    - Cloud provides speed to ingest and use data.

### Databases, data warehouses, and data lakes
#### *What is a database?*
A organized (relational) collection of data, generally stored in tables. Databases are built and optimized to enable ingesting large amounts of data from many different sources.

Data management priorities:
- Data integrity: 
    - Data integrity, also transactional integrity, refers to the accuracy and consistency of data stored in a database.
    - It is achieved by implementing a set of rules when a database is first designed and through ongoing error checking and validation routines as data is collected.
- Scale: transactional integrity at scale.
    - Three different types of data management systems, databases, data warehouses and data lakes. Each delivers value to businesses in different ways, enabling them to leverage data at **scale**.

The **Cloud SQL** is a fully managed relational database management service (RDBMS). 
- It offers security, availability, and durability, and **storage scales up automatically** *when enabled*.
- It is compatible with common database management systems and methodologies.

Cloud SQL is recommended for  databases that serve websites, for operational applications for e-commerce, and to feed into report and chart creation that informs BI.

The **Cloud Spanner** is another fully managed database service, and it's designed for global scale. 
- With this service, data is automatically copied across regions. This replication means that if one region goes offline, the data can still be retrieved from another region.
- It provides strong consistency, massive scalability, and enterprise-grade security.
- It is ideal for mission-critical **online transaction** processing because it's all managed
- It dramatically reduces the operational overhead needed to keep the database online and serving traffic.

With Google Cloud databases, businesses can build and deploy faster, deliver applications, and maintain portability and control their data. Cloud Storage and Cloud Spanner are databases that enable customers to manage high volume of transactional data.

#### *What is Data warehouse?*
Data warehouse is a system used for reporting and data analysis, Also:
- It is used for creating analytical reports, unlocking insights, and taking itelligent actions.
- Data warehouses can assemble data from multiple sources including databases.
- It is build to enable rapid analysis of large and multi-dimensional datasets.
- In other words, it is a central hub for all business data.
- Different types of data can be transformed and consolidated into the warehouse so that they are useful for analysis.
- It allows consolidating data that is structured and semi-structured. 
    - When combined with connector tools, DW can transform unstructured data into semi-structured data that can be used for analysis
    - Pub/Sub and DataFlow can work together to bring unstructured data into the cloud and transform it into semi-structured data.

Most data warehouse providers link storage and compute together, so customers are charged for compute capacity whether they are running a query or not.

Bigquery:
- is a fully-managed data warehouse with downtime free upgrades and maintence and seamless scaling.
- it allows to analyze petabytes of data
- It is serveless, it means that resources are automatically provisioned behind the scenes as needed to run queries. So businesses do not pay for compute power unless they are actually running a query.


#### *What is a Data lake?*
A Data lake is a repository for raw data and tend to serve many purposes, such as:
- store, process, and secure large amounts of structured, semi-structured and unstructured data.
- Hold 'back-up' data which helps businesses build resilience against unexpected harm affecting the data.
- protect against data loss

Data lakes are often made up of many different products. When determinating which product to use for the data lake, it's important to consider the nature of the data being ingested. The summary below shows the appropriate Google cloud storage products based on data type:
- **Structured**: Cloud SQL, Cloud Spanner, BigQuery
- **Semi-structured**: Cloud datastore, Cloud BigTable
- **Unstructured**: Cloud storage.

Cloud Storage is a service that enables the company to store and serve binary large object (Blob data). Some of the key benefits of Google cloud storage are :
- Any amount of data
- Low latency
- Accessible from anywhere
- Multi-regional storage
- Regional storage is ideal when an organization wants to use the data locally.


Cloud storage provides organizations with different options of storing objects.
One way to classify an organization's requirements for storage is by how often they need to access the data.

For data that will be accessed less often, cloud storage offers nearline, coldline, and archive storage classes.
1. **Nearline**: It's best for data you don't expect to access more than once per month.
1. **Coldline**: It's best for data you plan to access at most once per 90 days or quarter.
1. **Archive**: It's best for data you plan to access at most once per year.

#### Some ingest tools
**Pub/Sub** is a service for real-time ingestion of data
**Dataflow** is a service for large scale processing of data

Pub/Sub and Dataflow, can work together to bring unstructured data into the Cloud and transform it into semi-structured data.

This transformed data can then be sent directly from Dataflow to BigQuery, where it becomes immediately available for analysis.


#### BI solutions
business intelligence solutions serves data in the form of insights.

The challenge businesses often face is identifying the right business intelligence solution.


Looker is a Google Cloud business intelligence solution.
-  it's a data platform that sits on top of an analytics database and makes it simple to describe your data and define business metrics.
- Analyse, explore, create visualiations, etc.

#### Quizz Notes
1. Data integrity is achieved by implementing a set of rules when a database is first designed and through ongoing error checking and validation routines as data is collected
1. Databases efficiently ingest large amounts of real-time data, while data wharehouses rapidly analyze multi-dimensional datasets.
1. A data lake is a repository of raw data and tend to hold 'back up' data
1. The advantages for storing and managing data in the public cloud are: Elasticity and speed.
1. A solution for an organization that needs to store, do complex queries, and perform dataanalysis on large amounts of structured and semi-structured data is the Bigquery
1. Looker can be used to use it to create real-time dashboards of a large hotel chain and serve it for its customers.