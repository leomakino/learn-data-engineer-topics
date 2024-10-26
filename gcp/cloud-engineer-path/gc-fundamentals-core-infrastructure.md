# Google Cloud Fundamentals: Core Infrastructure
Google Cloud Fundamentals: Core Infrastructure introduces important concepts and terminology for working with Google Cloud. it compares many of Google Cloud's computing and storage services, along with important resource and policy management tools.

## Introducing Google Cloud
Iaas offerings provide:
- raw compute
- storage
- network capabilities

The Google Cloud network is the largest network of its kind, and Google has invested billions of dollars over many years to build it. This network is designed to give customers the highest possible throughput and lowest possible latencies for their applications by leveraging more than 100 content caching nodes worldwide. Google Cloud’s locations underpin all of the important work we do for our customers. From redundant cloud regions to high-bandwidth connectivity via subsea cables, every aspect of our infrastructure is designed to deliver your services to your users, no matter where they are around the world.


Google Cloud’s infrastructure is based in five major geographic locations: 
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
    - Google’s services communicate with each other using RPC calls (cryptographic privacy and integrity for remote procedure)
1. User identity layer
    - manifests to end users as the Google login page
    - it goes beyond asking for a simple username and password
1. Storage services layer
    - Encryption at rest
1. Internet communication layer
    - Google Front End (GFE): ensures that all TLS connections are ended using a public-private key pair and an X.509 certificate autority (CA)
    - Denial of Service (DoS) protection: Google has multi-tier, multi-layer DoS protections
1. Operational security layer
    - Intrusion detection: Rules and machine intelligence give Google’s operational security teams warnings of possible incidents.
    - Reducing insider risk: Google aggressively limits and actively monitors the activities of employees who have been granted administrative access to the infrastructure.
    - Employee Universal Second Factor (U2F) use: To guard against phishing attacks against Google employees, employee accounts require use of U2F-compatible Security Keys.
    - Software development practices: Google employs central source control and requires two-party review of new code.
    

## Resources and Access in the Cloud
### Resource Hierarchy
The resource hierarchy directly relates to how policies are managed and applied on Google Cloud.

Policies can be defined at the project, folder, and organization node levels. Some Google Cloud services allow policies to be applied to individual resources, too. Policies are also inherited downward.


Google Cloud’s Resource Manager tool is designed to programmatically help you manage projects. It’s an API that can gather a list of all the projects associated with an account, create new projects, update existing projects, and delete projects.

How a new organization node is created depends on whether your company is also a Google Workspace customer. If you have a Workspace domain, Google Cloud projects will automatically belong to your organization node. Otherwise, you can use Cloud Identity, Google’s identity, access, application, and endpoint management platform, to generate one.

### IAM
Otherwise, you can use Cloud Identity, Google’s identity, access, application, and endpoint management platform, to generate one.

A “who” is also called a “principal.” Each principal has its own identifier, usually an email address.


You can define deny rules that prevent certain principals from using certain permissions, regardless of the roles they're granted. This is because IAM always checks relevant deny policies before checking relevant allow policies. Deny policies, like allow policies, are inherited through the resource hierarchy.


There are three kinds of roles in IAM: 
1. basic, 
1. predefined, and 
1. custom.

Basic roles include:
- viewer: can access resources but can’t make changes.
- editor: can access and make changes to a resource
- owner: access and make changes to a resource; can manage the associated roles and permissions and set up billing
- billing administrator: control the billing for a project but not be able to change the resources in the project


Custom roles will allow you to define those exact permissions. Two important details about custom roles:
- need to manage the permissions that define the custom role you’ve created.
- it can only be applied to either the project level or organization level.

### Cloud Identity
With Cloud Identity, organizations can define policies and manage their users and groups using the Google Admin Console.
