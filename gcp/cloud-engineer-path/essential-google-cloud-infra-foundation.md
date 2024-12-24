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

## Virtual Machines
A VM is similar but not identical to a hardware computer. VMs consists of a virtual CPU, some amount of memory, disk storage, and an IP address.

Compute Engine is GCP's service to create VMs. It is very flexible and offers many **options including some that can't exist in physical hardware**. For example:
- a micro VM shares a CPU with other virtual machines, so you can get a VM with less capacity at a lower cost.
- some VMs offer burst capability: the virtual CPU will run above its rated capacity for a brief period, using the available shared physical CPU.

The main VM options are CPU, memory, discs, and networking.

Compute Engine features
- Machine rightsizing
    - Recommendation engine for optimum machine size
    - Cloud Monitoring statistics
    - New recommendation 24 hours after VM create or resize
- Instance metadata
- Startup and shutdown scripts
- Availability policies
    - Live migrate
    - Auto restart
- Global load balancing
    - Multiple regions for availability
- OS patch management:
    - Create patch approvals
    - Set up flexible scheduling
    - Apply advanced patch configuration settings
- Per-second billing
- Sustained use discounts
- Committed use discounts
- Preemptible and Spot VMs
    - up to 91% discount
    - No SLA

### Compute Options
Three disk options: Standard, SSD, or local SSD. Both of these options provide the same amount of capacity in terms of disk size when choosing a persistent disk. Therefore, the question really is about performance versus cost, because there's a different pricing structure. SSDs are designed to give you a **higher number of IOPS per dollar** versus standard disks, which will give you a **higher amount of capacity per dollar**. 

Local SSDs have higher throughput and lower latency than SSD persistent disks, because they are attached to the physical hardware. The data that you store on local SSDs persists only until you stop or delete the instance. Typically, a local SSD is used as a swap disk.

Networking:
- auto, custom networkds
- Inbound/outbound firewall rules
    - IP based
    - Instance/group tags
- Regional HTTPS load balancing
- Network load balancing
    - Doesn't require pre-warming
- Global and multi regional subnotworks

#### VM Access and lifecycle
VM access:
1. On a Linux instance (SSH):
    - The creator has SSH capability and can use the Google Cloud console to grant SSH capability to other users.
    - SSH from computer or third-party client and generate key pair
    - Requires firewall rule to allow tcp:22
1. On a Windows instance (RDP):
    - the creator can use the console to generate a username and password and anyone who knows the username and password can connect to the instance using a Remote Desktop Protocol, or RDP, client.
    - RDP clients and Powershell terminal
    - Requires setting the Windows password
    - Requires firewall rule to allow tcp:3389

The lifecycle of a VM:
1. States:
    1. Provisioning
    1. Staging
    1. Running/Repairing
    1. Supending/Suspended or Stopping/Terminated
1. After running, its possible to:
    - instances.suspend()
    - instances.stop()
    - instances.delete()
1. If suspend:
    - instances.delete()
    - instances.resume()
1. If Terminated:
    - instances.delete()
    - instances.start()

Compute Engine can live migrate your virtual machine to another host due to a maintenance event to prevent your applications from experiencing disruptions. A VM's availability policy determines how the instance behaves in such an event. The default maintenance behavior for instances is to live migrate, but you can change the behavior to terminate your instance during maintenance events instead. If your VM is terminated due to a crash or other maintenance event, your instance automatically restarts by default, but this can also be changed.

Availability policy: Automatic changes
- Automatic restart
    - Automatic VM restart due to crash or maintenance event (not preemption or a user-initiated terminate)
- On host maintenance
    - Determines whether host is live-migrated or terminated due to a maintenance event (Live migration is the default)
- Live migration
    - During maintenance event, VM is migrated to different hardware without interruption
    - Metadata indicates occurrence of live migration

