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

With both on premises and colocation, value creation only starts well after a substantial amount of capital expenditure or capex is committed.

Hardware is often heavily under utilized, even in the colocation model, so engineers packaged applications and their operating systems into a virtual machine.

Virtual machines share and optimize the same pool of computer processing, storage and networking resources. They enable businesses to have multiple applications running at the same time on a server.

IaaS can move some or all of its infrastructure away from physical data centers to virtualized data centers in the cloud.

The maintenance work is outsourced to the public cloud provider so it’s easier to shift a larger proportion of company expertise to build processes and applications that move the business forward.

PaaS you don't have to manage the infrastructure and for some services you only pay for what you use.

### Available computer options
Compute or computing refers to a machine's ability to process information (to store, retrieve, compare, and analyze it) and automate tasks often done by computer programs, otherwise known as software or applications.

Hypervisor is the software layer that sits on top of physical hardware, and multiple VMs are built on top of it. It’s like having multiple computers that only use one piece of hardware.

**Virtualization**:
- It is a form of resource optimization that allows multiple systems to run on the same hardware. These systems are called virtual machines.

**VMs**
- recreate a full representation of the hardware. Containers only recreate, or virtualize, the OS.
- enable businesses to have multiple applications running at the same time on a server in a way that is efficient and manageable.

**Containers**:
- only hold exactly what's needed for the particular application that they support. 
- They're even more efficient: they start faster, use less memory, and allow developers to create predictable environments.
- are like prefabricated units placed on top of each other. This means that any problem that arises is easier to isolate and fix.

**Serveless computing**: 
- resources, such as compute power, are automatically provisioned behind-the-scenes as needed.
- This kind of solution are often called 'function-as-a-service'. Businesses provide the code for whatever function they want and the public cloud provider does everything else.

**Resource pooling**:
- If one data center is down due to a natural disaster, for instance, another data center is available to prevent service disruption.

**Broad network access**:
- This means that access to data and compute resources is no longer tied to a particular geography or location

### Private, hybrid and multi-cloud architectures
how do you modernize the infrastructure you have without jumping completely to the cloud? How do you bridge incompatible architectures while you transition?
Answer: involve some on-premises infrastructure working in conjunction with public cloud services

Private cloud is where an organization has **virtualzed servers** in its own data centers to create its own private on-premises environment. This might be done when an organization has already made significant investments in its own infrastructure, or if, for regulatory reasons, data needs to be kept on-premises.

Hybrid cloud:
It is when an organization is using a combination of on-premises or private cloud infrastructure and public cloud services. Some data and applications have been migrated to the cloud and others remain on premises.

Multi-cloud:
- using multiple public cloud providers as part of its architecture.
The organization needs flexibility and secure connectivity between the different networks involved

When organizations are considering a move to a hybrid cloud or multi-cloud situation, they are often concerned about how easy it will be to move an application from one cloud to another. Google believes in an open cloud where users have the rights to move their data as they choose and not being tied to a particular cloud.

Examples: Google Cloud uses open APIs and Google services are compatible with open-source services and products. Because Google Cloud publishes key elements of its technology using open-source licenses, customers can use products both on-premises and on multiple clouds.

Google Cloud matches 100% of the energy consumed by our global operations with renewable energy and maintains a commitment to carbon neutrality. So, by moving compute from a self-managed data center or colocation facility to Google Cloud, the net emissions directly associated with your company's compute and data storage will be zero. 

### GCP Compute solutions
Leveraging cloud technology to truly transform a business requires new collaborative models, changing culture and processes, and enabling team productivity and innovation.

Let's look at some specific Google Cloud solutions for:
- **Virtal Machines**: Compute Engine, VMWare Engine, Bare Metal
- **Container**: Google Kubernetes Engine (GKE)
- **Serveless computing**: Cloud Run, Cloud Function, App Engine. 

Compute Engine:
- Is a computing and hosting service that lets you create and run VMs on Google Infrastructure.
- Vms boot quickly, come with persistent disk storage, and deliver consistent performance.
- This solution is ideal if you need complete control over the virtual machine infrastructure.
- It's also useful if you need to run a software **package that can't easily be containerized** or **have existing VM images to move to the cloud**.

VMware Engine: 
- It is a type of software that you can run on a virtual machine.
- It is a fully managed service that lets you run the VMware platform in Google Cloud.

Bare Metal:
- enables to migrate specialized workloads to the cloud, while maintaning your existing investments and architecture.
- allows to access and integrate with Google Cloud services with minimal latency.

