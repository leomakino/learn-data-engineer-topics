# Logging and Monitoring in Google Cloud
## Introduction to Google Cloud Operations Suite
Google Cloud operations is a suite of products to monitor, diagnose and troubleshoot infrastructure, services, and applications at scale. It incorporates capabilities to let DevOps (development operations), SREs (site reliability engineering), or ITOps (information technology operations) users operate services in a manner similar to how Google SREs operate their own services. It offers integrated capabilities for monitoring, logging, and advanced observability services like Trace and Profiler.

### Need for Google Cloud Observability
The five distinct recurring user needs for observability are:
- Visibility into system health
- Error reporting and alerting: proactive alerting, anomaly detection, or guidance on issues.
- Efficient troubleshooting: proactively correlate relevant signals and make it easy to search across different data sources, like logs and metrics.
- Improve performance

What needed from products:
- Continual improvement
- Dashboards
- Automated alerts
- Incident response

There are "Four Golden signals" that measure a system's performance and reliability:
1. Latency
1. Traffic
1. Saturation
1. Errors

**Latency** measures how long it takes a particular part of a system to return a result. Latency is important because:
1. It directly affects the user experience.
2. Changes in latency could indicate emerging issues.
3. Its values may be tied to capacity demands.
4. It can be used to measure system improvements.

How is it measured? Sample latency metrics include:
- Page load latency
- Number of requests waiting for a thread
- Query duration
- Service response time
- Transaction duration
- Time to ﬁrst response
- Time to complete data return

**Traﬃc** measures how many requests are reaching your
system. Traﬃc is important because:
1. It's an indicator of current system demand.
2. Its historical trends are used for capacity planning.
3. It's a core measure when calculating infrastructure spend.

Sample traﬃc metrics include:
- Network I/O

saturation measures how close to capacity a system is. Saturation is important because:
1. It's an indicator of current system demand. In other words, how full the service is.
2. It focuses on the most constrained resources.
3. It's frequently tied to degrading performance as capacity is reached.

Sample capacity metrics include:
- % memory utilization
- % thread pool utilization
- % cache utilization
- % disk utilization
- % CPU utilization
- Disk quota
- Memory quota
- number of available connections
- And number of users on the system

**errors** are events that measure system failures or other issues. Errors might indicate:
1. Conﬁguration or capacity issues
2. Service level objective violations
3. That it's time to emit an alert

Sample error metrics include:
- Wrong answers or incorrect content
- number 400/500 HTTP codes
- number failed requests
- number exceptions
- number stack traces
- Servers that fail liveness checks
- And # dropped connections

Observability starts with signals, which are metric, logging, and trace data captured and integrated into Google products from the hardware layer up

Google Cloud Operations Suite
- Cloud Monitoring
- Cloud Logging
- Error reporting
- Cloud Trace
- Cloud Profiler

### Cloud Monitoring
Cloud monitoring provides visibility into the performance, uptime, and overall health of cloud-powered applications. It collects metrics, events, and metadata from projects, logs, services, systems, agents, custom code, and various common application components

Cloud Monitoring Features:
- Automatic, free ingestion: On 100+ monitored resources, over 1,500 metrics are immediately available with no cost
- Open Source Standards: 
- Customization for key workloads: Cloud Monitoring offers custom visualization capabilities for GKE through Google Cloud Managed Service for Prometheus and for Google Compute Engine through Ops Agent.
- In-context visualizations & alerts: View relevant telemetry data alongside your
workloads across Google Cloud

### Cloud Logging
Cloud Logging allows users to collect, store, search, analyze, monitor, and
alert on log entries and events. Automated logging is integrated into Google Cloud
products like App Engine, Cloud Run, Compute Engine VMs running the logging agent,
and GKE.

Cloud Logging also provides massive features that makes managing and exploring
tons of logs easier. These include:
- Automatic, easy log ingestion: Immediate ingestion from GCP services
across your stack
- Gain insight quickly: Tools like Error Reporting, Log Explorer, and Log
Analytics let you quickly focus from large sets of data
- Customize routing & storage: Route your logs to the region or service of
your choice for additional compliance or business benefits
- Compliance Insights: Leverage audit and app logs for compliance patterns and issues