OS updated and patch management is an essential part of managing an infrastructure. Google Offers the **OS patch management** to easily keep infrastructures up-to-date and reduce the risk of security vulnerabilities. This service has two main components:
1. Patch compliance reporting, which provides insights on the patch status of your VM instances across Windows and Linux distributions. Also, recommendation.
1. Patch deployment, which automates the operating system and software patch update process. it schedules patch jobs.

There are several tasks that can be performed with patch management:
- Create patch approvals
- select what patches to apply to your system from the full set of updates available for the specific operating system
- Set up flexible scheduling
- choose when to run patch updates (one-time and recurring schedules)
- Apply advanced patch configuration settings
- customize patches by adding configurations such as pre and post patching scripts
- manage these patch jobs or updates from a centralized location

When a VM is terminated, you do not pay for memory and CPU resources. However, **you are charged for any attached disks and reserved IP addresses**. In the terminated state, you can perform any of the actions listed here, such as changing the machine type, but you cannot change the image of a stopped VM.

#### Creating Virtual Machine Lab
In this lab, you created several virtual machine instances of different types with different characteristics. One was a small utility VM for administration purposes. You also created a standard VM and a custom VM.

Note: Notice that you cannot change the machine type, the CPU platform, or the zone.

You can add network tags and allow specific network traffic from the internet through firewalls. Some properties of a VM are integral to the VM, are established when the VM is created, and cannot be changed. Other properties can be edited.

You can add additional disks and you can also determine whether the boot disk is deleted when the instance is deleted.

Normally the boot disk defaults to being deleted automatically when the instance is deleted. But sometimes you will want to override this behavior. This feature is very important because you cannot create an image from a boot disk when it is attached to a running instance.

So you would need to disable Delete boot disk when instance is deleted to enable creating a system image from the boot disk.

Note 2: You cannot convert a non-preemptible instance into a preemptible one. This choice must be made at VM creation. A preemptible instance can be interrupted at any time and is available at a lower cost.

If a VM is stopped for any reason, (for example an outage or a hardware failure) the automatic restart feature will start it back up. Is this the behavior you want? Are your applications idempotent (written to handle a second startup properly)?

During host maintenance, the VM is set for live migration. However, you can have the VM terminated instead of migrated.

If you make changes, they can sometimes take several minutes to be implemented, especially if they involve networking changes like adding firewalls or changing the external IP.

Commands:
- To see information about unused and used memory and swap space on your custom VM, run the following command: `free`
- To see details about the RAM installed on your VM, run the following command: `sudo dmidecode -t 17`
- To verify the number of processors, run the following command: `nproc`
- To see details about the CPUs installed on your VM, run the following command: `lscpu`

### Compute Options
Three options for creating and configuring a VM:
1. Cloud Console
1. Cloud Shell
1. RESTful API

If you plan on using the command line or RESTful API, I'ts recommend that you first configure the instance through the Google Cloud console and then ask Compute Engine for the equivalent REST request or command line.

When you create a VM, you select a machine type from a machine family that determines the resources available to that VM. There are several machine families you can choose from and each machine family is further organized into machine series and predefined machine types within each series. A machine family is a curated set of processor and hardware configurations optimized for specific workloads.

There are four Compute Engine machine families:
- General-purpose: 
    - E2:
        - Machine types for common workloads, optimized for cost and flexibility.
        - The E2 machine series is suited for day-to-day computing at a lower cost, especially where there are no application dependencies on a specific CPU architecture.
        - The Standard E2 VMs have between 2 to 32 vCPUs with a ratio of 0.5 GB to 8 GB of memory per vCPU.
        - They are a great choice for web servers, small to medium databases, development and test environments, and many applications that don't have strict performance requirements.
        - It constains a shared-core machine types that use context-switching to share a physical core between vCPUs for multitasking.
    - N2 and N2D:
        - They are the most flexible VM types and provide a balance between price and performance across a wide range of VM shapes, including enterprise applications, medium-to-large databases, and many web and app-serving workloads.
        - N2 supports the latest second generation scalable processor from Intel with up to 128 vCPUs and 0.5 to 8 GB of memory per vCPU.
        - N2D latest EPYC Milan and EPYC Rome processors, and provide up to 224 vCPUs per node.
    - T2A and T2D:
        - Scale-out workloads
        - run on Arm processors
        - If you have containerized workloads, Tau VMs are supported by Google Kubernetes Engine to help optimize price-performance.
