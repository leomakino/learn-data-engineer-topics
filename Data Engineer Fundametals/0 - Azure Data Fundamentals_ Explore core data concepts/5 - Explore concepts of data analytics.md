supplement: something that is added to something else in order to improve it or complete it
recur: to happen many times or to happen again:

\--Describe data ingestion and processing
Data analytics is concerned with taking data and finding meaningful information and inferences from it. In a data analytics solution, you combine this data and construct a data warehouse that you can use to ask (and answer) questions about your business operations.

*Wrangling is the process by which you transform and map raw data into a more useful format for analysis. It can involve writing code to capture, filter, clean, combine, and aggregate data from many sources.

Workflow:
	Data ingestion;
	Data processing;
	Data exploration.
	
Data ingestion:
The ingestion process might also perform filtering. For example, ingestion might reject suspicious, corrupt, or duplicated data. Suspicious data might be data arriving from an unexpected source. Corrupt or duplicated data could be due to a device error, transmission failure, or tampering.

Data processing:
	Data processing takes the data in its raw form, cleans it, and converts it into a more meaningful format (tables, graphs, documents, and so on). The aim of data processing is to convert the raw data into one or more business models.
	Data processing can be complex, and may involve automated scripts, and tools such as Azure Databricks, Azure Functions, and Azure Cognitive Services to examine and reformat the data, and generate models. 
	
What is ELT and ETL?
The data processing mechanism can take two approaches to retrieving the ingested data, processing this data to transform it and generate models: ETL and ELT

ETL: The raw data is retrieved and transformed before being saved.
	Improved data privacity and compliance;
	Does not require specialist skills.
ELT: The data is stored before being transformed.
	Data lake support;
	Ideal for large volumes of data.

ETL:
	It is suitable for systems that only require simple models, with little dependency between items: basic data cleaning tasks, deduplicating data, and reformatting the contents of individual fields. 
	It can help with data privacy and compliance, removing sensitive data before it arrives in your analytical data models.
ELT:
	Is more suitable for constructing complex models that depend on multiple items in the database, often using periodic batch processing.

The more stream-oriented approach of ETL places more emphasis on throughput. 

Azure options:
	Azure SQL Database: you can use SQL Server Integration Services. Integration Services can extract and transform data from a wide variety of sources such as XML data files, flat files, and relational data sources, and then load the data into one or more destinations.
	Azure Data Factory: You can build complex ETL processes that transform data visually with data flows, or by using compute services such as Azure HDInsight Hadoop, Azure Databricks, and Azure SQL Database.
	
\--Explore data visualization
The purpose of producing data visualization is to help you reason over the information it contains, ask questions, and hopefully obtain answers that can help you drive your business forward.

Data visualization techniques to analyze and understand the information:

-Report:
Reporting is the process of organizing data into informational summaries.
Good reporting should raise questions about the business from its end users.
Reporting shows you what has happened, while analysis focuses on explaining why it happened and what you can do about it.

-Business Intelligence:
The term Business Intelligence (BI) refers to technologies, applications, and practices for the collection, integration, analysis, and presentation of business information.
Business intelligence systems provide historical, current, and predictive views of business operations, most often using data that has been gathered into a data warehouse, 
benchmarking: The process of comparison with other companies in the same industry. Variables like: Applications tackle sales, production, financial, and many other sources of business data for purposes that include business performance management.

What is data visualization?
A: Data visualization is the graphical representation of information and data. 
It's provide an accessible way to spot and understand trends, outliers, and patterns in data.
A good data visualization enables you to quickly spot trends, anomalies, and potential issues. 
The most common forms of visualizations are:
	Bar and column charts;
	Line charts;
	Matrix;
	Key influencers;
	Treemap;
	Scatter and bubble;
	Filled map.
	
\--Explore data analytics
The term data analytics is a catch-all that covers a range of activities: descriptive, diagnostic, predictive, prescriptive, and cognitive analytics. Each with its own focus and goals.

-Descriptive analytics: It's like raw data itself
Descriptive analytics helps answer questions about what has happened, based on historical data.
By developing KPIs (Key Performance Indicators), these strategies can help track the success or failure of key objectives. 
Metrics such as return on investment (ROI) are used in many industries.
Specialized metrics are developed to track performance in specific industries.

-Diagnostic analytics: use of raw data to answers questions like why
Diagnostic analytics helps answer questions about why things happened. 
 Diagnostic analytics techniques supplement more basic descriptive analytics.
 
 -Predictive analytics:
Predictive analytics helps answer questions about what will happen in the future.
Predictive analytics techniques use historical data to identify trends and determine if they're likely to recur.
Techniques include a variety of statistical and machine learning techniques such as neural networks, decision trees, and regression.
 
 -Prescriptive analytics:
Prescriptive analytics helps answer questions about what actions should be taken to achieve a goal or target. 
By using insights from predictive analytics, data-driven decisions can be made.

-Cognitive analytics:
Cognitive analytics attempts to draw inferences from existing data and patterns, derive conclusions based on existing knowledge bases, and then add these findings back into the knowledge base for future inferences--a self-learning feedback loop.
Cognitive analytics helps you to learn what might happen if circumstances change, and how you might handle these situations.
