# Trust and Security with Google Cloud
This course explores the basics of cloud security, the value of Google Cloud's multilayered approach.

Trust and security lie at the heart of our product design and development philosophy. Security is a dynamic and ongoing process that demands constant attention and investment.

This course presents a range of security products and services that enable organizations to detect, investigate, and mitigate cyber threats while aligning with your policy, regulatory, and business objectives.

## Trust and Security in the cloud
In the field of cloud security, understanding the terminology is crucial to navigating the landscape effectively.

Concepts related to reducing the risk of **unauthorized access** to sensitive data:
1. **Privileged access**: is a security model that grants specific users access to broader set of resources than ordinary users.
1. **Least privilege**: security principle advocates granting users only the access they need to perform their job responsibilities. By providing the minimum required access, organizations can reduce the risk of unauthorized access to sensitive data.
1. **Zero-trust architecture**: security model assumes that no user or device can be trusted by default. It also helps ensure robust security by implementing strict access controls and continuously verifying user identities.

Concepts relate to how an organization can **protect itself from cyber threats**:
1. **Security by default**:  is a principle that emphasizes integrating security measures into systems and applications from the initial stages of development. By prioritizing security throughout the entire process, organizations can establish a strong security foundation in their cloud environments.
1. **Security posture**: refers to the overall security status of a cloud environment. It indicates how well an organization is prepared to defend against cyber attacks by evaluating their security controls, policies, and practices.
1. **Cyber resilience**: refers to an organization's ability to withstand and recover quickly from cyber attacks. It involves identifying, assessing, and mitigating risks, responding to incidents effectively, and recovering from disruptions quickly.

Essential **security measures**:
- **firewall**: is a network device that regulates traffic based on predefined security rules. It follows certain rules to decide which traffic is allowed to enter or leave a network. These rules help keep unauthorized people or harmful things away from important cloud resources, such as servers, databases, and applications.
- **Encryption**: is the process of converting data into an unreadable format by using an encryption algorithm.
- **Decryption**: is the reverse process that uses an encryption key to restore encrypted data back to its original form.


Three essential aspects of security, components that make up a cloud security: 
1. **Confidentiality**: is about keeping important information safe and secret. 
    - It ensures that *only authorized people* can access sensitive data, no matter where it's stored or sent.
    - Encryption plays a crucial role in ensuring confidentiality in the cloud.
1. **Integrity**: means keeping data accurate and trustworthy.
    - It ensures that information doesn't get changed or corrupted, no matter where it's stored or how it's moved around.
    - a message doesn't get altered during delivery.
    - data integrity controls: checksums or digital signatures.
    - Prevents unauthorized modifications or tampering,
1. **Availability**: systems and services are accessible and ready for use by the right people when needed.

By understanding and implementing measures to address these aspects, organizations can establish a strong security framework to safeguard their digital assets.

**Control** refers to the measures and processes implemented to manage and mitigate security risks. It involves establishing policies, procedures, and technical safeguards to protect against unauthorized access, misuse, and potential threats. Also, implementing robust authentication mechanisms, access restrictions, and security awareness training.


**Compliance** relates to adhering to industry regulations, legal requirements, and organizational policies. It involves ensuring that security practices and measures align with established standards and guidelines. It demonstrates an organization's commitment to data privacy and security, building trust with stakeholders, and minimizing legal and financial risks.

Cloud security involves hosting and managing data and applications in off-site data centers operated by cloud service providers. The responsibility for securing the infrastructure and underlying hardware lies with the cloud provider.

The customer is typically responsible for securing their data, applications, user access, and configurations.

Differencies between cloud security and on-premises security:
- location
- responsibility
- scalability
- maintenance and updates
- capital expenditure

Common cybersecurity threats faced by organizations:
1. **Deceptive social engineering**: phishing attacks.
1. **physical damage**
1. **malware, viruses, and ransomware**
1. **vulnerable third-party systems**
1. **configuration mishaps**: most prominent threat to cloud security.

## Google's Trusted Infrastructure
Google multilayered strategy builds progressive security layers, combining global data centers, purpose-built servers, custom security hardware and software, and two-step authentication. This approach provides true defense-in-depth.

Google Data centers are more than just facilities filled with computers. They meticulously designed to deliver exceptional reliability, top-notch security, and outstanding efficiency, and availability. The security principles (zero-trust architecture, least privilege and security by defaut) are also implemented. Moreover, there are efficiency, Power Usage Effectiveness (PUE) and Scalability.

When data is at rest, it's stored on physical devices like computers or servers. Google Cloud, automatically encrypt all customer content at rest, but if you prefer to manage your encryption keys yourself, you can use our Cloud Key Management Service (Cloud KMS) for added control.

