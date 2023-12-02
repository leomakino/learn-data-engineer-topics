# Understanding Google Cloud Security and Operations
The course examines cost management, security, and operations in the cloud. First, it explores how businesses can choose to maintain some or none of their own infrastructure by purchasing IT services from a cloud provider. Next, it explains how the responsibility of data security is shared between the cloud provider and the business, and explores the defense-in-depth security built into Google Cloud. Finally, it covers how IT teams and business leaders need to rethink IT resource management in the cloud and how Google Cloud resource monitoring tools can help them to maintain control and visibility over their cloud environment.

Embracing cloud effectively requires a change in mindset in business operations. One important change is how tech and non-tech-adjacent teams operate.

## Financial Governance in the cloud
Leveraging cloud technology either for business improvements or for large-scale transformation doesn't come without some challenges. One of the common pain points many organizations face regardless of which cloud provider they use is managing cloud costs.

This includes anything from **planning and budgeting** for cloud resources to being able to **monitor and control** monthly spend to optimizing it as needed to accurately **forecasting** future costs.

Yesterday's solutions (Excel) for predicting and controlling costs don't work well in the cloud era.

Cloud technology can provide organizations with the means to make more dynamic decisions and accelerate innovation, but managing cloud costs requires vigilance and real-time monitoring in parallel.

Anyone can now access cloud resources on demand, managing IT infrastructure costs no longer sits mainly with the finance team. Instead, it involves more people across multiple teams.

Whatever your role, understanding how using cloud technology affects your business from a cost perspective will help you maximize the business value your organization gains from using the cloud.

### Fundamentals of cloud cost management
Operational expenditures (Opex) in practice with cloud, budgeting is no longer a one-time operational process completed anually. Infrastructure procurement has radically changed. Given the right permissions, almost any employee can spend up resources in seconds. Therefore, cloud resources must be monitored and controlled on an ongoing basis.

The ease of access to cloud resources brings it the need for more precise, real time control of what is being consumed.

Unpredictable costs, lack of visibility, and transparency into the cloud usage are among the top pain points when managing cloud enviroments.

Businesses usually waste over their estimates. They are underestimating their cloud financial waste.

Keeping costs within budget and limiting surprises were among the most critical cost management tasks.

The solution through three lenses:
- People
    - partnership accross finance, technology, and business functions is required. This partnership would consist of several experts who ensure that best practices are in place across the organization and there is visibility into the ongoing cloud spend.
- Process
    - What could resources are being used and by whom? 
    - What are the associated resource costs?
    - How do these costs measure against the broader business strategy?
- Technology - GCP brings its own native tools to help organizations monitor and manage their costs. The tools enable organizations to:
    - gain greater **visibility**;
    - drive a culture of **accountability** for cloud spending,
    - **control** costs to reduce the risk of overspending.
    - provide **intelligent** recommendations to optimize costs and usage.


It'll need a core team across technology, finance, and business functions to work together to make decisions in real time.

Through this close collaboration, they'll be able to control and optimize cloud costs on an ongoing basis.

### Total cost of ownership - TCO
In IT, the Total Cost of Ownership refers to a comprehensive assessment of all of the layers within the infrastructure. This includes:
1. user expenses, and the cost of service downtime.
1. communications
1. management and support
1. hardware and software

Historically, companies spent a substantial amount of money upfront to set up their IT infrastructure, the **capital expenditure** (capex) **would include**:
- paying for data center space and associated costs, such as power and cooling;
- storage systems,
- networking,
- hardware,
- software,
- security systems.
The TCO in this case would be the cost of setting up , managing, controlling, and optimizing every layer of the stack. In addition to the personnel required and skilled workers.

When organizations run their business using public cloud services, much of their capital expenditure no longer applies.

When organizations choose to keep some of their business running on-premises and some running on public cloud, the total cost of owneership for them would be more complex. TCO can vary depending on an organization's cloud adoptions goals.

Cloud, is not just about assessing cost savings. There are values the company gain over time, e.g.: cloud absorbs the effort that organizations traditionally put into hosting their applications or data on-premises, allowing the company to shift focus from maintaining status quo to higher value work. Examples of indirect values are: efficiency, reliability, and security.

Google Cloud provides tools to help monitor and control costs and maximize value. 

### Best practices for managing Google Cloud costs
1. Organizations need to identify the individual or team that manage costs. 
    - If it's a team, it should ideally be a mix of IT team managers and financial controlles
