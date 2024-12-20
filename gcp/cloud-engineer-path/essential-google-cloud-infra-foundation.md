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

#### Expand a subnet
E.g.: A slash 29 mask provides you with eight addresses. But of those, four are reserved by GCP, which leaves you with another four for your VM instances.

If I create 4 VMs intances, when I try to create the fifth I receive a message telling that the IP space of that subnet has been exhausted.

To expand the subnet, I could go to VPC networks through the navigation menu. Click the "Edit" button on subnet. Expand the ip range to a slash 23, and this is going to allow a lot of instances, actually over 500 instances.

That's how easy it is to expand a subnet in GCP without any workload shutdown or downtime

### IP Addresses
In Google Cloud, each virtual machine can have two IP addresses assigned:
1. An internal IP address, which is going to be assigned via DHCP internally;
1. An external IP address, but this one is optional.


Every VM that starts up and any service that depends on virtual machines gets an internal IP address. When you create a VM in Google Cloud, its symbolic name is registered with an internal DNS service that translates the name to an internal IP address.


The external IP address can be:
1. assigned from a pool, making it ephemeral (meaning: lasting for only a short time), or 
1. it can be assigned from a reserved external IP address, making it static.

Primary internal Ipv4 address:
- Ephemeral (Automatic)
- Ephemeral (Custom)
- Reserve static internal IPV4 ADDRESS

If you reserve static external IP address and do not assign it to a resource, such as a VM instance or a forwarding rule, you are charged at a higher rate than for static and ephemeral external IP addresses that are in use.

#### Mapping IP Addresses
Regardless of whether you use an ephemeral or static IP address, the external address is unknown to the OS of the VM. The external IP address is mapped to the VM's internal address transparently by VPC. Running ifconfig within a VM in Google Cloud only returns the internal IP address.

Let’s explore this further by looking at DNS resolution for both internal and external addresses.

Google Cloud has two types of internal DNS names, Zonal and Global (project wide) DNS. In general, Google strongly recommends using zonal DNS because it offers higher reliability guarantees by isolating failures in the DNS registration to individual zones.

Each instance has a hostname that can be resolved to an internal IP address. This hostname is the same as the instance name. There is also an internal fully qualified domain name, or FQDN, for an instance that uses the format [hostnamke].[zone].c.[project-id].internal.

The DNS name always points to a specific instance, no matter what the internal IP address is. Each instance has a metadata server that also acts as a DNS resolver for that instance. The metadata server handles all DNS queries for local network resources and routes all other queries to Google's public DNS servers for public name resolution.

An instance is not aware of any external IP address assigned to it. Instead, the network stores a lookup table that matches external IP addresses with the internal IP addresses of the relevant instances.

Public DNS records pointing to instances are not published automatically; however, admins can publish these using existing DNS servers. Domain name servers can be hosted on Google Cloud, using Cloud DNS. 

**Cloud DNS** uses Google’s global network of Anycast name servers to serve your DNS zones from redundant locations around the world, providing lower latency and high availability for your users. Google Cloud offers a 100% uptime Service Level Agreement, or SLA, for domains configured in Cloud DNS. Cloud DNS lets you create and update millions of DNS records without the burden of managing your own DNS servers and software.

Another networking feature of Google Cloud is **Alias IP Ranges**. It lets you assign a range of internal IP addresses as an alias to a virtual machine's network interface. *This is useful if you have multiple services running on a VM, and you want to assign a different IP address to each service*. In other words, you can configure multiple IP addresses, representing containers or applications hosted in a VM, without having to define a separate network interface.

#### IP Addresses for Default Domains
Google publishes the complete list of IP ranges that it announces to the internet in goog.json. Useful links:
- https://www.gstatic.com/ipranges/cloud.json provides a JSON representation of Cloud IP addresses organized by region.
- https://www.gstatic.com/ipranges/cloud_geofeed is a standard geofeed formatted IP geolocation file that we share with 3rd-party IP geo providers like Maxmind, Neustar, and IP2Location.
- https://www.gstatic.com/ipranges/goog.json and https://www.gstatic.com/ipranges/goog.txt are JSON and TXT formatted files
respectively that include Google public prefixes in CIDR notation.

For more information as well as an example of how to use this information, refer to https://cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults

#### Routes and firewall rules
By default, every network has routes that let instances in a network send traffic directly to each other, even across subnets. In addition, every network has a default route that directs packets to destinations that are outside the network. Although these routes cover most of your normal routing needs, you can also create special routes that overwrite these routes.

Just creating a route does not ensure that your packet will be received by the specified next top. **Firewall** rules must also allow the packet.

The default network has pre-configured firewall rules that allow all instances in the network to talk with each other. Manually created networks do not have such rules, so you must create them.

Routes map traffic to destination networks. It matches packets by destination IP addresses. No traffic will flow without also matching a firewall rule.

Each route in the Routes collection may apply to one or more instances. A route applies to an instance if the network and instance tags match. If the network matches and there are no instance tags specified, the route applies to all instances in that network.

**GCP firewall rules** protect your virtual machine instances from unapproved connections, both inbound and outbound, known as ingress and egress, respectively.

Every VPC network functions as a distributed firewall. Although firewall rules are applied to the network as a whole, connections are allowed or denied at the instance level.

Firewall rules allow bidirectional communication once a session is established. if for some reason, all firewall rules in a network are deleted, there is still an implied "Deny all" ingress rule and an implied "Allow all" egress rule for the network.

A firewall rule is composed of the following parameters:
- The direction of the rule
     - Inbound connections are matched against ingress rules only
     - outbound connections are matched against egress rules only.