Export log data as files to Google Cloud Storage, or as messages through Pub/Sub, or into BigQuery tables. Pub/Sub messages can be analyzed in near-real time using custom code or stream processing technologies like Dataflow. BigQuery allows analysts to examine logging data through SQL queries. And archived log files in Cloud Storage can be analyzed with several tools and techniques. Logs-based metrics may be created and integrated into Cloud Monitoring dashboards, alerts, and service SLOs.

Default log retention in Cloud Logging depends on the log type. Data access logs are retained by default for 30 days, but this is configurable up to a max of 3650 days.
Admin logs are stored by default for 400 days. Export logs to Google Cloud Storage or BigQuery to extend retention.

### Error Reporting
Error Reporting counts, analyzes, and aggregates the crashes in your running cloud
services.

Features:
- Real time processing: Application errors are processed and displayed in the interface within seconds.
- Quickly view and understand errors: A dedicated page displays the details of the error: bar chart over time, list of affected versions, request URL and link to the request log.
- Instant notification: Do not wait for your users to report problems. Error Reporting is always watching your service and instantly alerts you when a new application error cannot be grouped with existing ones. Directly jump from a notification to the details of the new error.

### Application performance Management
**Cloud Trace**, based on the tools Google uses on its production services, is a tracingsystem that collects latency data from your distributed applications and displays it in the Google Cloud console.

Trace can capture traces from applications deployed on App Engine, Compute Engine VMs, and Google Kubernetes Engine containers.

Poorly performing code increases the latency and cost of applications and web
services every day, without anyone knowing or doing anything about it.

Cloud Proﬁler changes this by using statistical techniques and extremely low-impact
instrumentation that runs across all production application instances to provide a
complete CPU and heap picture of an application without slowing it down.

With broad platform support that includes Compute Engine VMs, App Engine, and Kubernetes, it allows developers to analyze applications running anywhere, including Google Cloud, other cloud platforms, or on-premises, with support for Java, Go, Python, and Node.js.

Cloud Proﬁler presents the call hierarchy and resource consumption of the relevant function in an interactive ﬂame graph that helps developers understand which paths consume the most resources and the different ways in which their code is actually called.

## Monitoring Critical systems
Monitoring is all about keeping track of exactly what's happening with the resources that we launched inside of Google Cloud.

Monitoring is the foundation of product reliability. It reveals what needs urgent attention and shows trends in application usage patterns, which can yield better capacity planning, and generally help improve an application client's experience, and reduce their problems.

---
### Cloud Monitoring Architecture patterns
A typical Cloud Monitoring architecture includes the following:
1. Metric Collection
    - GKE custom metrics
    - CE metrics
    - 100+ services metrics
1. Metric Storage
    - Stores the collected data and routes to the configured visualization and analysis layer.
    - this layer includes the
Cloud Monitoring API that helps triage the metrics collected to be stored for further analysis.
1. Visualization & Analysis
    - Dashboards
    - Uptime checks
    - Alert Policies
    - Notifications

System metrics from Google Cloud are available at no cost to customers. These
metrics provide information about how the service is operating. Over 1500 metrics
across more than 100 Google Cloud services automatically.

However, if customers, e.g. in traditional enterprise cohorts, are using 3Party products for monitoring and **want to aggregate their Google Cloud metrics into those partner products, they can use Cloud Monitoring APIs to ingest these metrics.**

Hybrid monitoring and logging: With Google's partner BindPlane by Blue Medora, you can import monitoring and 00000000000logging data from both on-premises VMs and other cloud providers

### Monitoring Multiple projects
When you go to monitoring settings for a project, you can see that the current metrics scope only has a single project in it, the one it is currently viewing.


### Monitoring and Dashboarding Multiple projects lab
How to set up a central project for monitoring other projects, create monitoring resource groups, uptime checks, and custom dashboards.

it's possible for one metrics scope to monitor multiple projects, and also a project can be monitored from only a single metrics scope.

the recommended approach for production deployments is to create a dedicated project to host monitoring conﬁguration data and use its metrics scope to set up monitoring for the projects that have actual resources in them.

### Data model and Dashboards
In general terms, monitoring data is recorded in time series. Each individual time series includes four pieces of information relevant to this discussion:

Cloud Monitoring Data model:
- metric: consists of metric label and metric type that describes the metric
- resource: consists of resource-label and the resource information from which the metrics are collected
- metricKind and valueType: tells you how to interpret the values
- points: are an array of timestamped values that tells you what the values of the metrics are


In general terms, monitoring data is recorded in time series. Each individual time series includes four pieces of information relevant to this discussion:
- The metric field describes the metric itself and records two aspects:
    - The metric-label that represents one combination of label values.
    - The metric type specifies the available labels and describes what is represented by the data points.
- The resource field records:
    - The resource-label represents one combination of label values.
    - The specific monitored resource from which the data was collected.
- The metricKind and valueType fields tell you how to interpret the values. The value type is the data type for the measurements. Each time series records the value type (type ValueType) for its data points.
    - For measurements consisting of a single value at a time, the value type tells you how the data is stored:
        - BOOL, a boolean
        - INT64, a 64-bit integer
        - DOUBLE, a double-precision float
        - STRING, a string
    - For distribution measurements, the value isn't a single value but a
    - group of values. The value type for distribution measurements is DISTRIBUTION.
- Each time series includes the metric kind (type MetricKind) for its data points.
The kind of metric data tells you how to interpret the values relative to each other. Cloud Monitoring metrics are one of three kinds:
    - A gauge metric, in which the value measures a specific instant in time.
For example, metrics measuring CPU utilization are gauge metrics;
each point records the CPU utilization at the time of measurement.
    - A delta metric, in which the value measures the change in a time
interval. For example, metrics measuring request counts are delta
metrics; each value records how many requests were received after
the start time, up to and including the end time.
    - A cumulative metric, in which the value constantly increases over time. For example, a metric for “sent bytes” might be cumulative; each value records the total number of bytes sent by a service at that time.
- The points field is an array of timestamped values. The metric type tells you what the values represent. The sample time series has an array with a single data point; in most time series, the array has many more values.

Dashboards are a way for you to view and analyze metric data that is important to you. They give you graphical representations on the main signal data in such a way as to help you make key decisions about your Google Cloud-based resources.

You can also use the Dashboard Builder to visualize application metrics that you are interested in. You can select the chart type and filter the metrics based on your requirements.

**Metrics Explorer** lets you build charts for any metric collected by your project. With it, you can:
- Save charts you create to a custom dashboard.
- Share charts by their URL.
- View the configuration for charts as JSON.

Most importantly, you can use Metrics Explorer as a tool to explore data that you don't need to display long term on a custom dashboard.

You define a chart by specifying both what data should display and how the chart should display it:
1. **Metric**
1. **Filter**: To reduce the amount of data returned for a metric
1. **Group by**: reduce the amount of data returned for a metric by
combining different time series. Grouping is done by label values.
1. **Alignment**: creates a new time series in which the raw data has been regularized in time so it can be combined with other aligned time series. Alignment produces time series with regularly spaced data.

Alignment is a prerequisite to aggregation across time series, and monitoring does it automatically, by using default values. You can override these defaults by using the alignment options, which are the Alignment function and the Min alignment period.

- The min alignment period determines the length of time for subdividing the time series. For example, you can break a time series into one-minute chunks or one-hour chunks. The default alignment period, which is also the minimum, is one minute.
- The alignment function determines how to summarize the data in each alignment period. The functions include the sum, the mean, and so forth.

A chart's widget type and its analysis mode setting determine how the chart displays data. There are three analysis modes:
- Standard mode displays each time series with a unique color.
- Stats mode displays common statistical measures for the data in a  chart.
- X-Ray mode displays each time series with a translucent gray color. Each line is faint, and where lines overlap or cross, the points appear brighter. Therefore, this mode is most useful on charts with many lines. Overlapping lines create bands of brightness, which indicate the normal behavior within a metrics group.

**Threshold line**: The Threshold option creates a horizontal line from a point on the Y-axis. The line provides a visual reference for the chosen threshold value. You can add a threshold that refers to a value on the left Y-axis or the right Y-axis.

Compare to past: When you use Compare to Past mode on a chart, the legend is modiﬁed to include a second “values” column. The current Value column becomes Today, and the past values column is named appropriately—for example, Last Week.

### Query metrics
a more versatile way of interacting with metrics by leveraging the query languages such as Monitoring Query Language (MQL) and PromQLA.

