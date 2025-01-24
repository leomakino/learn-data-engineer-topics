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