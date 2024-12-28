# Essential Google Cloud Infrastructure: Core Services

## IAM
Cloud IAM is a sophisticated system built on top of email-like address names, job type roles in granular permissions.

IAM objects:
- Organization
- Folders
- Projects
- Resources
- Roles
- Members

Organization admin has access to administer all resources belonging to his organization, which is useful for auditing.


### Roles
Roles, three types in Cloud IAM:
- basic roles
    - it offers fixed, coarse-grained levels of access.
    - owner
        - invite members
        - Remove members
        - Delete projects... 
    - editor
        - Deploy applications
        - Modify code
        - Configure services...
    - viewer
        - Read-only access
    - billing administrator
        - manage billing 
        - add or remove administrators without the right to change the resources in the project.
- predefined roles
    - GCP services, offers their own set of predefined roles, and they define where the roles can be applied.
    - These roles are a collection of permissions, because to do any meaningful operations, you usually need more than one permission.
- and custom roles.

*The owner role includes the permissions of the editor role. the editor role includes the permissions of the viewer role*

### Members
There are five different types of members: Google Accounts, Service Accounts, Google Groups, Google Workspace domains, and Cloud Identity domains.

---

Google account:
- represents a developer, an administrator, or any other person who interacts with Google Cloud
- Any email address that is associated with a Google account can be an identity, including gmail.com or other domains.

Service Accounts:
- It is an account that belongs to an application instead of to an individual end user.
- You can create as many service accounts as needed to represent the different logical components of your application.

Google Groups
- collection of Google accounts and service accounts.
- Every group has a unique email address that is associated with the group.
- Google groups are a convenient way to apply an access policy to a collection of users.

Workspace domains:
- represents a virtual group of all the Google accounts that have been created in an organization's Workspace account.

Cloud Identity domains
- lets you manage users and groups using the Google Admin Console, but you do not pay for or receive Workspace’s collaboration products such as Gmail, Docs, Drive, and Calendar.

---

A **policy** consists of a list of bindings. A binding binds a list of members to a role, 

A policy is a collection of access statements attached to a resource. Each policy contains a set of roles and role members, with resources inheriting policies from their parent. The IAM policy hierarchy always follows the same path as the Google Cloud resource hierarchy, which means that if you change the resource hierarchy, the policy hierarchy also changes. *For example, moving a project into a different organization will update the project's IAM policy to inherit from the new organization's IAM policy.* Child policies cannot restrict access granted at the parent level.

A **role** is a named list of permissions defined by IAM.

Recommender identifies excess permissions using policy insights.

**IAM deny policies**
Deny rules prevent certain principals from using certain permissions, refardless of the roles they're granted. Deny policies are made up of deny rules. Each deny rule specifies:
- A set of principals that are denied permissions
- The permissions that the principals are denied, or unable to use
- Optional: The condition that must be true for the permission to be denied

When a principal is denied a permission, they can't do anything that requires that permission.

**IAM always checks relevant deny policies before checking relevant allow policies.**

IAM Conditions allow you to define and enforce conditional, attribute-based access control for Google Cloud resources. With IAM Conditions, you can choose to grant resource access to identities (members) only if configured conditions are met. Conditions are specified in the role bindings of a resource's IAM policy.

An organization policy is:
- A configuration of restrictions
- It lets you constrain access to resources at and below the organization, folder or project.
- Defined by configuring a constraint with desired restrictions
- An organization policy can be applied to the organization node, and all of its folders or projects within that node.

What if I already have a different corporate directory?
A: Google Cloud Directory Sync

### Service Accounts
It provides an identity for carrying out service-to-service interactions in a project without supplying user credentials.

There are three types of service accounts: 
1. user-created or custom,
1. built-in, and 
1. Google APIs service accounts.

Apart from the default service account, all projects come with a Google Cloud APIs service account, identifiable by the email: project-number@cloudservices.gserviceaccount.com.

You can also start an instance with a custom service account.

Custom service accounts provide more flexibility than the default service account, but they require more management from you.

The default Compute Engine service account is identifiable by the email project-number-compute@developer.gserviceaccount.com, and it is automatically granted the Editor role on the project.

Authorization is the process of determining what permissions an authenticated identity has on a set of specified resources.

Scopes are used to determine whether an authenticated identity is authorized.

Service accounts are convenient when you're not accessing user data. 

Roles for service accounts can also be assigned to groups or users. You treat a service account as the resource, and decide who can use it by providing users or a group with the Service Account User role. This allows those users to act as that service account to perform permissions.

There are two types of service account keys:
- Google-managed service accounts
    - All service accounts have Google-managed keys
    - Google stores both the public and private portion of the key
    - Each public key can be used for signing for a maximum of two weeks
    - Private keys are never directly accessible. 
