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
1. It’s an indicator of current system demand.
2. Its historical trends are used for capacity planning.
3. It’s a core measure when calculating infrastructure spend.

Sample traﬃc metrics include:
- Network I/O

saturation measures how close to capacity a system is. Saturation is important because:
1. It's an indicator of current system demand. In other words, how full the service is.
2. It focuses on the most constrained resources.
3. It’s frequently tied to degrading performance as capacity is reached.

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
