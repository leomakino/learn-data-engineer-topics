# Infrastructure and Application Modernization with Google Cloud
Many traditional enterprises use legacy systems and applications that often struggle to achieve the scale and speed needed. IT decision makers constantly have to choose between maintenance of legacy systems and investing in innovative new products and services.

This course explores the challenges of an outdated IT infrastructure and how businesses can modernize it using cloud technology. It begins by exploring the different compute options available in the cloud and the benefits of each, before turning to application modernization and Application Programming Interfaces (APIs).

## Modernizing IT infrastructure

### Introduction
Consumer expectations over the last 20 years have radically changed. Customers now expect connected digital experiences in real time.

Many businesses, especially large enterprises, built their IT infrastructure on premises.

Legacy systems and applications make up the organization's IT backbone. Also, these legacy systems and applications struggle to achieve the scale and speed needed.

In this course, we'll explore the challenges of an outdated IT infrastructure and how businesses can modernize that infrastructure using cloud. Examine compute options available in the cloud and the benefits of each.

The module two, will focus on application modernization. Cloud technology enables businesses to develop, deploy and update applications with speed, security and agility built in.

It will cover App Engine, a GCP solution that lets application developers build scalable web and mobile applications on a fully managed serveless platform.

The module three presents APIs and explain how they unlock value from legacy systems, enable businesses to create new value, and monetize new services.

It will also cover Apache, a GCP for developing and managing APIs.

Remember, it's not necessary to be an IT specialist to create new business value or to develop innovative services. By understanding how infrastructure, applications, and APIs work together, you can initiate conversations about new projects and be more knowledgeable about strategic planning for digital transformation.

### Infrastructure modernization
For most organizations, owning and operating infrastructure is often a burden. 
It limits an organization’s staff in several ways:
- They have to undertake laborious tasks related to infrastructure;
- systems can be too old;
- using legacy systems, the organization can not scale with any ease because the organization is locked into what its have on premises.

One option for reducing this burden is to migrate to the cloud.

The first step in moving away from an on-premises infrastructure is colocation. 

A business sets up a large data center and then other organizations rent part of that data center. This means organizations no longer have to pay the costs associaited with hosting the infrastructure, but they still need to pay to maintain it.

Hardware is often heavily under utilized, even in the colocation model, so engineers packaged applications and their operating systems into a virtual machine.

Virtual machines share and optimize the same pool of computer processing, storage and networking resources. They enable businesses to have multiple applications running at the same time on a server.

IaaS can move some or all of its infrastructure away from physical data centers to virtualized data centers in the cloud.

The maintenance work is outsourced to the public cloud provider so it’s easier to shift a larger proportion of company expertise to build processes and applications that move the business forward.

PaaS you don't have to manage the infrastructure and for some services you only pay for what you use.

### Available computer options
Compute or computing refers to a machine's ability to process information (to store, retrieve, compare, and analyze it) and automate tasks often done by computer programs, otherwise known as software or applications.

Hypervisor is the software layer that sits on top of physical hardware, and multiple VMs are built on top of it. It’s like having multiple computers that only use one piece of hardware.

**VM**s recreate a full representation of the hardware. Containers only recreate, or virtualize, the OS.

**Containers**:
- only hold exactly what's needed for the particular application that they support. 
- They start faster, use less memory, and allow developers to create predictable environments.
- are like prefabricated units placed on top of each other. This means that any problem that arises is easier to isolate and fix.

**Serveless computing**: 
- resources, such as compute power, are automatically provisioned behind-the-scenes as needed.
- This kind of solution are often called 'function-as-a-service'. Businesses provide the code for whatever function they want and the public cloud provider does everything else.

### Private, hybrid and multi-cloud architectures
Private cloud is where an organization has **virtualzed servers** in its own data centers to create its own private on-premises environment. This might be done when an organization has already made significant investments in its own infrastructure, or if, for regulatory reasons, data needs to be kept on-premises.

Hybrid cloud:
It is when an organization is using a combination of on-premises or private cloud infrastructure and public cloud services. Some data and applications have been migrated to the cloud and others remain on premises.

Multi-cloud:
- using multiple public cloud providers as part of its architecture.
The organization needs flexibility and secure connectivity between the different networks involved

### GCP Compute solutions
Leveraging cloud technology to truly transform a business requires new collaborative models, changing culture and processes, and enabling team productivity and innovation.

Google Services:
- **Virtal Machines**: Compute Engine, VMWare Engine, Bare Metal
- **Container**: Google Kubernets Engine 
- **Serveless computing**: Cloud Run, Cloud Function, App Engine. 

Compute Engine:
- Is a computing and hosting service that lets you create and run VMs on Google Infrastructure.
- Vms boot quickly, come with persistent disk storage, and deliver consistent performance.

VMware Engine: 
- It is a fully managed service that lets you run the VMware platform in Google Cloud.

Bare Metal:
- enables to migrate specialized workloads to the cloud, while maintaning your existing investments and architecture.
- allows to access and integrate with Google Cloud services with minimal latency.

Google Kubernets or GKE: 
- provides a managed enviroment for deploying, managing, and scaling containerized applications using Google infrastructure. The GKE environment consists of multiple machines grouped together to form a cluster.
- allows securely speed up app development, streamline operations, and manage infrastructure.

Google App Engine:
- It is a PaaS and cloud computing platform for developing and hosting web applications. It lets app developers build scalable web and mobile back ends in any programming language on a fully managed serverless platform.

Cloud Run:
- allows to build applications in several programming language, dependencies and tools. It abstracts away all the infrastructure management by automatically scaling up and down.

Cloud function:
- is a serveless execution environment for building and connecting cloud services. It offers scalable, pay-as-you-go functions as a service to run code with zero server management.