- User-managed service accounts
    - Google only stores the public portion of a user-managed key
    - Users are responsible for private key security
    - Can create up to 10 user-managed service accounts keys per service
    - Can be administered via the IAM API, gcloud, or the console

By default, when using service accounts within Google Cloud, Google automatically manages the keys for service accounts. However, if you want to be able to use service accounts outside of Google Cloud, it is possible to also manually create and manage your own service account keys.

With Google-managed service account keys, Google stores both the public and private portion of the key, and rotates them regularly. Your private key is always held securely in escrow and is never directly accessible.

You may optionally create one or more user-managed key pairs (also known as **"external" keys**) that can be used from outside of Google Cloud. Google only stores the public portion of a user-managed key. The User is responsible for security of the private key and performing other management operations such as key rotation, whether manually or programmatically. Google does not save your user-managed private keys, so if you lose them, Google cannot help you recover them. 

User-managed keys should be used as a last resort. Consider the other alternatives, such as short-lived service account credentials (tokens), or service account impersonation.

### Organization Restrictions
The Organization Restrictions feature lets you prevent data exfiltration through phishing or insider attacks. It restricts access only to resources in authorized Google Cloud organizations.

Employees of an organization use a managed device to access the organization resources. The managed device is governed by the organizational policies of a company. An egress proxy administrator configures the proxy to add organization restrictions headers to any requests originating from a managed device. This proxy configuration prevents users from accessing any Google Cloud resources in non-authorized Google Cloud organization.

The Organization Restrictions feature in Google Cloud inspects all requests for organization restrictions header, and allows or denies the requests based on the organization being accessed.

Organization Restrictions can be used to restrict access to employees in your organization so that employees can access resources only in your Google Cloud organization and not other organizations.

They can also be used to allow your employees to read from Cloud Storage resources but restrict employee access only to resources in your Google Cloud organization. Or, allow your employees to access a vendor Google Cloud organization in addition to your Google Cloud organization.

### IAM best practices
Hierarchy:
- Check the policy granted on each resource and make sure you recognize the inheritance. 
- Because of inheritance, use the principle of least privilege when granting roles.
- Audit policies in Cloud Audit Logs: setiampolicy
- Audit membership of groups used in policies

Grant roles:
- Grant roles to groups instead of individuals. This allows you to update group membership instead of changing a Cloud IAM policy. - make sure to audit membership of groups used in policies and control the ownership of the Google group used in Cloud IAM policies.
- Example: Network Admin Group containing the (i) Group needing view only role and (ii) Group needing read_write only role
- groups are not only associated with job roles but can exist for the purpose of role assignment.

Service Accounts
- be very careful when granting the *service accounts user role* because it provides access to all the resources of the service account has access to.
- when you create a service account give it a display name that clearly identifies its purpose, ideally using an established naming convention.
-  establish key rotation policies and methods and audit keys with the serviceAccount.keys.list method.
- Use Cloud Identity Aware Proxy or Cloud IAP.

Cloud IAP lets you establish a central authorization layer for applications accessed by HTTPS. So you can use an application level access control model instead of relying on network level firewalls. Applications and resources protected by Cloud IAP can only be accessed through the proxy by users and groups with the correct Cloud IAM role.

When you grant a user access to an application or resource by Cloud IAP. They are subject to the fine-grained access controls implemented by the product in use without requiring a VPN. Cloud IAP performs authentication and authorization checks when a user tries to access a Cloud IAP secure resource.

What abstraction is primarily used to administer user access in IAM ? Roles

### Exploring IAM Lab
The Objectives of this lab are:
- Use IAM to implement access control;
- Restrict access to specific features or resources
- Use the Service Account User role

## Storage and Database Services
Questions to best choose the storage option:

Is your data structured? 
- No: Do you need a shared file system?
    - Yes: Filestore
    - No: Cloud Storage
- Yes: does your workload focus on analytics
    - Yes: Bigtable or BigQuery, depending on your latency and update needs
    - No: If your data is relational and you need Hybrid transaction/analytical processing, also known as HTAP, choose **AlloyDB**
    - No: If you don’t need HTAP and don’t need global scalability, choose **Cloud SQL**
    - No: If you don’t need HTAP and need global scalability, choose **Spanner**
- If your data is structured, does not focus on analytics and is not relational data
    - If need application caching: Memorystore
    - If don't need application caching: Firestore
---

