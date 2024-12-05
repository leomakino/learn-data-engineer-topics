# Essential Google Cloud Infrastructure: Foundation
This course introduces platform services provided by Google Cloud with a focus on Compute Engine.

The Cloud Mobile App is another way to interact with Google Cloud.
- start, stop, and SSH into Compute Engine instances and see logs from each instance
- set up customizable graphs showing key metrics such as CPU usage, network usage, requests per second, and server errors.
- The app even offers alerts and incident management and allows you to get up-to-date billing information for your projects and get billing alerts for projects that are going over budget.
- Manage VMs and database instances
- Manage apps in the App Engine
- Manage billinghttps://accounts.google.com/AddSession/signinchooser?service=accountsettings&sarp=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fhome%2Fdashboard%3Fproject%3Dqwiklabs-gcp-04-42f7ccba5be1&ddm=1&flowName=GlifWebSignIn&flowEntry=AddSession#Email=student-04-7158ad184798@qwiklabs.net


The Google Cloud interface consists of two parts: the Cloud Console and Cloud Shell.
The Console:
- Provides a fast way to perform tasks.
- Presents options to you, instead of requiring you to know them.
- Performs behind-the-scenes validation before submitting the commands.

Cloud Shell provides:
- Detailed control
- A complete range of options and features
- A path to automation through scripting

## Interacting with Google Cloud
Commands used:
- gcloud storage cp [MY_FILE] gs://[BUCKET_NAME]
- gcloud config list
- gcloud config set project project_name
- gcloud compute regions list

### Create a persistent state in Cloud Shell
Create a subdirectory for materials used in this lab:
```mkdir infraclass```

Create a file called config in the infraclass directory:
```touch infraclass/config```

Create an environment variable
```INFRACLASS_REGION=southamerica-east1```

Append the value of your Region environment variable to the config file:
```echo INFRACLASS_REGION=$INFRACLASS_REGION >> ~/infraclass/config```

Edit the shell profile
```nano .profile```

Add the following line to the end of the file
```source infraclass/config```

Press Ctrl+O, ENTER to save the file, and then press Ctrl+X to exit nano.

Use the echo command to verify that the variable is still set
```echo $INFRACLASS_REGION```

## Virtual Networks
Networking into its fundamental components:
- projects
- networks
- subnetworks
- IP addresses
- routes
- and firewall rules
- along with network pricing.


The PoPs (points of presence) are where Google's network is connected to the rest of the internet. The network connects regions and PoPs, and is composed of a global network of fiber optic cables with several submarine cable investments.

### VPC
GCP resources can connect them to each other and isolate them from each other in a Virtual Private Cloud. You can also define fine-grained network and policies within GCP and between GCP and On-premises or other public Clouds.


Essentially:
- VPC is a comprehensive set of Google managed networking objects. 
- VPC provides IP addresses for internal and external use along with granular IP address range selections.
- Networks come in three different flavors; default, auto mode, and custom mode. 
- Subnetworks allow you to divide or segregate your environment.
- Regions in zones represents Google's datacenters
### Projects, Networks, and Subnetworks
### IP Addresses
### Princing
### Common Network Designs