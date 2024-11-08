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
- ```gcloud config set compute/region ...```https://accounts.google.com/v3/signin/challenge/pwd?TL=AKOx4s35bZiOJA3tB2tKGm54b7iRmmRz2oap0MQoK0vJCOzSByEsU4KDDymA7l8A&checkConnection=youtube%3A124&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fhome%2Fdashboard%3Fproject%3Dqwiklabs-gcp-03-66d222c7800b&ddm=1&flowEntry=AddSession&flowName=GlifWebSignIn&pstMsg=1&sarp=1&service=accountsettings