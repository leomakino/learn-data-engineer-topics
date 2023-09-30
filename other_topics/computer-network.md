# Computer Network

## Data transmission modes
- Simplex: One direction
- Half-Duplex: Each station can both transmit and receive but not at the same time
- FUll-Duplex: both stations can transmit and receive simultaneously

## Network topology
Network topologies are categorized as either a physical network topology or logical network topology. The physical topology of a network is the physical layout of nodes and connections. Logical network topologies define how a network is set up, including which nodes connect and how, as well as the pattern of data transfers.

Types of topologies: 
- **Bus network**: every node is connected in series along a single cable
- **Star network**: a central device connects to all other nodes through a central hub. 
- **Ring network**: the nodes are connected in a closed-loop configuration.
- **Mesh Network**: The mesh network topology links nodes with connections so that multiple paths between at least some points of the network are available.
- **Tree Network**: The tree network topology consists of one root node, and all other nodes are connected in a hierarchy
- **Hybrid Network**: The hybrid network topology is any combination of two or more topologies.

## Structured cabling
Structured cabling is the design and installation of a cabling system that will support multiple hardware uses and be suitable for today's needs and those of the future. 

## IEE 802 (Layers 1 and 2 OSI)
It is a family of Institute of Electrical and Electronics Engineers (IEEE) standards for local area networks (LAN), personal area network (PAN), and metropolitan area networks (MAN). The IEEE 802 standards are restricted to computer networks.
The services and protocols specified in IEEE 802 map to the lower two layers (data link and physical) of the seven-layer Open Systems Interconnection (OSI) networking reference model. IEEE 802 divides the OSI data link layer into two sub-layers: logical link control (LLC) and medium access control (MAC).

The most widely used standards are for Ethernet, Bridging and Virtual Bridged LANs, Wireless LAN, Wireless PAN, Wireless MAN.

IEEE 802.1 - Higher Layer LAN Protocols Working Group
IEEE 802.3 - Ethernet (wired computer networking technologies commonly used in local area networks (LAN), metropolitan area networks (MAN) and wide area networks (WAN))

IEEE 802.11 - Wireless LAN (WLAN) & Mesh (Wi-Fi certification)

## TCP/IP and UDP (Layers 3 and 4 OSI)
It is a framework for organizing the set of communication protocols used in the Internet and similar computer networks according to functional criteria.

The foundational protocols in the suite are the Transmission Control Protocol (TCP), the User Datagram Protocol (UDP), and the Internet Protocol (IP).

TCP/IP addresses a port number and an IP address for each separate piece of equipment connected to a network.

## Application layer protocols (Layer 7 OSI)
An application layer is an abstraction layer that specifies the shared communication protocols and interface methods used by hosts in a communications network.

It is the layer through which users interact. It provides services to the user.

Application Layer Protocol in Computer Network:
- FTP (File Transfer Protocol): promotes sharing of files via remote computers with reliable and efficient data transfer
- SSH (Secure Shell): is a cryptographic network protocol for operating network services securely over an unsecured network.[1] Its most notable applications are remote login and command-line execution. 
- DNS (Domain Name Services):  is a hierarchical and distributed naming system for computers, services, and other resources in the Internet or other Internet Protocol (IP) networks. It associates various information with domain names (identification strings) assigned to each of the associated entities.
- SMTP (Simple Mail Transfer Protocol):  moves your email on and across networks
- POP (Post Office Protocol): used by User agents for message retrieval from mail servers. Together with IMAP, it is one of the most common protocols for email retrieval. 
- IMAP (Internet Message Access Protocol): is an Internet standard protocol used by email clients to retrieve email messages from a mail server over a TCP/IP connection.
- HTTPS (Hypertext Transfer Protocol Secure):   is an extension of the Hypertext Transfer Protocol (HTTP). It uses encryption for secure communication over a computer network, and is widely used on the Internet.
- HTTP: model for distributed, collaborative, hypermedia information systems.[1] HTTP is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks to other resources that the user can easily access.
- SSL (Secure Sockets Layer): encryption-based Internet security protocol. SSL is the predecessor to the modern TLS encryption used today.
- RDP (Remote Desktop Protocol):  provides a user with a graphical interface to connect to another computer over a network connection.
- DHCP (Dynamic Host Configuration Protocol): for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture.
## Encapsulation
Encapsulation is used to provide abstraction of protocols and services. Encapsulation is usually aligned with the division of the protocol suite into layers of general functionality. In general, an application (the highest level of the model) uses a set of protocols to send its data down the layers. The data is further encapsulated at each level. 