1. Learn the difference between invoices and cost tools.
    - Understand what kind information can be found in an invoice versus cost management tools.
    - An invoice and a Google Cloud tool are not the same thing
1. Use cost management tools for accountability
    - gain visibility, control, and intelligence.

An invoice contains how much the company is spending over a period of time.
Cost management tools are more effective for answering the why of the spendings.
    - It helps get more granular data, find trends, and identify actions.

Before organizations can optimize their cloud costs. They first need to understand:
1. what they're currently spending;
1. whether there are any trends;
1. what their forecasted costs are.

An organization needs to start capturing:
- what Cloud resources are being used, 
- by whom, 
- for what purpose, 
- and at what costs.

The organization also needs to think about:
- who is going to be responsible for monitoring this,
- who needs to be involved in managing costs, 
- how they will communicate the results or report on spending on an ongoing basis.

It's important to review the business priorities and establishing partnership between financial and IT teams, perhaps through a centralized team. Also, it's important to set up the cadence and format for ongoing communication with key cloud stakeholders.

The centralized team can use Google Cloud built-in reporting tools and create custom dashboards to gain greater visibility into their costs. The team should review these reports at least weekly.

Cloud spending is decentralized and variable. It's important to establish a culture of accountability for costs across the organization. Google Cloud offers flexible options to organize resources and allocate costs to individual departments and teams.

Defining clear ownership for projects and sharing cost views with the departments and teams that are using Cloud resources will help us establish this accountability culture and more responsible spending. This team should use these tools to regularly identify and report on cost inefficiencies.

In addition to making teams accountable for their spending, Google Cloud financial governance policies and permissions make it easy to control who has the ability to spend and view costs across your organization.

Creating budgets and alerts to notify key stakeholders when spending is getting off track, it is an important practice to keep costs under control.

Finally, organizations can make smart spending decisions with **intelligent** recommendations delivered by Google Cloud. It helps to:
- optimize usage,
- save time on management,
- minimize costs. 

An organization can see these recommendations which can easily be applied for immediate cost savings and greater efficiency.

### Quizz
1. Google Cloud's tools offer four key benefits for managing cloud costs: Visibility, accountability, control, intelligent recommendations.
1. Budgeting needs to be assessed on a daily, monthly, or weekly basis when a company starts using a service-based cloud architecture.
1. Creating a custom dashboard would give her and her teammates greater visibility into costs.
1. The primary factores that contribute to the complexity of calculating the TCO when migrating to the cloud are:
    - Cloud architecture
    - Qualified personnel
1. Sharing cost views with the departments that are exceeding their IT budgets promotes a culture of accountability.

## Security in the cloud
Organizations that adopt cloud technology will inevitably need to fundamentally change some of their business operations. A fundamental operational shift is about security.
From securing physical data centers to a global network, to private user data across the globe.

In this module, the course will examine a new cloud-first security model and explain how it differs from traditional on-premises IT security models

### Fundamental terms: Privacy, security, compliance and availabilty
Privacy:
- In the context of cloud technology, refers to the data an organization or an individual has access to and who they can share that data with.
- With traditional technology, an organization would store private data **on-premises**, where it feels safe because they generally know where it is and trust that it will be kept private.
- In the **cloud**, the private information is kept in a commercial storage facility. It's locked away just as before but now some of the control is relinquished to someone else.
- The facilities in the cloud have a strong security controls
- When moving data to the cloud, the facility and its employees only store or process the data. The data itself remains private.

Security:
- In the cloud refers to the policies, procedures, and controls put in place to keep data safe.

Compliance:
- It takes data security one step further. It's about meeting standards set by a third party. This third party might be a regulatory authority or might be an international standards organization.
- Especially important in highly regulated industries. Industries that there's abundance of sensitive data.

Availability:
- It refers to how much time the cloud service provider guarantees data and services are running or accessible.
- The availability of a service is typically documented as a percent of time per year. 
- 99.999% <-> 5 minutes unavailable per year; 

Google Cloud products terms:
1. You own your data, not Google;
1. Google dows not sell customer data to third parties. Neither for advertising;
1. All customer data is encrypted by default;
1. Google Cloud guards against insider access to your data. Insiders are only able to access customer data with their permission;
1. Google never give any government entity backdoor access to your data.
1. Google privacy practices are audited against international standards.

