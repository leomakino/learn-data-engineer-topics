# Observability in Google Cloud
This course is all about application performance management tools, including Error Reporting, Cloud Trace, and Cloud Profiler.

It tend to be more for developers who are trying to perfect or troubleshoot applications that are running in one of the Google Cloud compute products.

In this course you will learn to: 
1. Install and manage Ops Agent to collect logs for Compute Engine
1. Use Google Cloud Managed Service for Prometheus 
1. Analyze VPC Flow logs and Firewall Rules logs
1. Analyze resource utilization cost for monitoring related components within Google Cloud

## Configuring Google Cloud Services for Observability
In this module, we're going to spend a little time learning how to use Ops Agent with Compute Engine. We will also explain the benefits of using Google Cloud Managed Service for Prometheus and usage of Prometheus Query Language (or PromQL) to query Cloud Monitoring metrics.

### Introduction to Ops Agent
With Google Compute Engine instances, because the VMs are running on Google hardware, Cloud Monitoring can access some instance metrics without the agent, including CPU utilization, some disk traffic metrics, network traffic, and uptime information, but that information can be augmented by installing agents into the VM operating system.

The Ops Agent is the primary agent for collecting telemetry data from your Compute Engine instances.

Combining logging and metrics into a single agent, the Ops Agent uses Fluent Bit for logs, and the Open Telemetry Collector for metrics.

You can configure the Ops agent to monitor many third-party applications such as Apache, mySQL, Oracle database, SAP HANA, and NGINX. **The Ops Agent collects metrics inside the VM**, not at the hypervisor level.

There are other benefits of running the Ops Agent inside the VM: It monitors your VM instances without the need for any additional configuration after the installation. It helps monitor 3rd party applications.

The Ops Agent also ingests any user defined (Custom) metrics in Prometheus format.

You can install Ops Agent by using three different methods: 
1. Use the Google Cloud CLI or the Google Cloud console to install the agent on individual VMs.
1. Use an Agent Policy that installs and manages agents on your fleet of VMs.
1. Use automation tools, like Ansible, Chef, Puppet, and Terraform, to install and manage agents on your fleet of VMs.

Installing using an Agent Policy
1. install the beta component
1. enable the APIs
1. create a policy

Installing the Ops Agent on individual VMs.
1. Go to the VM instances page
1. Click the name of the VM that you want to install the agent on
1. Click the Observability tab
1. Click Install
1. Click Run in Cloud Shell. Cloud Shell opens and pastes the installation command.

### Non-VM resources
When monitoring any of the following non-virtual machine systems in Google Cloud, the Ops Agent is not required, and should not be installed:
- App Engine flex and standard
- Standard GKE nodes
- Cloud Run
- Cloud Run functions

### Cloud Operations for GKE
Monitoring options explicitly available for GKE.
1. integration with Cloud Logging and Cloud Monitoring (Free GKE metrics and control plane metrics)
1. Google Cloud Managed Service for Prometheus (Prometheus metrics).

### Google Cloud Managed Service for Prometheus
Google Cloud Managed Service for Prometheus is a fully managed service that makes it easy to collect, store, and analyze Prometheus metrics. Managed Service for Prometheus lets users collect metrics from both Kubernetes and VM environments at incredible scale without operational overhead.

Monarch is an end-to-end monitoring system with high-level data modeling, data collection, querying, alerting and data management features.

Managed Service for Prometheus splits responsibilities for data collection, query evaluation, rule and alert evaluation, and data storage into multiple components. It also supports two years of metric retention by default at no additional cost.

It also supports two years of metric retention by default at no additional cost. That includes Grafana and Cloud Monitoring.

Data collection options:
- Managed data collection
    - it eliminates the complexity of deploying, scaling, sharding, configuring, and maintaining Prometheus servers
    - **is a recommended approach for all Kubernetes environments and is especially suitable for more hands-off fully managed experience**.
- Self-deployed data collection
    - Prometheus installation managed by the user
    - **recommended for quick integration into more complex environment.**
- Ops Agent:
    - Prometheus metrics scraped and sent by the Ops Agent
    - You can configure the Ops Agent on any Compute Engine instance.
    - Using an agent simplifies VM discovery and eliminates the need to install, deploy, or configure Prometheus in VM environments.
    - **recommended to collect and send Prometheus metric data originating from Compute Engine environments**