Encrypting data in use adds another layer of protection, especially against unauthorized users who might physically access the computer. Google uses a technique called memory encryption, which locks your data inside the computer's memory

When it comes to encryption algorithms, the Advanced Encryption Standard (AES) takes center stage. AES is a powerful encryption algorithm trusted by governments and businesses worldwide.

Whether your data is resting, traveling, or actively in use, encryption acts as your loyal guardian, because it ensures its confidentiality and protection.


In cloud identity management, there are the three A’s 
- authentication: it verifies the identity of users or systems that seek access using a unique credentials.
    - two-factor authentication or multi-factor authentication, is a security feature that adds an extra layer of protection
- authorization: determine what that user or system is allowed to do within the system.
- auditing/accounting: monitoring and tracking user activities within a system

With IAM, the admin can:
- create and manage user accounts;
- assign roles to users;
- grant and revoke permissions to resources;
- **audit user activity**;
- **monitor your security position**.

Network security:
- zero trust;
    - Google Cloud's BeyondCorp Enterprise.
- secure connectivity across these environments;
    - Cloud VPN and Cloud Interconnect to establish secure connections between your on-premises networks and Google Cloud resources
- secure your perimeter:
    - Google Firewall and Virtual Private Cloud (VPC)
    - Shared VPC to separates each Google Cloud Project and work independently and safely
- External web applications and services are often targeted by cyber threats,
    - Google Cloud Armor comes to the rescue by providing robust DDoS protection.
- Automate infrastructure provisioning for enhanced security.
    - Create immutable infrastructure with Terraform, Jenkins, and Cloud Build
    - It becomes a well-designed workspace

Security Operations (SecOps):
- is about protecting your organization's data and systems in the cloud.
- It involves a combination of processes and technologies that help reduce the risk of data breaches, system outages, and other security incidents.

SecOps essential activities:
- **Vulnerability management**: process of identifying and fixing security vulnerabilities in cloud infrastructure and applications. 
It’s like regularly checking.
    - Google Cloud's Security Command Center (SCC) provides a centralized view of the security posture.
- **Log management**: Cloud Logging allows to analyze security logs from your entire Google Cloud environment.
- **Incident response**: being prepared for security incidents;
    - Google Cloud has expert incident responders across various domains, who are equipped with the knowledge and tools to tackle any security incident swiftly and effectively.
- **Education**: educating the employees on security best practices. Prevent incidents by raising awareness and empowering employees to protect themselves and the organization

SecOps Benefits:
- **Reduced risk of data breaches**;
- **Increased uptime**: A swift and effective incident response minimizes the impact of outages on your business operations, which ensures smoother and uninterrupted services;
- **Improved compliance**;
- **Enhanced employee productivity**: minimizes the risk of human error and promotes a more secure and productive work environment.

## Google Cloud's Trust Principles and Compliance
Google’s seven trust principles:
1. You own your data, not Google.
2. Google does not sell customer data to third parties.
3. Google Cloud does not use customer data for advertising.
4. All customer data is encrypted by default.
5. We guard against insider access to your data.
6. We never give any government entity "backdoor" access.
7. Our privacy practices are audited against international standards.

Transparency Reports and Independent Audits Transparency are a core element of our commitment to trust. Additionally, Google Cloud undergoes independent, third-party audits and certifications.


About storing data and keeping it secure:
- **Data sovereignty**: refers to the legal concept that data is subject to the laws and regulations of the country where it resides.
- **Data residency**: refers to the physical location where data is stored or processed

Google Cloud addresses data residency requirements offering a range of options to control the physical location of your data through regions. Additionally, Google Cloud provides Organization Policy constraints, coupled with IAM configuration, to prevent accidental data storage in the wrong region. Furthermore, Google Cloud offers features like VPC Service Controls, which let you restrict network access to data based on defined perimeters. Google Cloud Armor lets you restrict traffic locations for your external load balancer by adding an extra layer of protection. By using these capabilities, organizations can adhere to data residency and data sovereignty requirements.

Compliance is a critical aspect of the cloud journey, because not meeting regulatory obligations can have far-reaching consequences. Google Cloud offers robust resources and tools tailored to support it
- **Google Cloud Compliance Resource Center**: provides detailed information on the certifications and compliance standards Google satisfy. It is your go-to source for actionable information and support.
- **Compliance Reports Manager**: this platform offers easy, on-demand access to critical compliance resources at no extra cost. It provide evidence of Google adherence to rigorous compliance standards

By using the Google Cloud compliance resource center and the Compliance Reports Manager, you can navigate the complex realm of industry and regional compliance with confidence.