- Compute-optimized
    - Machine types for performance-intensive workloads, with **highest performance per core**
    - Best fit for: AAA gaming, electronic design automation, and high-performance computing across simulations, genomic analysis, or media transcoding.
    - C2: from 4 to 60 vCPUs, and offers up to 240 GB of memory
    - C2D machine series provides the largest VM sizes and are best-suited for high-performance computing. It also has the largest available last-level cache per core
    - H3 series offer 88 cores and 352 GB of DDR5 memory
- Memory-optimized
    - Machine types for workloads with higher memory-to-vCPU ratios, like in-memory databases 
    - M1 machine series has up to 4 TB of memory, while the M2 machine series has up to 12 TB of memory.
    - These machine series are well-suited for large in-memory databases such as SAP HANA, as well as in-memory data analytics workloads.
    - Both the M1 and M2 machine series offer the lowest cost per GB of memory on Compute Engine, making them **a great choice for workloads that utilize higher memory configurations with low compute resource requirements**.
- Accelerator-optimized (GPUs)
    - Graphics processing units (GPUs) accelerate specific workloads on your instances such as machine learning and data processing.
    - it is ideal for massively parallelized Compute Unified Device Architecture (CUDA) compute workloads, such as machine learning and high-performance computing.
    - A2, A3, G2, N1
    - The A2 series has 12 to 96 vCPUs, and up to 1360 GB of memory.
    - G2 VMs offer 4 to 96 vCPUs, up to 432 GB of memory. It is well-suited for CUDA-enabled ML training and inference, video transcoding, remote visualization workstation.
- Storage optimized
    - Machine types for storage-intensive workloads, like horizontal, scale-out databases.


Alternatively, it's possible to create custom machine types. These let you specify the number of vCPUs and the amount of memory for your instance. It is ideal for when you have workloads that are not a good fit for the predefined machine types that are available to you. 

It costs slightly more to use a custom machine type than an equivalent predefined machine type, and there are still some limitations in:
- Only machine types with 1 vCPU or an even number of vCPUs can be created.
- Memory must be between 1 GB and 8 GB per vCPU.
- The total memory of the instance must be a multiple of 256 MB.

### Compute pricing
All vCPUs, GPUs, and GB of memory are charged a minimum of 1 minute. After 1 minute, instances are charged in 1-second increments.

Compute Engine uses a resource-based pricing model, where each vCPU and each GB of memory on Compute Engine is billed separately rather than as a part of a single machine type.

If your workload is stable and predictable, you can purchase a specific amount of vCPUs and memory for a discount off of normal prices in return for committing to a usage term of 1 year or 3 years.

Preemptible and Spot VMs are instances that you can create and run at a much lower price than normal instances. 
For both types of VM, Compute Engine might terminate (or preempt) these instances if it requires to access those resources for other tasks.

Compute Engine provides VM sizing recommendations to help you optimize the resource used of your virtual machine instances. Recommendations for the new instance will appear 24 hours after the instance has been created.

Sustained use discounts are automatic discounts that you get for running specific Compute Engine resources (vCPUs, memory, and GPU devices) for a significant portion of the billing month. For example, when you run one of these resources for more than 25% of a month.
- if you use a virtual machine for 50% of the month, you can an effective discount of 10%.
- If you use it for 75% of the month, you get an effective discount of 20%.
- If you use it for 100% of the month, you get an effective discount of 30%