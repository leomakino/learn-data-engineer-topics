# Google Cloud Fundamentals: Core Infrastructure
Google Cloud Fundamentals: Core Infrastructure introduces important concepts and terminology for working with Google Cloud. it compares many of Google Cloud's computing and storage services, along with important resource and policy management tools.

## Introducing Google Cloud
Iaas offerings provide:
- raw compute
- storage
- network capabilities

The Google Cloud network is the largest network of its kind, and Google has invested billions of dollars over many years to build it. This network is designed to give customers the highest possible throughput and lowest possible latencies for their applications by leveraging more than 100 content caching nodes worldwide. Google Cloud's locations underpin all of the important work we do for our customers. From redundant cloud regions to high-bandwidth connectivity via subsea cables, every aspect of our infrastructure is designed to deliver your services to your users, no matter where they are around the world.


Google Cloud's infrastructure is based in five major geographic locations: 
- North America
- South America
- Europe
- Asia
- and Australia.

Each of these locations is divided into several different regions and zones. Regions represent independent geographic areas and are composed of zones. A zone is an area where Google Cloud resources are deployed.

You can run resources in different regions. This is useful for bringing applications closer to users around the world, and also for protection in case there are issues with an entire region, say, due to a natural disaster.


The security infrastructure can be explained in progressive layers, starting from the physical security os the data centers,continuing on to how the hardware and software that underlie the infrastructure are secured, and finally, describing the technical constraints and processes in place to support operational security.
1. Hardware infrastructure layer
    - hardware design and provenance: server boards, networking equipment, security chip are custom-designed by Google.
    - Secure boot stack: Google server machines use a variety of technologies to ensure that they are booting the correct software stack
    - Premises security: Access to data centers is limited to only a very small number of Google employees.
1. Service deployment layer
    - Encryption of inter-service communication
    - Google's services communicate with each other using RPC calls (cryptographic privacy and integrity for remote procedure)
1. User identity layer
    - manifests to end users as the Google login page
    - it goes beyond asking for a simple username and password
1. Storage services layer
    - Encryption at rest
1. Internet communication layer
    - Google Front End (GFE): ensures that all TLS connections are ended using a public-private key pair and an X.509 certificate autority (CA)
    - Denial of Service (DoS) protection: Google has multi-tier, multi-layer DoS protections
1. Operational security layer
    - Intrusion detection: Rules and machine intelligence give Google's operational security teams warnings of possible incidents.
    - Reducing insider risk: Google aggressively limits and actively monitors the activities of employees who have been granted administrative access to the infrastructure.
    - Employee Universal Second Factor (U2F) use: To guard against phishing attacks against Google employees, employee accounts require use of U2F-compatible Security Keys.
    - Software development practices: Google employs central source control and requires two-party review of new code.
    

## Resources and Access in the Cloud
### Resource Hierarchy
The resource hierarchy directly relates to how policies are managed and applied on Google Cloud.

Policies can be defined at the project, folder, and organization node levels. Some Google Cloud services allow policies to be applied to individual resources, too. Policies are also inherited downward.


Google Cloud's Resource Manager tool is designed to programmatically help you manage projects. It's an API that can gather a list of all the projects associated with an account, create new projects, update existing projects, and delete projects.

How a new organization node is created depends on whether your company is also a Google Workspace customer. If you have a Workspace domain, Google Cloud projects will automatically belong to your organization node. Otherwise, you can use Cloud Identity, Google's identity, access, application, and endpoint management platform, to generate one.

### IAM
Otherwise, you can use Cloud Identity, Google's identity, access, application, and endpoint management platform, to generate one.

A “who” is also called a “principal.” Each principal has its own identifier, usually an email address.


You can define deny rules that prevent certain principals from using certain permissions, regardless of the roles they're granted. This is because IAM always checks relevant deny policies before checking relevant allow policies. Deny policies, like allow policies, are inherited through the resource hierarchy.


There are three kinds of roles in IAM: 
1. basic, 
1. predefined, and 
1. custom.

Basic roles include:
- viewer: can access resources but can't make changes.
- editor: can access and make changes to a resource
- owner: access and make changes to a resource; can manage the associated roles and permissions and set up billing
- billing administrator: control the billing for a project but not be able to change the resources in the project


Custom roles will allow you to define those exact permissions. Two important details about custom roles:
- need to manage the permissions that define the custom role you've created.
- it can only be applied to either the project level or organization level.

### Cloud Identity
With Cloud Identity, organizations can define policies and manage their users and groups using the Google Admin Console.


## Virtual Machines and Networks in the Cloud

### VPC
What is a virtual private cloud? VPC, is a secure, individual, private cloud-computing model hosted within a public cloud.

A VPC network is a global resource that consists of a list of regional virtual subnetworks (subnets) in data centers, all connected by a global wide area network (WAN). VPC networks are logically isolated from each other in Google Cloud.