Google Kubernetes or GKE: 
- provides a managed enviroment for deploying, managing, and scaling containerized applications using Google infrastructure. The GKE environment consists of multiple machines grouped together to form a cluster.
- allows securely speed up app development, streamline operations, and manage infrastructure.

Google App Engine:
- It is a PaaS and cloud computing platform for developing and hosting web applications. It lets app developers build scalable web and mobile back ends in any programming language on a fully managed serverless platform.

Cloud Run:
- allows to build applications in several programming language, dependencies and tools. It abstracts away all the infrastructure management by automatically scaling up and down from zero almost instantly depending on user traffic.
- benefits: automatic scaling, multiple route support, and fast deployments

Cloud function:
- is a serveless execution environment for building and connecting cloud services. It offers scalable, pay-as-you-go functions as a service to run code with zero server management.
- write and run small code snippets that respond to events.

Anthos: 
- an open application modernization platform that enables to modernize your existing applications, build new ones, and run them anywhere.

### Quiz
1. Elasticity helps businesses serve their customers without service interruption and in a cost-effective way.

1. App Engine, Cloud Functions and Cloud Run are all Serveless computing type of Google Cloud compute option

1. A company is considering using public cloud services, specifically to modernize their IT infrastructure. With the modernization, the IaaS solution will be maintenance by the cloud provider

1. Containers recreate or virtualize Operating systems.

1. A company is using  combination of on-premises data centers and public cloud services for their IT infrastructure. This IT infrastructure model is called Hybrid-cloud because there is on-premises data centers. If the company uses several public cloud services without on-premises, it would be Multi-cloud.

## Modernizing Applications

### Introduction
What are applications?
A: Applications are computer programs or software that help users do something

Customers expect intuitive, well-functioning applications that enable them to do things faster.

Applications have been developed on-premises for years and still are. But on-premises application development often slows businesses down. Because deploying an application on-premises can be time-consuming and require specialized IT teams, and any new changes can take six months or even more to implement.

The module will explore how businesses can modernize their existing applications and build new ones in the cloud.

### Cloud change patterns
Moving an application to the cloud doesn't need to be done all at once.

There are five common patterns that businesses can adopt hen they want to modernize their applications:
1. Move applications to the cloud first and then change them
    - Conservative approach. Over time, futher modernization can be explored.
    - Brings minimal changes to the way of working within the organization
    - E.g.: Legacy application moved to the cloud 
1. Change the applications before they move
    - More aggressive approach
    - Re-architect applications first to make them more cloud ready before migrating them.
1. Invent in greenfield
    - Building an entirely new infrastruture and applications in the cloud
    - Only applies when an organization needs to develop new products or offerings.
1. Invent in brownfield
    - Invent a new application in the cloud that will replace an existing legacy application that remains on premises
    - The legacy application is only retired after the new application is built
    - It is redundancy and expensive (running two applications at time) but can minimize risk
    - E.g.: Legacy application moved to the cloud 
1. Move application without any changes
    - Leverage to the cloud just to modernize the infrastructure layer
    - Use case 1: Use cloud storage instead of on premises data centers
    - Use case 2: create virtualized environment for disaster recovery

### Challenges in application development
Creating a new application within an organization can be a challenge. It can take 18 months or maybe even tell you it's not possible with the legacy systems already in place.
when business professionals want a new application, the tech or IT team has to do a lot of work to identify features, estimate capacity, define a technical architecture, consider integration with other systems, and allocate resources even before a line of code is written.

New needs often compete with existing projects for time and resources.

Whether building an app on premises or in the cloud, developers still need to make decisions about overall network architecture, choice of database, and type of server.

The challenges for building apps using an on premises infrastructure can outnumber those of cloud native apps and can often be frustrating for developers and business professionals.

Building a new application in the cloud means you can be more agile in your development.

### Google Kubernetes Engine (GKE)
Containerization allows developer to divide an application design into individual compartments. It's an one-compute option for modernizing IT infrastructures. Parts of the code can be updated without affecting the whole application. Also, it builds resilience because one error doesn't impact the whole application.

A way to manage or orchestrate the containers is using Kubernetes, an open source container orchestration system for automating computer application deployment,scaling, and management.

Google Kubernetes Engine (GKE) is the Google Cloud manage service for container orchestration.

GKE enables rapid application development and iteration by making it easy to deploy, update, and manage your applications and services.

### App Engine
App Engine is a platform for building scalable Web applications and mobile back ends. It's manage the infrastructure (hardware, networking) automatically in response to the amount of traffic. Moreover, the company only pays for the resources it uses. 

It's possible to run multiple versions of the app to test new features or designs with end users.