- OpenTelemetry collection
    - Deployed in any computer or Kubernetes environment
    - it uses a single collector to collect metrics from any environment and then sends them to any compatible backend.
    - best to support cross-singal workflows

### Exposing user-defined metrics
Any metrics not defined by Google Cloud are user-defined metrics.

There are two fundamental approaches to creating custom metrics for Cloud Monitoring:
- use the OpenTelemetry protocol and Ops Agent
- use the classic Cloud Monitoring API

The OpenTelemetry Protocol (OTLP) receiver 
- is a **plugin** installed on the Ops Agent that helps collect the user-defined metrics from the application and send those metrics to Cloud Monitoring for analysis and visualization.
- To configure OTLP, you must install an Ops Agent and modify the user configuration file to include the OTLP file.
    - By default, the receiver uses the Prometheus API; the default value for the metrics_mode option is googlemanagedprometheus.
    - To receive the custom metrics from the OTLP receiver, set the OTLP receiver metrics_mode to googlecloudmonitoring.

### Monitoring a Compute Engine by using Ops Agent
#### Install and configure the Ops Agent
1. To collect logs and metrics from your Apache Web Server, install the Ops Agent by using the following command: 
```bash
curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
sudo bash add-google-cloud-ops-agent-repo.sh --also-install
```
2. Copy the following command, then paste it into the terminal:
```bash
# Configures Ops Agent to collect telemetry from the app and restart Ops Agent.

set -e

# Create a back up of the existing file so existing configurations are not lost.
sudo cp /etc/google-cloud-ops-agent/config.yaml /etc/google-cloud-ops-agent/config.yaml.bak

# Configure the Ops Agent.
sudo tee /etc/google-cloud-ops-agent/config.yaml > /dev/null << EOF
metrics:
  receivers:
    apache:
      type: apache
  service:
    pipelines:
      apache:
        receivers:
          - apache
logging:
  receivers:
    apache_access:
      type: apache_access
    apache_error:
      type: apache_error
  service:
    pipelines:
      apache:
        receivers:
          - apache_access
          - apache_error
EOF

sudo service google-cloud-ops-agent restart
sleep 60
```
The previous command creates the configuration to collect and ingest logs and metrics from the Apache Web Server.

#### Generate traffic and view metrics
To generate traffic on your Apache Web Server, run the following command: `timeout 120 bash -c -- 'while true; do curl localhost; sleep $((RANDOM % 4)) ; done'`

To view the Apache GCE Overview dashboard, do the following:
1. Monitoring service.
1. select Dashboards.
1. select the Apache Overview dashboard

## Monitoring Google Cloud Network
Learn to: Collect and analyze VPC Flow Logs, Firewall Rules Logging, load balancer logs, and Cloud NAT logs so you can see what's happening to the traffic across your network.

### VPC Flow Logs
VPC Flow Logs records a sample of network flows sent from and received by VM instances, including Google Kubernetes Engine nodes.

These logs can be used for network monitoring, traffic analysis, forensics, real-time security analysis, and expense optimization.

VPC Flow Logs introduces **no delay or performance penalty** when enabled.

You can activate or deactivate VPC Flow Logs per VPC subnet.

When enabled for a subnet, VPC Flow Logs collects data from all VM instances in that subnet.

Logs Explorer can be used to access the VPC Flow Logs. The entries will be vpc_flows below the Compute Engine section.

### Firewall rules logging
VPC firewall rules let you allow or deny connections to or from your virtual machine (VM) instances based on a configuration that you specify.

Enabled VPC firewall rules are always enforced, and protect your instances regardless of their configuration and operating system, even if they didn’t start.

Firewall Rules Logging lets you audit, verify, and analyze the effects of your firewall rules.

**By default, Firewall Rules Logging is disabled.**

*Note: Firewall Rules Logging can only record TCP and UDP connections.*. For other protocols, use Packet Mirroring.


*Caution: Firewall Rules Logging can generate a lot of data, which might have a cost implication.*

If the connectivity issue is related to a firewall, then there are two major possibilities: A firewall rule is actively blocking the incoming connections from the web servers Or Network traffic is blocked by default in most networks.

### Load balancer logs
While all the Google Cloud load balancers support Cloud Logging and Cloud Monitoring, the log type and log fields supported vary based on the type of the load balancers.

