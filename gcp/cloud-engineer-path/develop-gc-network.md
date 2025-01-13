# Develop your Google Cloud Network
This course teaches multiple ways to deploy and monitor applications including how to: explore IAM rols and add/remove project access, create VPC networks, deploy and monitor Compute Engine VMs, write SQL queries, deploy and monitor VMs in Compute Engine, and deploy applications using Kubernetes with multiple deployment approaches.

## Introduction to SQL for BigQuery and Cloud SQL
### Working with Cloud SQL
Cloud SQL is a fully-managed database service that makes it easy to set up, maintain, manage, and administer your relational PostgreSQL and MySQL databases in the cloud. There are two formats of data accepted by Cloud SQL: dump files (.sql) or CSV files (.csv).

Commands:
- set project ID: 
```bash
export PROJECT_ID=$(gcloud config get-value project)
gcloud config set project $PROJECT_ID`
```
- setup auth without opening up a browser `gcloud auth login --no-launch-browser`
- connect to your SQL instance: `gcloud sql connect my-demo --user=root --quiet`

## Multiple VPC Networks
In this lab, you will learn how to perform the following tasks:
- Create custom mode VPC networks with firewall rules
- Create VM instances using Compute Engine
- Explore the connectivity for VM instances across VPC networks
- Create a VM instance with multiple network interfaces


Determine the effect of having VM instances in the same zone versus having instances in the same VPC network:

External IPs:
- Same VPC has connection when ` ping -c 3 'Enter mynet-vm-2 external IP here'`
- Ping VMs in the same zone returned packed transmitted
- **This confirms public access to those instances is only controlled by the ICMP firewall rules that you established earlier.**

Internal IPs:
- Same VPC has connection when ` ping -c 3 'Enter mynet-vm-2 external IP here'`. You are able to ping the internal IP address of mynet-vm-2 because it is on the same VPC network as the source of the ping (mynet-vm-1), even though both VM instances are in separate zones, regions and continents! 
- Ping between VMs in the same zone doesn't returned packets. This should not work either as indicated by a 100% packet loss! You are unable to ping the internal IP address of managementnet-vm-1 and privatenet-vm-1 because they are in separate VPC networks from the source of the ping (mynet-vm-1), even though they are all in the same region

VPC networks are by default isolated private networking domains. However, no internal IP address communication is allowed between networks, unless you set up mechanisms such as VPC peering or VPN.

---

Create a VM instance with multiple network interfaces: Multiple network interfaces enable you to create configurations in which an instance connects directly to several VPC networks (up to 8 interfaces, depending on the instance's type). Each network interface has its own internal IP address so that the VM instance can communicate with those networks. 

## Cloud Monitoring Starting Lab

### Install the Monitoring and Logging agents
Agents collect data and then send or stream info to Cloud Monitoring in the Cloud Console.

The Cloud **Monitoring agent** is a collected-based daemon that **gathers system and application metrics from virtual machine instances** and sends them to Monitoring. By default, the Monitoring agent collects disk, CPU, network, and process metrics. Configuring the Monitoring agent allows third-party applications to get the full list of agent metrics.

In this section, you install the Cloud Logging agent to stream logs from your VM instances to Cloud Logging. It is best practice to run the Cloud Logging agent on all your VM instances.


Run the Monitoring agent install script:
1. `curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh`
1. `sudo bash add-google-cloud-ops-agent-repo.sh --also-install`
1. `sudo systemctl status google-cloud-ops-agent"*"`

### Create an uptime check
Uptime checks verify that a resource is always accessible.  create an uptime check to verify your VM is up.
1. Create Uptime Check
1. Protocol, select HTTP. *Maybe the vm need: Firewall: Allow HTTP traffic*

### Create an alerting policy
In the alerting policy is possible 
- Set the Threshold position
- Manage Notification Channels

### Create a dashboard and chart
You can display the metrics collected by Cloud Monitoring in your own charts and dashboards. 

### View logs
Cloud Monitoring and Cloud Logging are closely integrated.

Select Navigation menu > Logging > Logs Explorer.