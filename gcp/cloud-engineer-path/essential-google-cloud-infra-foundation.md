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
Projects are the key organizer of infrastructure resources and it associates objects and services with billing. The default quota for each project is 15 networks, but you can simply request additional quota


These networks can be shared with other projects, or they can be peered with networks in other projects. Also, these networks do not have IP ranges but are simply a construct of all of the individual IP addresses and services within that network.

Inside a network, you can segregate your resources with **regional** subnetworks. There are different types of networks: default, auto, and custom.
- default
    - Every project is provided with a default VPC network with preset subnets and firewall rules.
    -  a subnet is allocated for each region with non-overlapping CIDR blocks and firewall rules that allow ingress traffic for ICMP, RDP, and SSH traffic from anywhere, as well as ingress traffic from within the default network for all protocols and ports.
- auto mode
    - one subnet from each region is automatically created within it.
    - the default network is actually an auto mode network. ???
    - These automatically created subnets use a set of predefined IP ranges with a /20 mask that can be expanded to /16.
    - All of these subnets fit within the 10.128.0.0/9 CIDR block.
    - as new Google Cloud regions become available, new subnets in those regions are automatically added to auto mode networks using an IP range from that block.
- custom mode
    - it does not automatically create subnets
    - This type of network provides you with **complete control** over its subnets and IP ranges: which subnets to create, in regions you choose, and using IP ranges you specify.
    - These IP ranges cannot overlap between subnets of the same network.
    - you can convert an auto mode network to a custom mode network to take advantage of the control that custom mode networks provide.
    - Google Cloud now supports IPv6 in a custom VPC network mode, for example you can configure IPv6 addressing on ‘dual-stack’ VM instances running both IPv4 and IPv6.


The subnet is simply an IP address range, and you can use IP addresses within that range. Every subnet has four reserved IP addresses in its primary IP range. The new subnet must not overlap with other subnets in the same VPC network in any region. Each IP range for all subnets in a VPC network must be a unique valid CIDR block. Also, the new subnet IP address ranges are regional internal IP addresses and have to fall within valid IP ranges.


Do not scale your subnet beyond what you actually need.

### IP Addresses
### Princing
### Common Network Designs