These include: Internal and external Application Load Balancers, Internal and external Network Load Balancers, and internal and external Proxy Load Balancers.

You can view request logs and export them to Cloud Storage, BigQuery, or Pub/Sub for analysis.

A single internal Application Load Balancer URL map can reference more than one backend service. You might need to enable logging for more than one backend service, depending on your configuration.

### Cloud NAT logs
Cloud NAT is the Google-managed Network Address Translation service. It lets you provision your application instances without public IP addresses, and it also lets them access the internet in a controlled and efficient manner.

There are many Cloud NAT benefits:
- VMs without external IP addresses can access destinations on the internet.
    - For example, you might have VMs that only need internet access to download updates. Cloud NAT lets you configure these VMs with an internal IP address.

Cloud NAT logging lets you log NAT TCP and UDP connections and errors.

When Cloud NAT logging is enabled, a log entry can be generated when a network connection that uses Cloud NAT is created, and/or when an egress packet is dropped because no port was available for Cloud NAT.

Cloud NAT logging might be enabled when a new Cloud NAT gateway is first created, or by editing the settings of an existing gateway.

### Packet Mirroring
Another way to monitor the network traffic flowing in and out of your Compute Engine virtual machines is to use Packet Mirroring.

Packet Mirroring clones the traffic of specific instances in your Virtual Private Cloud (VPC) network and forwards it for examination.

Packet Mirroring captures all ingress and egress traffic and packet data, such as payloads and headers.

The mirroring happens on the virtual machine (VM) instances, not on the network. Therefore, Packet Mirroring consumes additional bandwidth on the hosts.

Packet Mirroring is useful when you need to monitor and analyze your security status. It exports all traffic, not only the traffic between sampling periods.

One of the major limitations of Packet Mirroring is bandwidth consumption:
- Packet Mirroring consumes the egress bandwidth of the mirrored instances
- there is a work around: Use filters to reduce the traffic collected for mirrored instances. This filter can be used for IP address ranges, protocols, traffic directions and lot more.

Two main use cases where Packet Mirroring is useful in security and monitoring:
- Network and application monitoring
    - Network engineers can use the data from Packet Mirroring to: Maintain integrity of deployment.
    - Troubleshoot packet loss issues by analyzing protocols.
    - Troubleshoot reconnection and latency issues by analyzing real time traffic patterns.
- Security and compliance: 
    - Implement zero-trust by monitoring network traffic across and within the trust boundaries without any network re-architecture.
- Network forensics for PCI compliance:
    - Packet mirroring help capture, process and preserve forensic of different attack vectors.

### Network Intelligence Center
Network Intelligence Center gives you centralized monitoring and visibility into your network. It reduces troubleshooting time and effort and increases network security, all while improving the overall user experience.

Currently, it offers five modules:
- **Network Topology**: visualizes your Google Cloud network as a graph.
- **Connectivity Tests**: helps you to quickly diagnose connectivity issues and prevent outages.
  - Run tests to help verify the effect of configuration changes
- **Performance Dashboard**: gives you visibility into the performance of your VPC.
  - The **Latency tab** aggregates latency information based on a sample of your actual Transmission Control Protocol (TCP) VM traffic.
- **Firewall Insights**: produces metrics and insights that let you make better decisions about your firewall rules.
  -  It exposes misconfigurations, and identifies rules that could be made more strict.
- **Network Analyzer**: automatically monitors your VPC network configurations and detects misconfigurations and suboptimal configurations.
  - It provides insights on Network Topology, firewall rules, routes, configuration dependencies, and connectivity to services and applications.

Firewall Insights metrics let you analyze the way that your firewall rules are being used:
- Verify that firewall rules are being used in the intended way
- Verify that firewall rules allow or block their intended connections
- Perform live debugging of connections that are inadvertently dropped
- Discover malicious attempts to access your network

### Analyzing Network Traffic with VPC Flow Logs
In this lab, you will configure a network to record traffic to and from an Apache web server using VPC Flow Logs. You will then export the logs to BigQuery to analyze them.

Tasks:
1. Configure a custom network with VPC flow logs
  - *Note: Turning on VPC flow logs doesn't affect performance, but some systems generate a large number of logs, which can increase costs. If you click on Configure logs you'll notice that you can modify the aggregation interval and sample rate. This allows you to trade off longer interval updates for lower data volume generation which lowers logging costs.*
