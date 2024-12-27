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