Storage and database services
| **Service name** | **Best for**   | **Good for**                                          | **Such as**                                     |
|------------------|----------------|-------------------------------------------------------|-------------------------------------------------|
| Cloud Storage    | Object         | Binary or object data                                 | Images, media, serving, backups                 |
| Filestore        | File           | Network Attached Storage (NAS)                        | Latency sensitive workloads                     |
| Cloud SQL        | Relational     | Web Frameworks                                        | CMS, eCommerce                                  |
| Cloud Spanner    | Relational     | RDBMS + Scale, HA, HTAP                               | User metadata, Ad/Fin/MarTech                   |
| AlloyDB          | Relational     | Hybrid transactional and analytical processing (HTAP) | Machine Learning, Generative AI                 |
| Firestore        | Non-relational | Hierarchical, mobile, web                             | User, profiles, game state                      |
| Cloud Bigtable   | Non-relational | Heavy read + write events                             | AdTeach, financial, IoT                         |
| BigQuery         | Warehouse      | Enterprise data warehouse                             | Analytics, dashboards                           |
| Memorystore      | Redis          | Automating complex Redis and Memcached tasks          | Enabling high availability, fail over, patching |

### Cloud Storage
Cloud Storage is a collection of buckets that you place objects into.

Cloud Storage has four storage classes: Standard, Nearline, Coldline and Archive, and each of those storage classes provide 3 location types: 
- multi-region: is a large geographic area, such as the United States, that contains two or more geographic places.
- Dual-region is a specific pair of regions, such as Finland and the Netherlands.
- A region: is a specific geographic place

1. Standard Storage is best for data that is frequently accessed and/or stored for only brief periods of time. This is the most expensive storage class but it has no minimum storage duration and no retrieval cost.
1. Nearline Storage is a low-cost, highly durable storage service for storing infrequently accessed data like data backup, long-tail multimedia content, and data archiving. **30-day minimum storage duration**. Costs for data access are acceptable trade-offs for lowered at-rest storage costs.
1. Coldline Storage is a very-low-cost, highly durable storage service for storing infrequently accessed data. **90-day minimum storage duration**. 
1. Archive Storage is the lowest-cost, highly durable storage service for data archiving, online backup, and disaster recovery. Unlike the so-to-speak "coldest" storage services offered by other Cloud providers, your data is available within milliseconds, not hours or days. Archive Storage also has higher costs for data access and operations, as well as a **365-day minimum storage duration**.


When you upload an object to a bucket, the object is assigned the bucket's storage class, unless you specify a storage class for the object. You can change the default storage class of a bucket but you can't change the location type.

**In order to help manage the classes of objects in your bucket**, Cloud Storage offers Object Lifecycle Management.
000000
Access control for your objects and buckets
- For most purposes, IAM is sufficient, and roles are inherited from project to bucket to object.
- Access control lists or ACLs offer finer control.
- For even more detailed control, signed URLs provide a cryptographic key that gives time-limited access to a bucket or object.
- a signed policy document further refines the control by determining what kind of file can be uploaded by someone with a signed URL.

The maximum number of ACL entries you can create for a bucket or object is 100. Each ACL consists of one or more entries, and these entries consist of two pieces of information: 
- scope: defines who can perform the specified actions (for example, a specific user or group of users).
- permission, which defines what actions can be performed (for example, read or write).


### Cloud Storage Features
- Customer-supplied encryption key (CSEK)
    - Use your own encryption keys instead of the Google-managed keys,
- Object Lifecycle Management
    - Automatically delete, archive objects, etc.
- Object Versioning
    - Maintain multiple versions of objects
    - *You are charged for the versions as if they were multiple files,*
- Directory Synchronization
    - Synchronizes a VM directory with a bucket
- Object change notifications using Pub/Sub
- Autoclass
    - It manages all aspects of storage classes for a bucket.

---

Object Versioning:
- can be enabled for a bucket
- Storage creates an archived version of an object each time the live version of the object is overwritten or deleted.
- The archived version retains the name of the object but is uniquely identified by a generation number
- It's possible to list archived versions of an object, restore the live version of an object to an older state, or permanently delete an archived version
- Google recommends that you use Soft Delete instead of Object Versioning to protect against permanent data loss from accidental or malicious deletions.

Soft Delete:
- It provides default bucket-level protection for your data from accidental or malicious deletion by preserving all recently deleted objects for a specified period of time.
- It retains all deleted objects, whether from a delete command or because of an overwrite
- It is enabled by default with a retention duration of seven days
- You can increase the retention duration to 90 days or disable it by setting the retention duration to 0.

Object Lifecycle Management:
- use cases like: 
    - setting a Time to Live for objects
    - archiving older versions of objects
    - downgrading storage classes
- The configuration is a set of rules that apply to all the objects in the bucket.
- When an object meets the criteria of one of the rules, Cloud Storage automatically performs a specified action on the object.
- rules may not be applied immediately because Object inspection occurs in asynchronous batches. Updates to your lifecycle configuration may take up to 24 hours to go into effect.

Object Retention Lock:
- lets you set retention configuration on objects within Cloud Storage buckets that have enabled the feature
- It governs how long the object must be retained and has the option to permanently prevent the retention time from being reduced or removed.