Subnets can span the zones that make up a region. This architecture makes it easy to define network layouts with global scope. Resources can even be in different zones on the same subnet.

The size of a subnet can be increased by expanding the range of IP addresses allocated to it, and doing so won't affect virtual machines that are already configured.

### Compute Engine
A virtual machine instance can be created via the Google Cloud console, the Google Cloud CLI, or the Compute Engine API.
The instance can run Linux and Windows Server images provided by Google or **any customized versions** of these images.


Compute Engine also offers committed-use discounts. This means that for stable and predictable workloads, a specific amount of vCPUs and memory can be purchased for up to a 57% discount off of normal prices in return for committing to a usage term of one year or three years.


There are Preemptible and Spot VMs. An example, you have a workload that doesn't require a human to sit and wait for it to finish such as a batch job analyzing a large dataset.
You can save money, in some cases up to 90%, by choosing Preemptible or Spot VMs to run the job.


A Preemptible or Spot VM is different from an ordinary Compute Engine VM in only. Spot VMs differ from Preemptible VMs by offering more features. 
- preemptible VMs can only run for up to 24 hours at a time, but Spot VMs do not have a maximum runtime.
- the pricing is, currently the same for both.


Compute Engine has a feature called Autoscaling, where VMs can be added to or subtracted from an application based on load metrics. The other part of making that work is balancing the incoming traffic among the VMs.


VPC supports several different kinds of load balancing, which we'll explore shortly.


Virtual Private Cloud compatibility features:
- VPC routing tables are built-in so you don't have to provision or manage a router.
    - They're used to forward traffic from one instance to another within the same network, across subnetworks, or even between Google Cloud zones, without requiring an external IP address.
- Firewalls also are built-in so you don't have to provision or manage
    - VPCs provide a global distributed firewall, which can be controlled to restrict access to instances through both incoming and outgoing traffic.
    - Firewall rules can be defined through network tags on Compute Engine instances,
    - Each VPC network implements a distributed virtual firewall that you can configure. Firewall rules allow you to control which packets are allowed to travel to which destinations.

VPCs belong to Google Cloud projects, but what if your company has several Google Cloud projects, and the VPCs need to talk to each other? A: VPC Peering, a relationship between two VPCs can be established to exchange traffic.
Alternatively, to use the full power of Identity Access Management (IAM) to control who and what in one project can interact with a VPC in another, you can configure a Shared VPC.

How do your customers get to your application when it might be provided by four VMs one moment, and by 40 VMs at another? That's done through **Cloud Load Balancing**.

Cloud Load Balancing is a fully distributed, software-defined, managed service for all your traffic.
- The job of a load balancer is to distribute user traffic across multiple instances of an application.
- By spreading the load, load balancing reduces the risk that applications experience performance issues.
- you don't have to worry about scaling or managing them.
- You can put Cloud Load Balancing in front of all of your traffic: HTTP or HTTPS, other TCP and SSL traffic, and UDP traffic too.
- it provides cross-region load balancing, including automatic multi-region failover, which gently moves traffic in fractions if backends become unhealthy.
- it reacts quickly to changes in users, traffic, network, backend health, and other related conditions.



VPC offers a suite of load-balancing options:
- Global HTTP(S)
    - if you need cross-regional load balancing
- Global SSL Proxy
    - for Secure Sockets Layer traffic that is not HTTP
- Global TCP Proxy
    - If it's other TCP traffic that doesn't use SSL
- Regional External
    - they're intended for traffic coming into the Google network from the internet.
    - TCP: proxy services only work for specific port numbers
    - UDP traffic: traffic on any port number
- Regional Internal
    - traffic inside your project
    - supports Proxy Network load balancer, Passthrough Network load balancer, and Application load balancer.
    - It accepts traffic on a Google Cloud internal IP address and load balances it across Compute Engine VMs.
- Cross-region internal
    - It is a Layer 7 load balancer that enables you to load balance traffic to backend services that are globally distributed, including traffic management that ensures traffic is directed to the closest backend.


Routes tell VM instances and the VPC network how to send traffic from an instance to a destination, either inside the network or outside Google Cloud.

**Cloud DNS:** 

what about the internet hostnames and addresses of applications built in Google Cloud? Google Cloud offers Cloud DNS to help the world find them.
- It's a managed DNS service that runs on the same infrastructure as Google.
- It has low latency and high availability, and it's a cost-effective way to make your applications and services available to your users.
- publish and manage millions of DNS zones and records using the Cloud Console, the command-line interface, or the API.

**Cloud CDN:**


Google also has a global system of edge caches. Edge caching refers to the use of caching servers to store content closer to end users. use this system to accelerate content delivery

### Connecting networks to Google VPC

