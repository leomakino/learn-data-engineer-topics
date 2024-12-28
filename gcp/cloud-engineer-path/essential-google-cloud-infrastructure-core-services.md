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