### Today's top cyber security challenges
Cyber Attack are bigger than never. Many groups, might use sophisticated methods to gain access to an organization's data.

Traditional on-premises systems or company own datacenters generally rely on perimeter-based security approach. The boundary around all of their data is protected by a firewall, for example, along with other security features. Once someone is inside that security perimeter, they're deemed trustworthy and therefore have access to everything.

In the cloud, each object is individually protected.

What are the common cybersecurity threats?
- Phishing attacks
    - attackers do research to gather information about you or anyone in your organization
    - Attackers craft highly targeted e-mails to trick people into thinking that the messages are genuine.
    - Employees can then be scammed into downloading malicious attachments, giving up their password, or sharing sensitive data.
- Physical damage
    - organizations can still be responsible for data losses even when there is damage to the physical hardware.
    - power losses or natural disasters, such as floods, fires, and earthquakes
- malware, viruses and ransomware attacks
    - Data can be lost, damaged, or destroyed by viruses or malware.
    - A set of files can be rendered unavailable to its intended users via ransomware until the ransom amount is paid.
- Unsecured third-party systems
    - Although third-party systems are often used to address common business needs like finance, inventory, or account management. Without adequate security measures and regular checks, these systems can pose a threat to data security.
- Misconfiguration
    - While this can be due to a lack of expert knowledge, even expert cloud engineers can misconfigure systems.
    - It is the single biggest threat to cloud security
    - This is why access should be limited following a least privilege zero trust model.

How do you defend against security threats that can come from anywhere, at anytime from anyone?

A perimeter security model is not enough anymore.

Leveraging cloud technology for your organization can dramatically strengthen your organization's ability to secure a data against newer and more sophisticated threats. A collaborative approach with your cloud provider is crucial to keeping your organization's data secure.

### Shared Responsability Model
When using cloud technology, the responsibility to secure data is shared between a business and the cloud provider.

When an organization adopts the cloud, the cloud service **provider** typically **becomes the data processor** and the **organization becomes the data controller**.

The cloud service provider manages the security of its infrastructure and its data centers and the customers gain the benefits of their infrastructure's security layers.

Google Cloud is responsible for securing the underlying infrastructure and the customer's core responsability is to secure access to data. It's is a partnership between the customer and the cloud provider.


Google's responsibility in the  the shared responsibility model: Google protects its infrastructure using the "defense in depth" approach. There is a layer upon a layer of security built into Google Cloud products and services. They are:
1. Operations
    - global team of more than 900 security experts monitor the system 24 hours a day, 365 days a year.
1. Network
    - all data moving into and out of Google's infrastructure is encrypted in transit.
    - Multi layers of defense are in place to help protect customers against network attacks like DDoS attacks.
1. Identity
    - operates a zero trust model. This means that every user and every machine that tries to access data or services must strongly authenticate at every stage for each file.
1. Storage
    - connected to the idea of data encryption at rest
    - Encryption at rest protects data when it's stored on physical media
    - When data is going to be stored on Google Cloud
        1. It's broken into many pieces (chunks) in memory
        1. These pieces are encrypted with their own data encryption key or DEK
        1. These data encryption keys are then encrypted a second time generating another key which we call a key encryption key or KEK.
        1. Encrypted chunks and wrapped encryption keys are distributed across Google's infrastructure.

1. Software
    - Titan microcontroller also verify the OS and the rest of the deploy software stack
1. Hardware
    - Google design its own servers, its storage, and its networking gear
    - Third parties never see the overall process
    - The hardware is housed in high security data centers
    - embedded chip called Titan checks the integrity of the machine.

organization's responsibility in the shared responsibility model: 

The old ways of securing data have to change. 

- Organizations need to reassess their existing security policies and practices and determine how to best use cloud products and solutions to maintain and potentially improve their security posture.
1. IT teams need to control data access, maintain visibility, and be prepared for incidents.
    - IT teams need to have a complete understanding of who can access what data
    - Establish granular access policies. In other words, to define who can do what and on what cloud resource.
    - Enable multi factor authentication to protect against phishing and other risks.
1. IT teams and business decision makers need to ensure that they have visibility into what's happening, who is accessing what data and when.
    - Logging and monitoring tools are used here
1. Manage a data breach
    - teams and business leaders need to have a plan in place to successfully deal with it
    - organizations need to have a culture that allows teams to work in stressful situations.
    - organizations need to be ready for what's coming; maintain operational readiness.

