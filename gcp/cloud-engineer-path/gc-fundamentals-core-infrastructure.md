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
    


