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
