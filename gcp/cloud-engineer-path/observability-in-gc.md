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
