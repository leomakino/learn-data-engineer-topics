# Getting Started with Terraform for Google Cloud
Problems that IaC can solva:
- Inability to scale rapidly
- Operational bottlenecks
- Disonnected feedback loops
- High manual errors

Benefits of IaC:
- Declative: Specify the desired state of infrastructure, not updates
- Code management: Commit, version, trace, and collaborate, just like source code.
- Auditable: Compare infrastructure between desired state and current state
- Portable: Build reusable modules across an organization

IaC:
- Used for provisioning and managing cloud resources
    - Example: Creating and provisioning
- Refers to frameworks that manipulate Google Cloud APIs to deploy the infrastructure

IaC configuration workflow:
1. **Scope**: Confirm the resources required for a project
1. **Author**: Author the configuration files based on the scope
1. **Initialize**: Download the provider plugins and initialize directory
1. **Plan**: View execution plan for resources created, modified, or destroyed.
1. **Apply**: Create actual infrastructure resources

Terraform use cases:
- **Manage infrastructure**: Terraform stakes an immutable approach to building and managing infrastructure
- **Track changes**: Terraform enables you to review the changes before they are applied to the configuration setup
- **Automate changes**: Terraform defines the end state of the infrastructure instead of a series of steps to achieve it.
- **Standardize the configuration**: Terraform uses modules to implement best practices and improve efficiency