Query metrics by using MQL and PromQL:
- MQL: is an advanced query language. It provides an expressive, text-based interface to Cloud Monitoring time-series data. By using MQL, you can retrieve, filter, and manipulate time-series data.
- PromQL provides an alternative to the Metrics Explorer menu-driven and Monitoring Query Language (MQL) interfaces for creating charts and dashboards.

You can use PromQL to query and chart Cloud Monitoring data from the following sources:
- Google Cloud services
- User-defined metrics, like log-based metrics and Cloud Monitoring user-defined metrics.
- Google Cloud Managed Service for Prometheus

You can also use tools like Grafana to chart metric data ingested into Cloud Monitoring. Available metrics include metrics from Managed Service for Prometheus and Cloud Monitoring metrics documented in the lists of metrics.

Why use MQL? **Whether you need to perform joins, display arbitrary percentages, or even make advanced calculations, the use cases for MQL are unlimited.**
- Create ratio-based charts and alerts
- Perform time-shift analysis (compare metric data week over week, month over month, year over year, etc.)
- Apply mathematical, logical, table operations, and other functions to metrics
- Fetch, join, and aggregate over multiple metrics
- Select by arbitrary, rather than predefined, percentile values
- Create new labels to aggregate data by, using arbitrary string  manipulations including regular expressions

### Uptime checks
Uptime checks can be configured to test the availability of your public services from locations around the world, as you can see on this slide. The type of uptime check can be set to HTTP, HTTPS, or TCP.

For each uptime check, you can create an alerting policy and view the latency of each global location.

Uptime checks can help us ensure that our externally facing services are running and that we aren't burning our error budgets unnecessarily.


#### Create a metrics scope and link the two worker projects into it.
There are a number of ways you might want to configure the relationship between the host project doing the monitoring, and the project or projects being monitored.

In general, if you're going for the multiple projects being centrally monitored approach, then it's recommended that the monitoring project contains nothing but monitoring related resources and configurations. 

#### Create and configure Monitoring groups
Cloud Monitoring lets you monitor a set of resources together as a single group. Groups can then be linked to alerting policies, dashboards, etc. Each metrics scope can support up to five-hundred groups and up to six layers of sub-groups. Groups can be created using a variety of criteria, including labels, regions, and applications.

In this task, you:
- Assign labels to the web servers to make them easier to track.
- Create a resource group and place the servers into it.
- Create a sub-group just for frontend dev servers

#### Create and test an uptime check
Google Cloud uptime checks test the liveliness of externally facing HTTP, HTTPS, or TCP applications by accessing said applications from multiple locations around the world. The subsequent report includes information on uptime, latency, and status. Uptime checks can also be used in alerting policies and dashboards.

In this task, you:
- Create an uptime check for the Frontend Servers group.
- Investigate out how an uptime check handles failure.

Note: If a Monitoring group is created based on labels, then the group will keep checking for powered off server for 5 minutes. After 5 minutes, Google Cloud determines the server should no longer be counted as a member of the group.

This is important because if an uptime check is tied to the group, then it will only report failures while the group reports that missing server.

When the group quits reporting the off server, the uptime check quits checking for it, and suddenly the check starts passing again. This can be a real issue if you're not careful. 

## Alerting Policies
### SLI, SLO and SLA
SLIs, are carefully selected monitoring metrics that measure one aspect of a service's reliability. Ideally, SLIs should have a close linear relationship with your users' experience of that reliability, and we recommend expressing them as the ratio of two numbers: the number of good events divided by the count of all valid events.

SLO, combines a service level indicator with a target reliability and will generally be somewhere just short of 100%. you should choose SLOs that are **S.M.A.R.T.**

SLAs, which are commitments made to your customers that your systems and applications will have only a certain amount of “down time.”

### Developing an alerting strategy
Goal: Person is notified when needed
- A service is down
- SLOs or SLAs are heading toward not being met.
- Something needs to change.

An alert is an automated notification sent by Google Cloud through some notification channel to an external application, ticketing system, or person.

Error budget = Perfetion - SLO. E.g.: If the SLO is: “90% of requests must return in 200 ms,” then the error budget is: 100% - 90% = 10%