- The source of the connection for ingress packets, or the destination of the connection for egress packets.
- The protocol and port of the connection
    - where any rule can be restricted to apply to specific protocols only or specific combinations of protocols and ports only.
- The action of the rule: which is to allow or deny packets that match the direction, protocol, port, and source or destination of the rule.
- The priority of the rule: which governs the order in which rules are evaluated.
- Rule assignment: all rules are assigned to all instances, but you can assign certain rules to certain instances only.


Egress firewall rules control **outgoing connections originated inside** your GCP network. For egress firewall rules, destinations to which a rule applies may be specified using IP CIDR ranges.

Ingress firewall rules protect against **incoming connections to the instance from any source**. The firewall prevents instances from receiving connections on non-permitted ports and protocols. Source CIDR ranges can be used to protect an instance from undesired connections coming either from external networks or from GCP IP ranges. You can control ingress connections from a VM instance by constructing inbound connection conditions using source CIDR ranges, protocols, or ports.

Which firewall rule allows the ping to mynet-notus-vm's external IP address? 
A: mynetwork-allow-icmp. Public access to those instances is only controlled by the ICMP firewall rule


VPC networks are by default isolated private networking domains. Therefore, no internal IP address communication is allowed between networks, unless you set up mechanisms such as VPC peering or VPN


Commands used:
- ping -c 3 <Enter mynet-notus-vm's internal IP here>
- gcloud compute networks create privatenet --subnet-mode=custom
- gcloud compute networks subnets create privatesubnet-us --network=privatenet --region=Region 1 --range=172.16.0.0/24
- gcloud compute networks list
- gcloud compute networks subnets list --sort-by=NETWORK
- gcloud compute firewall-rules create privatenet-allow-icmp-ssh-rdp --direction=INGRESS --priority=1000 --network=privatenet --action=ALLOW --rules=icmp,tcp:22,tcp:3389 --source-ranges=0.0.0.0/0
- gcloud compute firewall-rules list --sort-by=NETWORK
- gcloud compute instances create privatenet-us-vm --zone=Zone 1 --machine-type=e2-micro --subnet=privatesubnet-us --image-family=debian-12 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=privatenet-us-vm
- gcloud compute instances list --sort-by=ZONE


Lab note: You cannot ping the internal IP address of managementnet-us-vm and privatenet-us-vm because they are in separate VPC networks from the source of the ping (mynet-us-vm), even though they are all in the same zone.

### Common Network Designs
1. If your application needs increased availability, you can place two virtual machines into multiple zones, but within the same subnet work. By allocating VMs on a single subnet to separate zones, you get improved availability without additional security complexity. It provides isolation for many types of infrastructure, hardware and software failures.

1. Globalization: Putting resources in different regions provides an even higher degree of failure independence. When using a global load balancer like the HTTP load balancer, you can route traffic to the region that is closest to the user. This can result in better latency for users and lower network traffic costs for your project.


A general security **best practice is only assigning internal IP addresses to your VM instances**, whenever possible.

Cloud NAT (Network Address Translation) is Google's managed network address translation service. It lets you provision your application instances without public IP addresses, while also allowing them to access the internet in a controlled and efficient manner. This means your private instances can access the internet for updates, patching, configuration management, and more.  In the class example Cloud NAT enables two private instances to access an update server on the Internet, which is referred to as outbound NAT. However, Cloud NAT does not Implement inbound NAT. In other words, hosts outside your VPC network cannot directly access any of the private instances behind the cloud NAT gateway.


You should enable private Google access to allow VM instances that only have internal IP addresses to reach the external IP addresses of Google APIs and services. For example, if your private VM instance needs to access a cloud storage bucket, you need to enable private Google access. **Private Google access has no effect on instances that have external IP addresses**, that's why VMs A2 and B2 can access Google APIs and services.

#### Implementing Private Google Access and Cloud NAT
In this lab, you implement Private Google Access and Cloud NAT for a VM instance that doesn't have an external IP address. Then you verify access to public IP addresses of Google APIs and services and other connections to the Internet.

The objectives of this lab are:
- Configure a VM instance that doesn't have an external IP address
- Connect to a VM instance using an Identity-Aware Proxy (IAP) tunnel
- Enable Private Google Access on a subnet
- Configure a Cloud NAT gateway
- Verify access to public IP addresses of Google APIs and services and other connections to the internet

When instances do not have external IP addresses, they can only be reached by other instances on the network via a managed VPN gateway or via a Cloud IAP tunnel. Cloud IAP enables context-aware access to VMs via SSH and RDP without bastion hosts. 

Private Google Access is enabled at the subnet level. When it is enabled, instances in the subnet that only have private IP addresses can send traffic to Google APIs and services through the default route (0.0.0.0/0) with a next hop to the default internet gateway.

With the Private Google Access the vms can now access certain Google APIs and services without an external IP address, but the instance cannot access the internet for updates and patches. Running sudo apt-get update in the vm should only work for Google Cloud packages because the VMs only has access to Google APIs and services. Configuring a **Cloud NAT gateway allows the vms to reach the internet**.

Cloud NAT is a regional resource. You can configure it to allow traffic from all ranges of all subnets in a region, from specific subnets in the region only, or from specific primary and secondary CIDR ranges only.

Cloud NAT logs are generated for the following sequences:
- When a network connection using NAT is created.
- When a packet is dropped because no port was available for NAT.


Commands:
- gcloud compute ssh vm-internal --zone ZONE --tunnel-through-iap
- ping -c 2 www.google.com