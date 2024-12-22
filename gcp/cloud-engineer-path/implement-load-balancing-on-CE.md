# Implement Load Balancing on Compute Engine
Demonstration skills in the following: writing gcloud commands and using Cloud Shell, creating and deploying virtual machines in Compute Engine, and configuring network and HTTP load balancers.

Skills: Cloud Computing, Networking, and Compute Engine

## Creating a Virtual Machine
In this hands-on lab, it was created VM instances of various machine types using the Google Cloud console and the gcloud command line in Cloud Shell. You also learn how to connect an NGINX web server to your VM. The tasks were: 
- Create a VM with the Cloud console.
- Create a VM with the gcloud command line.
- Deploy a web server and connect it to a VM.

Commands in this lab:
- list the active account name with this command: ```gcloud auth list```
- List the project ID: ```gcloud config list project```
- Set the project region: ```gcloud config set compute/region REGION```
- Create a variable for region: ```export REGION=REGION```
- Create a variable for zone: ```export ZONE=Zone```


In the SSH:
- Install an NGINX web server, one of the most popular web servers in the world, to connect your VM to something: ```sudo apt-get install -y nginx```
- Confirm that NGINX is running: ```ps auwx | grep nginx```


Create a new instance with gcloud ```gcloud compute instances create gcelab2 --machine-type e2-medium --zone=$ZONE ```

See all the defaults ```gcloud compute instances create --help```


You can set the default region and zones that gcloud uses if you are always working within one region/zone and you don't want to append the --zone flag every time. To do this, run these commands:
- ```gcloud config set compute/zone ...```
- ```gcloud config set compute/region ...```

## Qwik Start - Windows
See whether the server instance is ready for an RDP connection: ```gcloud compute instances get-serial-port-output [instance] --zone=us-west1-a```

Set a password for logging into the RDP: ```gcloud compute reset-windows-password [instance] --zone us-west1-a --user admin```

## Getting Started with Cloud Shell and gcloud
Resources that live in a zone are referred to as zonal resources. Virtual machine instances and persistent disks live in a zone. If you want to attach a persistent disk to a virtual machine instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address.

Commands:
- Set the region: `gcloud config set compute/region REGION`
- To view the project region setting: `gcloud config get-value compute/region`
- Set the zone to: `gcloud config set compute/zone ZONE`
- To view the project zone setting: `gcloud config get-value compute/zone`
- details about the project: `gcloud compute project-info describe --project $(gcloud config get-value project)`
- store your Project ID: `export PROJECT_ID=$(gcloud config get-value project)`
- Create a VM: `gcloud compute instances create instance_name --machine-type e2-medium --zone $ZONE`
- List the firewall rules for the project `gcloud compute firewall-rules list`
- Add a tag to the virtual machine: `gcloud compute instances add-tags instance_name --tags http-server,https-server`
- An firewall rune to allow nginx: `gcloud compute firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server`
- View the available logs on the system `gcloud logging logs list`
- View the logs that relate to compute resources `gcloud logging logs list --filter="compute"`
- Read the logs related to the resource type of gce_instance `gcloud logging read "resource.type=gce_instance" --limit 5`
- Read the logs for a specific virtual machine: `gcloud logging read "resource.type=gce_instance AND labels.instance_name='gcelab2'" --limit 1`

The gcloud tool offers simple usage guidelines that are available by adding the -h flag (for help) onto the end of any gcloud command.
- `gcloud -h`
- `gcloud config --help`
- `gcloud help config`

The results of the gcloud config --help and gcloud help config commands are equivalent. Both return long, detailed help.


Filtering command-line output:
- View the logs that relate to compute resources`gcloud compute instances list --filter="name=('instance_name')"`

You have connected to the virtual machine created earlier in the lab. Did you notice how the command prompt changed?
The prompt now says something similar to sa_107021519685252337470@gcelab2:
- The reference before the @ indicates the account being used.
- After the @ sign indicates the host machine being accessed.

## Set up Network and Application Load Balancers
In this lab, you learn how to perform the following tasks:
1. Create multiple web server instances.
1. Configure a load balancing service.
1. Send traffic to the instances
1. Create an Application Load Balancer.
1. Test traffic sent to the instances

Create VM with startup script: 
```
  gcloud compute instances create www1 \
    --zone=Zone \
    --tags=network-lb-tag \
    --machine-type=e2-small \
    --image-family=debian-11 \
    --image-project=debian-cloud \
    --metadata=startup-script='#!/bin/bash
      apt-get update
      apt-get install apache2 -y
      service apache2 restart
      echo "
<h3>Web Server: www1</h3>" | tee /var/www/html/index.html'
```

Configure the load balancing service:
1. Create a static external IP address for your load balancer `gcloud compute addresses create network-lb-ip-1 --region Region`
1. Add a legacy HTTP health check resource: `gcloud compute http-health-checks create basic-check`
1. Add a target pool in the same region as your instances. Run the following to create the target pool and use the health check, which is required for the service to function:`gcloud compute target-pools create www-pool   --region Region --http-health-check basic-check`
1. Add the instances to the pool: `gcloud compute target-pools add-instances www-pool --instances www1,www2,www3`
1. Add a forwarding rule:
```
gcloud compute forwarding-rules create www-rule \
    --region  Region \
    --ports 80 \
    --address network-lb-ip-1 \
    --target-pool www-pool
```

Application Load Balancing is implemented on Google Front End (GFE). GFEs are distributed globally and operate together using Google's global network and control plane. You can configure URL rules to route some URLs to one set of instances and route other URLs to other instances.

Requests are always routed to the instance group that is closest to the user, if that group has enough capacity and is appropriate for the request. If the closest group does not have enough capacity, the request is sent to the closest group that does have capacity.

To set up a load balancer with a Compute Engine backend, your VMs need to be in an instance group. The managed instance group provides VMs running the backend servers of an external Application Load Balancer.

Managed instance groups (MIGs) let you operate apps on multiple identical VMs. You can make your workloads scalable and highly available by taking advantage of automated MIG services, including: autoscaling, autohealing, regional (multiple zone) deployment, and automatic updating.

-  create the load balancer template
```
gcloud compute instance-templates create lb-backend-template \
   --region=Region \
   --network=default \
   --subnet=default \
   --tags=allow-health-check \
   --machine-type=e2-medium \
   --image-family=debian-11 \
   --image-project=debian-cloud \
   --metadata=startup-script='#!/bin/bash
     apt-get update
     apt-get install apache2 -y
     a2ensite default-ssl
     a2enmod ssl
     vm_hostname="$(curl -H "Metadata-Flavor:Google" \
     http://169.254.169.254/computeMetadata/v1/instance/name)"
     echo "Page served from: $vm_hostname" | \
     tee /var/www/html/index.html
     systemctl restart apache2'
```
- Create a managed instance group based on the template:
```
gcloud compute instance-groups managed create lb-backend-group \
   --template=lb-backend-template --size=2 --zone=Zone
```
- Create a backend service
```
gcloud compute backend-services create web-backend-service \
  --protocol=HTTP \
  --port-name=http \
  --health-checks=http-basic-check \
  --global
```

- Add your instance group as the backend to the backend service
```
gcloud compute backend-services add-backend web-backend-service \
  --instance-group=lb-backend-group \
  --instance-group-zone=Zone \
  --global
```
- Create a target HTTP proxy to route requests to your URL map:
```
gcloud compute target-http-proxies create http-lb-proxy \
    --url-map web-map-http
```