Evaluating alerts:
- Precision: 
    - Relevant alerts = Relevant alerts + irrelevant alerts
    - It’s decreased by false alerts
- Recall: 
    - Relevant alerts = Relevant alerts + missed alerts
    - Recall is adversely affected by missed alerts. It’s decreased by missing alerts.
- Detection time: 
    - How long it takes the system to notice an alert condition
    - Long detection times can negatively affect the error budget
    - Raising alerts too fast may result in poor precision
- Reset time: 
    - How long alerts fire after an issue is resolved
    - Continued alerts on repaired systems can lead to confusion

Precision can be seen as a measure of exactness, whereas recall is a measure of completeness.

---
Alert window lengths (per week, per month, per year)

The window is a regular-length subdivision of the SLO total time:
- Smaller windows tend to yield faster alert detections and shorter reset times, but they also tend to decrease precision because of their tendency toward false positives.
- Longer windows tend to yield better precision, because they have longer to confirm that an error is really occurring. But reset and detection times are also longer. That means you spend more error budget before the alert triggers.

One trick might be to use short windows, but add a successive failure count. One window failing won’t trigger the alert, but when three fail in a row the error is triggered. This way, the error is spotted quickly but treated as an anomaly until the duration or error count is reached. The rule: An error is spotted quickly but treated as an anomaly until three windows fail in a row.

Many variables can affect a good alerting strategy:
- Amount of traffic
- Error budget
- Peak and slow periods
You can define multiple conditions in an alerting policy to try to get better precision, recall, detection time, and rest time.

Alerts should always be prioritized based on customer impact and SLA. Don't involve humans unless the alert meets some threshold for criticality. severity levels are an important concept in alerting to aid you and your team in properly assessing which notifications should be prioritized.

You can create custom severity levels on your alert policies and have this data included in your notifications for more effective alerting and integration with downstream third-party services (for example, Webhook, Cloud Pub/Sub, PagerDuty).

Low-priority alerts might be logged, sent through email, or inserted into a support ticket management system.

### Creating Alerts
An alerting policy has:
- A name
- One or more alert conditions
- Notifications
- Documentation

The alerting policies are of two types:
- Metric based alerting
    - Used to track metric data collected by Cloud Monitoring
    - Add a metric-based alerting policy by starting from the Alerts page of Cloud Monitoring.
    - Example: Notify when the application that runs on a VM has high latency for a significant time period.
- Log based alerting
    - Used to notify anytime a specific message occurs in a log,
    - Add a log-based alerting policy by using the Logs Explorer in Cloud Logging or under Cloud Monitoring
    - Example: Notify when a human user accesses the security key of a service account

There are three types of conditions for **metric-based alerts**:
- Metric-threshold conditions trigger when the values of a metric are more than, or less than, a threshold for a specific duration window.
- Metric-absence conditions trigger when there is an absence of measurements for a duration window.
- Forecast conditions predict the future behavior of the measurements by using previous data. These conditions trigger when there is a prediction that a time series will violate the threshold within a forecast window

The documentation option is designed to give the alert recipient additional information they might find helpful.

Each incident is in one of three **states**:
- Incidents firing: If an incident is open, the alerting policy's set of conditions is being met. Or there’s no data to indicate that the condition is no longer met. Open incidents usually indicate a new or unhandled alert.
- Acknowledged incidents: A technician spots a new open alert. Before one starts to investigate, they mark it as acknowledged as a signal to others that someone is dealing with the issue.
- Alert policies: displays the number of alerting policies created.

Snooze displays the recently configured snoozes. When you want to temporarily prevent alerts from being created and notifications from being sent, or to prevent repeated notifications from being sent for an open incident, you create a snooze.

Groups provide a mechanism for alerting on the behavior of a set of resources instead of individual resources.

You define the one-to-many membership criteria for your groups. Criteria can include:
- Cloud Projects
- Resource name
- Resource type
- Tags and labels
- Security groups
- Regions
- App Engine apps and services

**Logs-based metrics** are extracted from Cloud Monitoring and are based on the content of log entries.

### Alerting in Google Cloud Lab
The Alerting CLI (and API) can be very effective when applying alerting policies with code or scripts.

Every project needs to first create an App Engine application before it can be used. This is done just once per project using the console, or the gcloud app create command.

