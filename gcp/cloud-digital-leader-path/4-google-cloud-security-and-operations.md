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

## Monitoring Cloud IT Services and Operations
