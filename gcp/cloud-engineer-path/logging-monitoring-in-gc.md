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
### Monitoring and Dashboarding Multiple projects lab
How to set up a central project for monitoring other projects, create monitoring resource groups, uptime checks, and custom dashboards.

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