employees value convenience: 
- This means they often do things without keeping the security of their data top of mind.
- They write down simple passwords, plug infected USB flash drives into their computers, and delay software updates to avoid painfully long reboots.


### Identity and access management
Cloud Identity helps organizations control and manage access to resources in order to maintain the security and integrity of both data and systems.

An Identity Access Management policy, or IAM policy, is made of three parts:
- Who:
    - Can be a google account, a Google group, a service account, or a Google Workspace or Cloud Identity domain
- Can do what
    - It is defined by an IAM role
    - There are three kinds of roles in IAM: Basic, predefined and custom.
        - Basic: Owner, Editor, and Viewer
        - Predefined: sets of predefined roles that align with typical responsibilities of people using services. Each role is a collection of permissions.
        - Custom: Even more granular. manage the permissions to specific resources. This means that users get access only to what they need to do their job
- on which resource

Google Cloud recommends using a “least-privilege” model, in which each person in your organization is given the minimal amount of privilege needed to do their job.

### Resource hierarchy
Another facet to controlling and managing access is tied to the resource hierarchy. In other words, what resources users can access.

Managing files, folders, and resources for projects is very similar to how teams would use and manage Google Cloud services.

In the Cloud environment, a **project** is the basis for enabling and using Google Cloud capabilities

Any resources consumed by the project are connected to the project in the hierarchy.

Businesses usually have more than one Cloud project running, so projects can be organized into folders. A folder can contain projects, other folders, or combination of both.

This means projects can be grouped into a hierarchy. In other words, it is the way the IT team can organize their business's Google Cloud environment.

*a resource is any Google Cloud service, such as Compute Engine and BigQuery*

Start from the top, everything managed in Google Cloud is under a domain and an organization. It is like an umbrella.

Projects belong to the organization rather than the user who created them.

Projects are used for grouping Google Cloud resources.

Cloud **Billing** accounts live under the organization and track any charges for associated projects. Cloud Billing account users can associate projects and see spend, while Cloud Billing account administrators are able to unlink projects, set budgets, and contact billing support.

### Quiz
1. Google Cloud Identity does a strong authentication for data acess.
1. An Identity Access Management policy is made of: "Who", "can do what", "on which resource"
1. An e-mail saying: "We have identified that your account is vulnerable. Click this link to change your security settings" can bring cybersecurity risks such as Phishing for sensitive data and Malware attacks on files
1. A Google Cloud's principle for granting access to users is "Least privilege"


## Monitoring Cloud IT Services and Operations
Areas for operational change:
- Cost management
- Cybersecurity
- **Monitoring Cloud IT Services and Operations**

In this module, the course will explore the following topics:
1. IT Operational challenges
    - how IT teams are traditionally structured, and why that structure prevents organizations from quickly delivering updates to services or fresh customer experiences.
1. DevOps and Site Reliability Engineering
    - what DevOps and site reliability engineering are, and then use them as a framework for IT operational changes
1. Google resource monitoring tools
    - how they help organizations maintain control and visibility of their cloud environment.

### IT development and operations challenges
When a company wants to release updates to their webservice, they need to take their service offline while changes are being implemented.

Unexpected or prolonged downtime can be irritating for end users and costly for businesses, including from loss of customers.

Therefore, IT leaders want to avoid service downtime.

But service downtime is unavoidable for IT teams, and it's also a source of two operational challenges:
1. Developers agility
2. Operators reliability

Even though system updates are typically scheduled outside regular business hours, in today's global digital economy, service downtime can still be disruptive for some users. 

If a service disruption happens unexpectedly, this may be the result of a team structure issue where developers and operators are working in silos.

The structure of these teams restricts collaboration and obscures accountability.

**Developers** are responsible for writing code for systems and applications.
**Operators** are responsible for ensuring that those systems and applications operate reliably.

In the other hand, **developers** are expected to be agile and are often pushed to write and deploy code quickly. **Operators** are expected to keep system stable, and so they often prefer to work more slowly to ensure reliability and consistency.

Worse, accountability between the teams may be not always clear.

For organizations to thrive in the cloud, they need to adapt their IT operations in two ways.
1. Adjust their expectations for service availability from 100% to a lower percentage
1. Adopt best practices from the developer operations or DevOps, and site reliability engineering (SRE)