Many Google Cloud customers want to connect their Google Virtual Private Cloud networks to other networks in their system, such as on-premises networks or networks in other clouds. There are several effective ways to accomplish this:
- Cloud VPN: 
    - One option is to start with a Virtual Private Network connection over the internet and use **Cloud VPN** to create a “tunnel” connection.
    - To make the connection dynamic, a Google Cloud feature called **Cloud Router** can be used.
    - Cloud Router lets other networks and Google VPC, exchange route information over the VPN using the Border Gateway Protocol.
        - Using this method, if you add a new subnet to your Google VPC, your on-premises network will automatically get routes to it.
    - Using the internet to connect networks isn't always the best option for everyone, either because of security concerns or because of bandwidth reliability.
- Direct Perring
    - Peering means putting a router in the same public data center as a Google point of presence and using it to exchange traffic between networks.
    - Customers who aren't already in a point of presence can work with a partner in the Carrier Peering program to get connected.
- Carries Perring
    - it gives the direct access from your on-premises network through a service provider's network to Google
    - One downside of peering, though, is that it isn't covered by a Google Service Level Agreement.
- Dedicated Interconnect
    - If getting the highest uptimes for interconnection is important, using Dedicated Interconnect would be a good solution.
    - connections must have topologies that meet Google's specifications to be covered by an SLA of up to 99.99%.
- Partner Interconnect
    - provides connectivity between an on-premises network and a VPC network through a supported service provider
    - it is useful if a data center is in a physical location that can't reach a Dedicated Interconnect colocation facility, or if the data needs don't warrant an entire 10 GigaBytes per second connection.
    - Google isn't responsible for any aspects of Partner Interconnect provided by the third-party service provider, nor any issues outside of Google's network.
- Cross-Cloud Interconnect
    - it helps you establish high-bandwidth dedicated connectivity between Google Cloud and another cloud service provider.
    - it supports your adoption of an integrated multicloud strategy.
    - it offers reduced complexity, site-to-site data transfer, and encryption.

## Storage in the cloud
### Cloud Storage
The storage objects offered by Cloud Storage are immutable, which means that you do not edit them, but instead a new version is created with every change made. Administrators have the option to either allow each new version to completely overwrite the older one, or to keep track of each change made to a particular object by enabling “versioning” within a bucket. If you don’t turn on object versioning, by default new versions will always overwrite older versions.

Using IAM roles and, where needed, access control lists (ACLs), organizations can conform to security best practices (principle of least privilege).


There are a couple of options to control user access to objects and buckets:
- For most purposes, IAM is sufficient;
    - Roles are inherited from project to bucket to object.
- To finer control, you can create access control lists (ACLs).
    - Each access control list consists of two pieces of information.
    - The first is a **scope**, which defines who can access and perform an action.
    - The second is a **permission**, which defines what actions can be performed.

There are several ways to bring data into Cloud Storage
- online transfer using commands (gcloud storage) 
- Drag and drop option using web browser
- Storage Transfer Service enables you to import large amounts of online data into Cloud Storage quickly and cost-effectively.
    - it lets you schedule and manage batch transfers to Cloud Storage from: 
        1. another cloud provider, 
        1. different Cloud Storage region 
        1. an HTTP(S) endpoint.
- Transfer Appliance, which is a rackable, high-capacity storage server that you lease from Google Cloud.
    - You can transfer up to a petabyte of data on a single appliance.

### Cloud SQL
It is the Google Cloud’s second core storage option is Cloud SQL. Cloud SQL offers fully managed relational databases, including MySQL, PostgreSQL, and SQL Server as a service.

Cloud SQL doesn't require any software installation or maintenance. It can scale up to 128 processor cores, 864 GB of RAM, and 64 TB of storage.

It includes a network firewall, which controls network access to each database instance.

A benefit of Cloud SQL instances is that they are accessible by other Google Cloud services (e.g. Compute Engine), and even external services.

### Spanner
key words: relational, global, high numbers of operations per second

### Firestore
NoSQL cloud database for mobile, web, and server development.


Data is stored in documents and then organized into collections. Documents can contain complex nested objects in addition to subcollections. Each document contains a set of key-value pairs.

Query performance is proportional to the size of the result set,


Firestore uses data synchronization to update data on any connected device.


### Bigtable
Bigtable is Google's NoSQL big data database service. It is a great choice for both operational and analytical applications.


Bigtable can interact with other Google Cloud services and third-party clients.

Data can also be streamed in through a variety of popular stream processing frameworks like Dataflow Streaming, Spark Streaming, and Storm. And if streaming is not an option, data can also be read from and written to Bigtable through batch processes like Hadoop MapReduce, Dataflow, or Spark.


### Obs: BQ
BigQuery hasn’t been mentioned in this section of the course because it sits on the edge between data storage and data processing.

The usual reason to store data in BigQuery is so you can use its big data analysis and interactive querying capabilities, but it’s not purely a data storage product.