### Service Monitoring
Modern applications are composed of multiple services connected together, and when something fails, it often seems like many things fail at the same time. To help manage this complexity, SLO monitoring helps with SLO and alert creation.

With Service Monitoring, you get the answers to the following questions:
- What are your services? What functionality do those services expose to internal and external customers?
- What are your promises and commitments regarding the availability and performance of those services, and are your services meeting them?
- For microservices-based apps, what are the inter-service dependencies? How can you use that knowledge to double check new code rollouts and triage problems if a service degradation occurs?
- Can you look at all the monitoring signals for a service holistically to reduce mean time to repair (MTTR)?

Service Monitoring can approach SLO compliance calculations in two fundamental ways:
1. Request-based SLOs: use a ratio of good requests to total requests
1. Window-based SLOs: use a ratio of the number of good versus bad measurement intervals, or windows.

Service Monitoring makes SLO creation easy.

## Advanced Logging and Analysis
### Cloud Logging overview and architecture
Cloud Logging allows you to store, search, analyze, monitor, and alert on log data and events from Google Cloud.

Logs is one of the top most visited sections in Google Cloud console and one of most transitional, which indicated that it is an important component of many scenarios.

Cloud Logging helps to:
- Gather data from various workloads: to troubleshoot and understand the workload and application needs
- Analyze large volumes of data: Tools like Error Reporting, Log Explorer, and Log Analytics let you focus from large sets of data
- Route and store logs: 
- Get Compliance Insights: Leverage audit and app logs for compliance patterns and issues.

Cloud Logging architecture consists of the following components:
- Log Collections: These are the places where log data originates. Log sources can be Google Cloud services, such as Compute Engine, App Engine, and Kubernetes Engine, or your own applications.
- The Log Router is responsible for routing log data to its destination. The Log Router uses a combination of inclusion filters and exclusion filters to determine which log data is routed to each destination.
- Log sinks are destinations where log data is stored. Cloud Logging
supports a variety of log sinks, including:
    - Cloud Logging log buckets
    - Cloud Pub/Sub topics
    - BigQuery
    - Cloud Storage buckets
- Log Analysis: Cloud Logging provides several tools to analyze logs.
    - Logs Explorer
    - Error Reporting
    - Logs-based metrics
    - Log Analytics

### Log types and collection
Available Logs:
- Platform logs: are logs written by Google Cloud services
- Component logs: are similar to platform logs, but they are generated by Google-provided software components that run on your systems.
- Security logs: help you answer "who did what, where, and when."
    - Cloud Audit Logs provide information about administrative activities
    - Access Transparency provides you with logs of actions taken by Google staff when accessing your Google Cloud content
- User-written logs: are logs written by custom applications and services. Typically,these logs are written to Cloud Logging by using one of the following methods:
    - Ops Agent
    - Cloud Logging API
    - Cloud Logging client libraries
- Multi-cloud logs and Hybrid-cloud logs: These refer to logs from other cloud providers like Microsoft Azure and logs from on-premises infrastructure.

### Storing, routing, and exporting the logs
Cloud Logging is actually a collection of components exposed through a centralized logging API.
1. log router: Entries are passed through the API and fed to Log Router. Log Router is optimized for processing streaming data, reliably buffering it, and sending it to any combination of log storage and sink (export) locations.
1. Log sinks run in parallel with the default log flow and might be used to direct entries to external locations.
1. Log storage: Locations might include additional Cloud Logging buckets, Cloud Storage, BigQuery, Pub/Sub, or external projects.

*Inclusion and exclusion filters can control exactly which logging entries end up at a particular destination, and which are ignored completely.*

*Cloud Storage buckets are different storage entities than Cloud Logging buckets.*

For each Google Cloud project, Logging automatically creates two logs buckets: **_Required and _Default**, and corresponding log sinks with the same names. All logs generated in the project are stored in one of these two locations:
- _Required: This bucket holds Admin Activity audit logs, System Event audit logs, and Access Transparency logs, and retains them for 400 days. You aren't charged for the logs stored in _Required, and the retention period of the logs stored here cannot be modified. You cannot delete or modify this bucket.
- _Default:  This bucket holds all other ingested logs in a Google Cloud project, except for the logs held in the _Required bucket. Standard Cloud Logging pricing applies to these logs.