1. Create an Apache web server
1. Verify that network traffic is logged
1. Export the network traffic to BigQuery to further analyze the logs
1. Add VPC flow log aggregation

## Investigating application performance issues
### Error Reporting
Application Performance Management (APM) combines the monitoring and troubleshooting capabilities of Cloud Logging and Cloud Monitoring with Error Reporting, Cloud Trace, and Cloud Profiler.

Error Reporting looks through all the logs that your application and infrastructure has reported. It then counts, analyzes, and aggregates the exceptions to report them on your preferred notification channel.

Error Reporting can only analyze log entries that are stored in Cloud Logging buckets that are in the **global** region. 
**The source and destination Google Cloud projects must be the same, and customer-managed encryption keys (CMEK) must be disabled.**

Error Reporting helps you see the problems through the noise by constantly analyzing your exceptions. Problems are intelligently aggregated into meaningful groups tailored to your programming language and framework.

Error Reporting is available on desktop and in the Google Cloud app for iOS and Android.

Error Reporting can aggregate and display errors for: 
- App Engine standard environment and flexible environment,
- Cloud Run functions
- Apps Script
-  Cloud Run
- Compute Engine
- Amazon EC2
- GKE

Setting up Error Reporting 
- is simple and dependent on the language and compute environment.
- install the client library by using npm
- The easiest way to manually log errors to Error Reporting in Node.js is to import the Error Reporting library.
- You then instantiate a client to start reporting errors to Error Reporting.
- *For App Engine flexible environment and standard environment, Cloud Run, Cloud Run functions, and Apps Script, Error Reporting is automatically enabled.*
- *For GKE, add cloud-platform access scope during cluster creation.*
- *For Compute Engine, ensure the service account used has the Error Reporting Writer role.*
- *Outside Google Cloud, provide the Google Cloud project ID and service account credentials to the Error Reporting library*

### Cloud Trace
Cloud Trace is a distributed tracing system that collects latency data from your applications and displays it in the Google Cloud console. You can track how requests propagate through your application and receive detailed near-real time performance insights.

Trace continuously gathers and analyzes trace data from your project to automatically identify recent changes to the performance of your application. If Trace detects a significant shift in the latency profile of your app, you’re **automatically alerted**. It also helps with identification of **performance bottlenecks**.

The language-specific SDKs of Trace can analyze projects that run on VMs (even VMs not managed by Google Cloud). The Trace SDK is available for Java, Node.js, Ruby, and Go. 

The Trace API can be used to submit and retrieve trace data from any source.

Cloud Trace terminologies
- Tracing client: collects spans and sends them to Cloud Trace
- Trace: describes the time it takes an application to complete a single operation
- Span: describes how long it takes to perform a complete suboperation.

A trace is a collection of spans. A span describes how long it takes to perform a complete suboperation. A trace might describe how long it takes to process an incoming request from a user and return a response. A span might describe how long a particular RPC call requires.


There are two ways to send trace data to Cloud Trace: 
1. The first one is automatic tracing
1. instrumenting the application. You can do this by using Google client libraries or OpenTelemetry

Required IAM permissions: Cloud **Trace Agent role** is needed to send trace data from the application to Cloud Trace

### View application latency with Cloud Trace
Learn how to use Cloud Trace by doing the following:
- Deploy a sample application to a Google Kubernetes Engine (GKE) cluster.
- Create a trace by sending an HTTP request to the sample application.
- Use the Cloud Trace interface to view the latency information of the trace you created.

### Cloud Profiler
Attempting to measure performance in test environments usually fails to replicate the pressures on a production system. Continuous profiling of production systems is an effective way to discover where resources like CPU cycles and memory are consumed when the service operates in its working environment.

Cloud Profiler is a statistical, low-overhead profiler that continuously gathers CPU usage and memory-allocation information from your production applications.

Cloud Profiler presents the call hierarchy and resource consumption of the corresponding function in an interactive flame graph.

The profiling types available vary by language. For the metrics, you will find the following: 
- **CPU time** is the time that the CPU spends executing a block of code. *The time it was waiting or processing instructions for something else is not included.*
- **Wall time** is the time that it takes to run a block of code, including all wait time, including that for locks and thread synchronization.
- **Heap** is the amount of memory allocated in the heap of the program when the profile is collected. 
- **Allocated heap** is the total amount of memory that was allocated in the heap of the program.
- **Contention**: provides information about threads stuck waiting for other threads.
- **Threads** contains thread counts.