### Quizz
1. GKE is a Google Cloud managed service for container orchestration
1. App Engine is a platform for building scalable web applications and mobile backends.
1. The primary value of using a CI/CD approach for the overall business is: "It increases application release velocity and reliability."
1. An online apparel retail company can use microservice pattern in its architecture because it's modular and therefore easy to update.
1. Migrating an existing application to the cloud reducing risk service downtime and building a new application in the cloud while continuing to run their old application on-premises (redundancy) refers to the invent in brownfield pattern.

## The value of APIs
When it comes to digital transformation, companies typically have the following three primary goals:
1. Modernize IT systems
1. Modernize Applications
1. Leverage Application Programming Interfaces (APIs)

APIs are a tool for both digital integration and digital transformation. 

### Legacy system challenges
A legacy system is outdated computing software and/or hardware that is still in use. It often is not equipped to deliver new services. Worse, a legacy system cannot connect to new systems.

Legacy sustems are valuable to the business because they hold a large amount of data. But unlocking the value of that data is challenging. They were developed for a time when data was shared in batches or at specific time intervals. It means, legacy sytems are not designed to serve real time data.

As a result, legacy sustems tend to hold organizations back from digital technologies to innovate or improve IT efficiency.

Modernizing IT infrastructure is central to digital transformation. So, businesses no longer have to choose between maintenance and innovation.

This means they need a well-designed integration strategy that leverages APIs

Legacy systems struggle to meet the demands of the digital age.

### How APIs can modernize legacy systems
API can be a solution for legacy system challenges.

API is a piece of software that connects different applications and enables information to flow between systems. In other words, APIs enable integration between systems. They do this by exposing data in a way that protects the integrity of the legacy systems and enables secure and govern access to the underlying data.

This allows organizations with older systems to adapt to modern business needs and, more importantly, to quickly adopt new technologies and platforms.

APIs enable businesses to unlock value without architecting all of those legacy applications. It's a way to build long term flexibility.

Customers expect real time, seamless experiences across platforms. Businesses now have the opportunity to digitize experiences throughout their value chain to meet their customers expectations.

APIs are therefore central to any business's digital transformation strategy. Because, they enable faster innovation. So, organizations can bring new services to market quickly and create new business value.

### Using APIs to create new business value
APIs started as a tool to facilitate access and integration. They still serve those functions, but now APIs can do so much more.

When organizations start to think about and build an API first architecture, they can build new digital ecosystems and create new business value.

A digital ecosystem is a group of interconnected companies and products. This includes vendors, third party suppliers, customers, and applications.

A robust, well-connected, and multifaceted digital ecosystem enables businesses to create and monetize new digital experiences.

**Example 1: Walgreens**

Over the past decade, they embraced a culture of innovation. One service they historically provided was photo development from film. With the advent of digital cameras and then smartphones, consumer needs changed. People weren't bringing in film to be developed anymore.

Walgreens asked themselves, "How do we re-engage smartphone users with photo printing?" 

Walgreens built the photo printing API.

instead of only having create, edit, and share buttons for what an end user can do with their photo, there's also a print button that connects to any Walgreens store.

In this model, Walgreens is partnering with the developer community to serve customers in a new way. Walgreens treated the API as a product, not just a tool for integration.

**Example 2: Monex**
Monex couldn't upend their backend systems quick enough to deploy new services or even modify new ones. So, they developed an API to sabe them time and simplify processes of dveloping new products and services.


### Apigee
There's a widening gap between modern applications and legacy systems

Legacy systems like CRMs, ERPs, SOAs, databases, data warehouses, and data lakes provide businesses data but don't provide features and capabilities at the rate of change demanded by today's users. Modern applications on the other hand provide connected experiences and can be rapidly updated to meet user demands.

Applications that provide these connected experiences to end users must be able to do so securely and at scale.

Developers therefore need to manage the entire application lifecycle, connect to different backend systems, including the legacy ones, and be able to track and analyze the interactions between consumers, data, and service producers.

Also, the company's digital ecosystem becomes more complex, the required time and effort to manage hundreds of APIs securely and at scale becomes costly.

That's where Apigee comes in.

Apigee is a Google Cloud solution for developing and managing APIs. It includes an API Services layer that provides the runtime API gateway functionality, developer services, measuring and tracking services.

### Quizz
1. Apigee provides security policies for Michelle to manages her team's API.
1. A critical outcome of API management is measuring and tracking business performance.
1. The function of APIs is integration between systems.
1. Legacy systems struggle to meet modern consumer expectations because they scale slowly.
1. Businesses can use API to unlock value from their legacy system by gaining access to data stored in legacy systems.