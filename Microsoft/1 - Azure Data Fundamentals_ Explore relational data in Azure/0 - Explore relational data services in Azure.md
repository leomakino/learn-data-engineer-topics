DBMS: 
deploy: to use something or someone, especially in an effective way
# Explore relational Azure data services
IaaS is an acronym for Infrastructure-as-a-Service. Azure enables you to create a virtual infrastructure in the cloud that mirrors the way an on-premises data center might work. 

PaaS stands for Platform-as-a-service. Rather than creating a virtual infrastructure, and installing and managing the database software yourself, a PaaS solution does this for you. You specify the resources that you require (based on how large you think your databases will be, the number of users, and the performance you require), and Azure automatically creates the necessary virtual machines, networks, and other devices for you.

SaaS is short for Software-as-a-Service. SaaS services are typically specific software packages that are installed and run on virtual hardware in the cloud.

Example 	Includes
IaaS 	Azure virtual network 	Servers, storage, networking, and physical data center.
PaaS 	Azure SQL Databases 	IaaS plus database management (or other server systems), and operating systems.
SaaS 	Office 365 	PaaS plus apps.

What are Azure Data Services?
A: Azure Data Services fall into the PaaS category.

# SQL Server on Azure virtual machines
lift-and-shift refers to the way in which you can move a database dir2hectly from an on-premises server to an Azure virtual machine without requiring that you make any changes to it.
A hybrid deployment is a system where part of the operation runs on-premises, and part in the cloud. 

# Azure SQL Database Managed instance
What is Azure SQL Database?A: Azure SQL Database is a PaaS
Azure SQL Database is available with several options: 
	Single Database,
	Elastic Pool,
	Managed Instance. 

Single Database: You create and run a database server in the cloud, and you access your database through this server. Microsoft manages the server, so all you have to do is configure the database, create your tables, and populate them with your data.

Elastic Pool: It is similar to Single Database, except that by default multiple databases can share the same resources, such as memory, data storage space, and processing power through multiple-tenancy. This model is useful if you have databases with resource requirements that vary over time, and can help you to reduce costs. 

Managed Instance:  Instance-scoped programming model with high compatibility with SQL Server. Best for modernization at scale with low cost/effort.
The Single Database and Elastic Pool options restrict some of the administrative features available to SQL Server. Managed instance effectively runs a fully controllable instance of SQL Server in the cloud.
SQL Database managed instance use cases:
	system that uses features such as linked servers;
	Service Broker;
	Database Mail.

# PostgreSQL, MariaDB, MySQL
The primary reason for these services is to enable organizations running PostgreSQL, MySQL, or MariaDB to move to Azure quickly, without making wholesale changes to their applications.

Azure Database for MySQL: It is a PaaS implementation of MySQL in the Azure cloud.
Azure Database for MariaDB: It is an implementation of the MariaDB database management system adapted to run in Azure.	
Azure Database for PostgreSQL: It is an PaaS implementation of PostgreSQL in the Azure Cloud. 


