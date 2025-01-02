# Elastic Google Cloud Infrastructure: Scaling and Automation
This course explores and deploys solution elements, including securely interconnecting networks, load balancing, autoscaling, infrastructure automation and managed services.

## Interconnecting Network
Different applications and workloads require different network connectivity solutions. Google supports multiple ways to connect your infrastructure to GCP. This module focus on GCP's hybrid connectivity products, which Cloud VPN, Cloud Interconnect, and Peering

### Cloud VPN
Google Cloud offers two types of Cloud VPN gateways:
1. HA VPN
1. Classic VPN

*All Cloud VPN gateways created before the introduction of HA VPN are considered Classic VPN gateways.*

Classic VPN:
- securely connects your on-premises network to your Google Cloud VPC network through an IPsec VPN tunnel.
- Traffic traveling between the two networks is encrypted by one VPN gateway, then decrypted by the other VPN gateway.
- This protects your data as it travels over the public internet, and that’s why **Classic VPN is useful for low-volume data connections**.
- supports site-to-site VPN, static and dynamic routes, and IKEv1 and IKEv2 ciphers.
- doesn't support use cases where client computers need to “dial in” to a VPN using client VPN software.


In order to connect to your on-premises network and its resources, you need to configure your Cloud VPN gateway, on-premises VPN gateway, and two VPN tunnels.
- Cloud VPN gateway is a regional resource that uses a regional external IP address.
- on-premises VPN gateway can be a physical device in your data center or a physical or software-based VPN offering in another cloud provider's network. This VPN gateway also has an external IP address.
- A VPN tunnel then connects your VPN gateways (In order to create a connection between two VPN gateways, you must establish two VPN tunnels.)
- Each tunnel defines the connection from the perspective of its gateway, and traffic can only pass when the pair of tunnels is established.
- the maximum transmission unit, or **MTU**, for your on-premises VPN gateway **cannot be greater than 1460 bytes**.

HA VPN:
- securely connect your on-premises network to your Virtual Private Cloud (VPC) network through an IPsec VPN connection in a single region.
- provides an SLA of 99.99% service availability. To guarantee a 99.99% availability SLA for HA VPN connections, you must properly configure two or four tunnels
- When you create an HA VPN gateway, Google Cloud automatically chooses two external IP addresses, one for each of its fixed number of two interfaces.
- Each of the HA VPN gateway interfaces supports multiple tunnels.
- You can also create multiple HA VPN gateways.
- You can configure an HA VPN gateway with only one active interface and one external IP address; But this don't provide a 99,99% availability anymore.
- VPN tunnels connected to HA VPN gateways must use dynamic (BGP) routing.
- supports site-to-site VPN in one of the following recommended topologies or configuration scenarios: 
    - An HA VPN gateway to peer VPN devices 
    - An HA VPN gateway to an AWS virtual private gateway
    - Two HA VPN gateways connected to each other

There are three typical peer *gateway configurations* for HA VPN.
1. An HA VPN gateway to two separate peer VPN devices
    - Each peer device has one interface and one external IP address.
    - The HA VPN gateway uses two tunnels, one tunnel to each peer device.
    - provides redundancy and failover
    - A second physical gateway lets you take one of the gateways offline for software upgrades or other scheduled maintenance.
    - the REDUNDANCY_TYPE for this configuration takes the value **TWO_IPS_REDUNDANCY**.
1. An HA VPN gateway to one peer VPN device that uses two separate IP addresses
    - E.g. Two tunnels from one AWS virtual private gateway to one interface of the HA VPN gateway, and two tunnels from the other AWS virtual private gateway to the other interface of the HA VPN gateway.
1. An HA VPN gateway to one peer VPN device that uses one IP address

In order to use dynamic routes, you need to configure Cloud Routers.
- Cloud Router can manage routes for a Cloud VPN tunnel using Border Gateway Protocol, or BGP.
- *This routing method (BGP) allows for routes to be updated and exchanged without changing the tunnel configuration.*
- To automatically propagate network configuration changes, the VPN tunnel uses Cloud Router to establish a BGP session between the VPC and the on-premises VPN gateway, which must support BGP. Instances in the new subnets can start sending and receiving traffic immediately

### Configuring Google Cloud HA VPN
In this lab, you learn how to perform the following tasks:

- Create two VPC networks and instances.
- Configure HA VPN gateways.
- Configure dynamic routing with VPN tunnels.
- Configure global dynamic routing mode.
- Verify and test HA VPN gateway configuration.

#### Set up a Global VPC environment
- create a VPC network called vpc-demo: `gcloud compute networks create vpc-demo --subnet-mode custom`
- create subnet: 
```
gcloud compute networks subnets create vpc-demo-subnet1 \
--network vpc-demo --range 10.1.1.0/24 --region "REGION"
```
- Create a firewall rule to allow all custom traffic within the network:
```
gcloud compute firewall-rules create vpc-demo-allow-custom \
  --network vpc-demo \
  --allow tcp:0-65535,udp:0-65535,icmp \
  --source-ranges 10.0.0.0/8
```
- Create a firewall rule to allow SSH, ICMP traffic from anywhere
```
gcloud compute firewall-rules create vpc-demo-allow-ssh-icmp \
    --network vpc-demo \
    --allow tcp:22,icmp
```

#### Set up an HA VPN gateway
- create an HA VPN in the vpc-demo network: `gcloud compute vpn-gateways create vpc-demo-vpn-gw1 --network vpc-demo --region "REGION"`
- Describe: `gcloud compute vpn-gateways describe vpc-demo-vpn-gw1 --region "REGION"`
- Create a cloud router in the vpc-demo network: 
```
gcloud compute routers create vpc-demo-router1 \
    --region "REGION" \
    --network vpc-demo \
    --asn 65001
```

#### Create two VPN tunnels
- Create the first VPN tunnel in the vpc-demo network
```
gcloud compute vpn-tunnels create vpc-demo-tunnel0 \
    --peer-gcp-gateway on-prem-vpn-gw1 \
    --region "REGION" \
    --ike-version 2 \
    --shared-secret [SHARED_SECRET] \
    --router vpc-demo-router1 \
    --vpn-gateway vpc-demo-vpn-gw1 \
    --interface 0
```

#### Create Border Gateway Protocol (BGP) peering for each tunnel
- Create the router interface for tunnel0 in network vpc-demo:
```
gcloud compute routers add-interface vpc-demo-router1 \
    --interface-name if-tunnel0-to-on-prem \
    --ip-address 169.254.0.1 \
    --mask-length 30 \
    --vpn-tunnel vpc-demo-tunnel0 \
    --region "REGION"
```
- Create the BGP peer for tunnel0 in network vpc-demo:
```
gcloud compute routers add-bgp-peer vpc-demo-router1 \
    --peer-name bgp-on-prem-tunnel0 \
    --interface if-tunnel0-to-on-prem \
    --peer-ip-address 169.254.0.2 \
    --peer-asn 65002 \
    --region "REGION"
```

## Load Balancing and Autoscaling
## Infrastructure Automation
## Managed Services