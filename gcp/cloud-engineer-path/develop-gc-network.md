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

## Managing Deployments Using Kubernetes Engine
### Depolyment object
- `kubectl explain deployment`
- see all of the fields `kubectl explain deployment --recursive`
- `kubectl explain deployment.metadata.name`

### Create a deployment
- Update the deployments/auth.yaml configuration file: `vi deployments/auth.yaml`

When you run the kubectl create command to create the auth deployment, it will make one pod that conforms to the data in the deployment manifest. This means you can scale the number of Pods by changing the number specified in the replicas field.
- create your deployment: `kubectl create -f deployments/auth.yaml`
- verify: `kubectl get deployments`, then `kubectl get replicasets`
- View the Pods that were created: `kubectl get pods`

create and expose the hello deployment
- create a service for the auth deployment: `kubectl create -f services/auth.yaml`
- `kubectl create -f deployments/hello.yaml`
- `kubectl create -f services/hello.yaml`


Scale a deployment:
The replicas field can be most easily updated using the kubectl scale command: `kubectl scale deployment hello --replicas=5`

### Rolling update
Deployments support updating images to a new version through a rolling update mechanism. When a deployment is updated with a new version, it creates a new ReplicaSet and slowly increases the number of replicas in the new ReplicaSet as it decreases the replicas in the old ReplicaSet.
- To update your deployment: `kubectl edit deployment hello`
- rollout history: `kubectl rollout history deployment/hello`
- pause the rollout: `kubectl rollout pause deployment/hello`

### Canary deployments
When you want to test a new deployment in production with a subset of your users, use a canary deployment. Canary deployments allow you to release a change to a small subset of your users to mitigate risk associated with new releases. A canary deployment consists of a separate deployment with your new version and a service that targets both your normal, stable deployment as well as your canary deployment.
- create a new canary deployment for the new version: `cat deployments/hello-canary.yaml`
- create the canary deployment: `kubectl create -f deployments/hello-canary.yaml`

what if you wanted to ensure that a user didn't get served by the canary deployment? A use case could be that the UI for an application changed, and you don't want to confuse the user. In a case like this, you want the user to "stick" to one deployment or the other. You can do this by creating a service with session affinity. This way the same user will always be served from the same version. 

### Blue-green Deployments
Rolling updates are ideal because they allow you to deploy an application slowly with minimal overhead, minimal performance impact, and minimal downtime. There are instances where it is beneficial to modify the load balancers to point to that new version only after it has been fully deployed. In this case, blue-green deployments are the way to go.

Kubernetes achieves this by creating two separate deployments; one for the old "blue" version and one for the new "green" version. Use your existing hello deployment for the "blue" version. The deployments will be accessed via a service which will act as the router. Once the new "green" version is up and running, you'll switch over to using that version by updating the service.

**A major downside of blue-green deployments is that you will need to have at least 2x the resources in your cluster necessary to host your application. Make sure you have enough resources in your cluster before deploying both versions of the application at once.**

You've had the opportunity to work more with the kubectl command-line tool, and many styles of deployment configurations set up in YAML files to launch, update, and scale your deployments.

## Challenge Lab
You need to complete the following tasks:
- Create a development VPC with three subnets manually
- Create a production VPC with three subnets manually
- Create a bastion that is connected to both VPCs
- Create a development Cloud SQL Instance and connect and prepare the WordPress environment
- Create a Kubernetes cluster in the development VPC for WordPress
- Prepare the Kubernetes cluster for the WordPress environment
- Create a WordPress deployment using the supplied configuration
- Enable monitoring of the cluster
- Provide access for an additional engineer

Standards you should follow:
- Create all resources in the region and zone, unless otherwise directed.
- Use the project VPCs.
- Naming is normally team-resource, e.g. an instance could be named kraken-webserver1.
- Allocate cost effective resource sizes. Projects are monitored and excessive resource use will result in the containing project's termination (and possibly yours), so beware. This is the guidance the monitoring team is willing to share: unless directed, use e2-medium.