what if you have to upload terabytes or even petabytes of data? There are three services that address this:
1. Transfer Appliance
    - It is a hardware appliance you can use to securely migrate large volumes of data (from hundreds of terabytes up to 1 petabyte) to Google Cloud without disrupting business operations.
1. Storage Transfer Service
    - It enables high-performance **imports of online data**
    - data source can be another Cloud Storage bucket, an Amazon S3 bucket, or an HTTP/HTTPS location.
1. Offline Media Import
    - It is a third party service where physical media (such as storage arrays, hard disk drives, tapes, and USB flash drives) is sent to a provider who uploads the data.

### Choosing a storage class
If your data has a variety of access frequencies, or the access patterns for your data are unknown or unpredictable, you should consider Autoclass. The Autoclass feature automatically transitions objects in your bucket to appropriate storage classes based on the access pattern of each object. all objects added to the bucket begin in Standard storage. The feature moves data that is not accessed to colder storage classes to reduce storage cost. 
Data that is accessed is also moved to Standard storage to optimize future accesses. **When enabled on a bucket, there are no early deletion charges, no retrieval charges, and no charges for storage class transitions.** All operations are charged at the Standard storage rate.

### Filestore
It is a fully managed network attached storage (NAS) for CE and GKE instances.
Filestore is a managed file storage service for applications that require a file system interface and a shared file system for data. It gives users a simple native experience for standing up managed network attached storage with either Compute Engine or Google Kubernetes Engine instances.

It offers native compatibility with existing enterprise applications and supports any NFSV3 compatible clients. The the benefit of this features are:
- scale-out performance, 
- hundreds of terabytes of capacity, and 
- file locking without the need to install or maintain any specialized plug-ins or client-side software

Use cases:
- expedite migration of enterprise applications
- On-premises applications that require a file system interface to data.
- Enterprise applications that need a shared file system
- media rendering: you can easily meant filestore file shares on Compute Engine instances, enabling visual effects artists to collaborate on the same file share.
- Web developers and large hosting providers also rely on Filestore to manage and serve web content, including needs such as WordPress hosting.

It offers low latency for file operations, and as capacity or performance needs change, you can easily grow or shrink your instances as needed.

### Lab
The objectives of this lab are:
- Create and use buckets
- Set access control lists to restrict access
- Use your own encryption keys
- Implement version controls
- Use directory synchronization
- Share a bucket across projects using IAM

In this lab you learned to create and work with buckets and objects, and you learned about the following features for Cloud Storage:
- CSEK: Customer-supplied encryption key
- Use your own encryption keys
- Rotate keys
- ACL: Access control list
- Set an ACL for private, and modify to public
- Lifecycle management
- Set policy to delete objects after 31 days
- Versioning
- Create a version and restore a previous version
- Directory synchronization
- Recursively synchronize a VM directory with a bucket
- Cross-project resource sharing using IAM
- Use IAM to enable access to resources across projects



get the default access list that's been assigned to the file
```
gsutil acl get gs://$BUCKET_NAME_1/filename.extension  > acl.txt
cat acl.txt
```

To update the access list to make the file publicly readable
```
gsutil acl ch -u AllUsers:R gs://$BUCKET_NAME_1/setup.html
gsutil acl get gs://$BUCKET_NAME_1/setup.html  > acl3.txt
cat acl3.txt
```

Generate a CSEK key

- AES-256 base-64 key: `python3 -c 'import base64; import os; print(base64.encodebytes(os.urandom(32)))'`
- generate boto file: `gsutil config -n`
- Modify the boto file
```
ls -al

nano .boto
```
---
Rotate CSEK keys
- When a file is encrypted, rewriting the file decrypts it using the decryption_key1 that you previously set, and encrypts the file with the new encryption_key.
```
gsutil rewrite -k gs://$BUCKET_NAME_1/setup2.html
```

---
- View the current lifecycle policy for the bucket: `gsutil lifecycle get gs://$BUCKET_NAME_1`
- Create a JSON lifecycle policy file: `nano life.json`
- Paste the following value into the life.json file
```
{
  "rule":
  [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 31}
    }
  ]
}
```
- set the policy: `gsutil lifecycle set life.json gs://$BUCKET_NAME_1`
- verify the policy `gsutil lifecycle get gs://$BUCKET_NAME_1`

---
Enable versioning
- view the current versioning status `gsutil versioning get gs://$BUCKET_NAME_1`
- enable versioning `gsutil versioning set on gs://$BUCKET_NAME_1`
- List all versions of the file: 
```
gcloud storage ls -a gs://$BUCKET_NAME_1/setup.html
```
---
Synchronize a directory to a bucket

To sync the firstlevel directory on the VM with your bucket, run the following command:
`gsutil rsync -r ./firstlevel gs://$BUCKET_NAME_1/firstlevel`