Log Router sinks can be used to forward copies of some or all of your log entries to non-default locations. There are several sink locations, depending on need:
- Cloud Logging bucket works well to help pre-separate log entries into a distinct log storage bucket.
- BigQuery dataset allows the SQL query power of BigQuery to be brought to bear on large and complex log entries.
- Cloud Storage bucket is a simple external Cloud Storage location, perhaps for long-term storage or processing with other systems.
- Pub/Sub topic can export log entries to message handling third-party applications or systems created with code and running somewhere like Dataflow or Cloud Functions.
- Splunk is used to integrate logs into existing Splunk-based system.
- The Other project option is useful to help control access to a subset of log
entries.

The process for creating log sinks involves writing a query that selects the log entries you want to export in Logs Explorer, and choosing a destination of Cloud Storage, BigQuery, or Pub/Sub. The query and destination are held in an object called a sink.

Some possible log export processing options:
- Log archiving and analysis: s
    - Events -> Logging -> Pub/Sub -> Dataflow -> BigQuery
    - excellent option if you're looking for real-time log processing at scale.
    - react to real-time issues, while streaming the logs into BigQuery for longer-term analysis.
- Archive logs for long-term storage
    -  Events -> Logging -> Cloud Storage
    - long-term retention, reduced storage costs, and configurable object lifecycles
- Exporting back to Splunk
    - Events -> Logging -> Pub/Sub -> Splunk
    - Integrate the logging data from Google Cloud, back into an third-party System Information.

A common logging need is centralized **log aggregation** for auditing, retention, or non-repudiation purposes. **Aggregated sinks allow for easy exporting of logging entries without a one-to-one setup.** There are three available Google Cloud Logging aggregation levels:
- Project
- Folder
- Organization

By performing security analytics, you help your organization prevent, detect, and respond to threats like malware, phishing, ransomware, and poorly configured assets. One of the steps in security log analytics workflow is to create aggregate sinks and
route those logs to a single destination depending on the choice of security analytics tool, such as Log Analytics, BigQuery, Chronicle, or a third-party security information and event management (SIEM) technology.

### Query and view logs
The Logs Explorer interface lets you retrieve logs, parse and analyze log data, and refine your query parameters. The Logs Explorer contains the following panes:
1. Action toolbar: to refine logs to projects or storage views, share a link and learn about logs explorer.
1. Query pane: Query pane is where you can build queries, view recently viewed and saved queries and a lot more.
1. Results Toolbar: This can be used to quickly show or hide logs and histogram pane and create a log based metric or alert
1. Query results: Is the details of results with a summary and timestamp that helps troubleshoot further
1. Log fields: is used to filter your options based on various factors such as a resource type, log name, project ID, etc
1. Histogram: s where the query result is visualized a histogram bars, where each bar is a time range and is color coded based on severity.

Queries may be created directly with the Logging Query Language (LQL), using the drop-down menus, the logs field explorer, or by clicking fields in the results themselves. The query builder drop-down menu makes it easy to start narrowing your log choices:
- Resource: Lets you specify resource.type. Entries use the logical operator AND.
- Log name: Lets you specify logName. When selecting multiple entries, the logical operator OR is used.
- Severity: Lets you specify severity. When selecting multiple entries, the logical operator OR is used.

Comparison operators to filter queries: [FIELD_NAME] [OPERATOR] [VALUE]. Operators:
| **Operator** | **Description**          | **Example**                                         |
|-----------------|--------------------------|-----------------------------------------------------|
| =               | Equals                   | resource.type="gce_instance"                        |
| !=              | does not equal           | resource.labels.instance_id!="1234567890"           |
| > < >= <=       | numeric ordering         | timestamp <= "2018-08-13T20:00:00Z"                 |
| :               | has                      | textPayload:"GET /check"                            |
| :*              | presence                 | jsonPayload.error:*                                 |
| =~              | search for a pattern     | jsonPayload.message =~ "regular expression pattern" |
| !~              | search not for a pattern | jsonPayload.message !~ "regular expression pattern" |

The colon operation helps check if a value exists. This is useful when you want to match a substring within a log entry field. To test if a missing or defaulted field exists without testing for a particular value in the field, use the :* comparison