And so on, teams can be more agile and work more collaboratively with clearer accountability.

100% of service availability is misleading. In order to roll out updates, operators have to take a system offline and ensuring 100% service availability is also incredibly expensive. 

Cloud providers use standard practices to define and measure service availability for customers:
- Service Level Agreement (SLA);
    - It s a contractual commitment between the cloud service provider and the customer.
    - It provides the baseline level for the quality, availability and reliability of that service.
- Service Level Objectives (SLO);
    - It is a key element within the SLA.
    - It's the goal for the cloud service performance level.
    - it's shared between the cloud provider and a customer.
    - If service performance meets or exceeds the SLO, It means that end users, customers, and internal stakeholders are all happy.
    - If the service performance is below the SLO and above the SLA or baseline performance expectation, it does not directly affect the end user or end customer, but it does give the cloud provider the signal to reduce service outages and increase service reliability instead of pushing out new updates.
- Service Level Indicators (SLI).
    - It is a measure of the service provided.
    - It often include reliability and errors.
    - Involved with Error budget. It is the space between the SLA and the SLO.

An error budget is the amount of error that a service provider can accumulate over a certain period of time before end users start feeling unhappy. It is like a pain tolerance for end users.

By adjusting service performance expectations, with an SLA, SLO, SLIs, and error budgets, businesses can optimize their cloud environment and create better, more seamless customer experiences.

DevOps and site reliability help to adjust service availability expectations and improve their team's IT operations.


### DevOps and SRE
When an organization needs to adapt their operations, team structure. IT leaders can use best practices from DevOps and Site Reliability Engineering.

DevOps, or Developers Operations, is a philosophy that seeks to create a more collaborative and accountable culture within developer and operations teams. The philosophy highlights are:
1. Reduce Silos
    - Businesses can increase and foster collaboration by breaking down barriers across teams.
    - the importance of establishing shared ownership of production between developers and operations to meet DevOps objective
1. Accept failures as normal
    - leaders can't expect perfect execution.
1. Implement gradual change
    - Small incremental changes are easier to review and in the event that a gradual change does release a bug in production, it allows teams to reduce their time to recover, making it simple to roll back.
1. Leverage tooling and automation
    - Identifying manual work that can be automated is key to working efficiently and focusing on the tasks that matter.
1. Measure everthing
    - measurement is a critical gauge for success
    - There's no way to tell whether what you're doing is successful if you have no way to measure it.

While **DevOps** is a **conceptual approach** to a collaborative and accountable data culture, **SRE** is about the **practical implementation** of that philosophy.

Site Reliability Engineering, or SRE, is a discipline that applies aspects of software engineering to operations. The goals of SRE are to create ultra-scalable and highly reliable software systems. The SRE best practices are aligned with the five objectives of DevOps cited above.
1. Reduce Silos
    - Developers and Operations, together, they define service level objectives, or SLOS, calculate error budgets, and determine reliability and order work priorities.
    - the shared ownership promotes shared vision and knowledge and the need for improved collaboration and communications.
1. Accept failures as normal
    - One way this is done is by holding a blameless 'lessons learned' discussion after an incident occurs.
    - This practice helps SREs improve their understanding of system failures in order to identify preventative actions and ultimately reduce the likelihood or impact of a similar incident.
1. Implement gradual change
    - SREs aim to reduce the cost of failure by rolling out changes to a small percentage of users first.
    - Culturally, this promotes more prototyping and launching iteratively.
1. Leverage tooling and automation
    - SREs focus on increasing efficiency through toil automation. Toil is a type of work that is tied to running a production service.
    - Toil automation therefore reduces the amount of manual repetitive work.
1. Measure everthing
    - tracking everything related to toil, reliability and system health.

To foster these practices, organizations need a culture of goal setting, transparency, and data-driven decision making. They also need the tools to monitor their cloud environment and to identify whether they're meeting their service level objectives.

SRE shifts the mindset from 100% availability to 99.99%. This means that updates are pushed out iteratively and continually, but only require seconds or minutes of downtime.

DevOps and SRE have the same intended outcome: designed to break down organizational barriers to help deliver better customer experiences faster.

### Quiz
1. the expectation for 100% service availability is misleading because service maintenance is inevitable and requires downtime
1. Site reliability engineering (SRE) refers to breaking down silos and closing gaps between developer and operations teams
1. Service Level Objective (SLO) is the goal for your cloud service performance level.