## Optimizing the costs for Google Cloud Observability
### Costs and pricing
Because Google Cloud Observability services are managed services, their cost is usage-based and not infrastructure-based. Although Cloud Profiler is offered at no cost, Cloud Logging, Cloud Monitoring, and Cloud Trace has associated costs.

Error Reporting supports errors sent by using Cloud Logging and incurs costs associated with this service.

Logging pricing is based on the volume of chargeable logs ingested.

Logging incurs cost when using: 
- Cloud Load Balancing logs, 
- Custom logs, 
- Error reporting costs (if your errors are ingested by Cloud Logging),
- The write operation in the Cloud Logging API, 
- Logs stored beyond 30 days will incur a retention charge for non-required buckets.

Cloud Monitoring prices are based on the:
- Volume of chargeable metrics ingested.
- Number of chargeable API calls.
- Execution of Cloud Monitoring uptime checks
- Metrics ingested by using Google Cloud Managed Service for Prometheus.
- 
Many functions of Google Cloud Observability are free:
- Cloud Profiler.
- Collecting and using the Cloud Audit Logs
- Access Transparency logs
- BigQuery Data Access logs and anything excluded from logs.


The networking logs, including VPC Flow logs, Firewall Rules Logging, and Cloud NAT, will **cost you the standard log storage fees**. If you store them in Cloud Logging, they won't cost you anything extra to generate. If you export the network telemetry logs to an external service, cost is incurred to generate logs.

Network Intelligence Center incurs costs for metrics overlaid on the network topology, Network Analyzer, and performance dashboard. Network Intelligence Center also incurs a cost for running connectivity tests and Firewall insights.

### Bill Estimation
Bill Estimation:
- Use Pricing Calculator because it is accurate, but it's only as accurate as the data that you provide it.
- Start with current usages
- You can also use the Cost Estimation API. It provides customer-specific estimates that include your discounts. E.g.: those negotiated as part of a contract and those based on committed usage

### Cost Controle Best practices
Best practices:
- Exclude logs:
  - Exclude certain logs based on high volume or the lack of pratical value
  - Common exclusions: Load balancers, VPC Flow Logs, Web Applications
- Export logs
  - Export logs yet exclude them from being ingested into Cloud Logging
  - Export logs to: Cloud Storage, BigQuery, Pub/Sub.
  - *E.g.: 2 TiBs of data access log data stored in Logging would cost about $1,000. The same 2 TiBs stored in a regional, standard class bucket would cost about $40.*
- Reduce Ops Agent usage
  - Choose not to add agents in nonessential environments
  - Reduce log volumes by not sending the additional logs generated by the Ops Agent to Cloud Logging

*Log exports are free, but not the target resource.*
*How you use labels on Monitoring custom metrics can affect the volume of time series that are generated.* Thus, where possible, limit the number of custom metric labels.

If you don't need the detailed system metrics or metrics from the third-party apps for certain VMs, reduce the volume by not sending these metrics. You can also reduce the metric volumes by reducing the number of VMs using the Ops Agent.

If you want to reduce metric volumes, you can reduce the number of custom monitoring metrics that your apps send.

In Prometheus, to reduce the number of metrics, you can do the following:
- Modify your scrape configs to scrape fewer targets.
- reduce the number of samples ingested Increasing the length of the sampling period. For example: Changing a 10-second sampling period to 30 seconds.

Trace charges are based on the number of trace spans ingested and scanned. Use sampling to reduce the volume of traces ingested. Sampling is not only a best practice for using Cloud Trace: you might reduce your span volume for cost-reduction reasons too. For example, with a popular web application with 5000 queries/second, you might gain enough insight from sampling 5% of your app traffic instead of 20%.

Controlling monitoring costs best practices:
- Optimize metrics and label usage
  - limit custom metric labels
  - Select labels thoughtfully
- Reduce Ops Agent usage
  - Consider reducing the volume of metrics by not sending detailed metrics
  - Reduce the number of VMs using Ops Agents
- Reduce custom metrics usage
  - Reduce the number of custom monitoring metrics that yout apps send