Boolean operators:
- AND
- NOT
- OR
*The NOT operator has the highest precedence, followed by OR and AND in that order*

The recipe for finding entries:
- When you’re trying to find log entries, start with what you know: the log filename, resource name, even a bit of the contents of the logged message might work.
- Full text searches are slow, but they may be effective
- Use indexed SEARCH function for complete text matches, because they perform a case-insensitive match SEARCH(textPayload, "hello world")
- If possible, restrict text searches to an log field

Some tips on finding log entries quickly:
- Search for specific values of indexed fields
- Apply constraints on resource.type and resource.labels field
    - resource.type = "gke_cluster" resource.labels.namespace = "my-cool-namespace"
- Be specific on which logs you’re searching
    - logName="projects/benkelly-test/logs/apache-access"
- Limit the time range that you’re searching
    - timestamp >= “2018-08-08T10:00:00Z” AND timestamp <= “2018-08-08T10:10:00Z”

### Logs-based metrics
Logs-based metrics derive metric data from the content of log entries. There are two types of log-based metrics:
- System-defined log-based metrics: are calculated only from logs that have been ingested by Logging. If a log has been explicitly excluded from ingestion by Cloud Logging, it isn't included in these metrics.
- User-defined log-based metrics: created by you to track things in your Google Cloud project that are of particular interest to you.

Logs-based metrics are suitable in different cases: 
- **Count the occurrences** of a message, like a warning or error, in your logs and receive a notiﬁcation when the number of occurrences crosses a threshold.
- **Observe trends in your data**: like latency values in your logs, and receive a notiﬁcation if the values change in an unacceptable way.
- **Visualize extracted data**: Create charts to display the numeric data extracted from your logs

Key access control roles:
- Logs Configuration Writer: can list, create, get, update, and delete log-based metrics.
- Logs Viewers can view existing metrics
- Monitoring Viewers can read the time series in log-based metrics.
- Logging Admins, Editors, and Owners are all broad-level roles that can create log-based metrics.

Log-based metric types:
1. Counter metrics: count the number of log entries matching an advanced logs query.
1. Distribution metrics: record the statistical distribution of the extracted log values in
histogram buckets. Their
distribution across the configured buckets is recorded, along with the count, mean,
and sum of squared deviations of the values.
1. Boolean metrics: record where a log entry matches a specified filter


Labels and logs:
- Like many cloud resources, labels can be applied to log-based metrics. Their prime use is to help with group-by and filtering tasks in Cloud Monitoring.
- Two types of labels applied:
    - Default
    - User-defined
- User-defined labels can be either of the following:
    - The entire contents of a named field in the LogEntry object.
    - A part of a named field that matches a regular expression.
- You can create up to ten user-defined labels per metric.
- A label cannot be deleted once created.

### Log Analytics
Log Analytics gives you the analytical power of BigQuery within the Cloud Logging console and provides you with a new user interface that's optimized for analyzing your logs.

When you create a bucket and activate analytics on it, Cloud Logging makes the logs data available in both the new Log Analytics interface and BigQuery; you don't have to route and manage a separate copy of the data in BigQuery. You can still query and examine the data as usual in Cloud Logging with the Logging query language.

Use cases:
- Logs Explorer: Troubleshooting
    - Get to the root cause with search, filtering, histogram and suggested searches.
- Log Analytics
    - Analyze application performance, data access and network access patterns.
- Log Analytics pipeline maps logs to BigQuery tables (JSON, STRING, INT64, RECORD, etc..) and writes to BigQuery. Use the same logs data in Log Analytics directly from BigQuery to report on aggregated application and business data found in logs.


How different is analytics-enabled bucket log data from logs routed to BigQuery?
- Log data in BigQuery is managed by Cloud Logging.
- BigQuery ingestion and storage costs are included in your Logging costs.
- Data residency and lifecycle are managed by Cloud Logging.

Log Analytics is useful in multiple aspects:
- DevOps: quickly troubleshoot an issue. Log Analytics includes capabilities to count the top requests grouped by response type and severity, which allows engineers to diagnose the issues.
- Security: finding all the audit logs. Log Analytics help better investigate the security -related attacks with queries over large volumes of security data.
- IT/Network Operations: identifying network issues. Log Analytics in this case provides better network insights and management through advanced log aggregation capabilities.