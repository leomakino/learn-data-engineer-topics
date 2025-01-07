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
1. *(Optional) Validate*:
1. **Apply**: Create actual infrastructure resources

Terraform use cases:
- **Manage infrastructure**: Terraform stakes an immutable approach to building and managing infrastructure
- **Track changes**: Terraform enables you to review the changes before they are applied to the configuration setup
- **Automate changes**: Terraform defines the end state of the infrastructure instead of a series of steps to achieve it.
- **Standardize the configuration**: Terraform uses modules to implement best practices and improve efficiency

## Terms and concepts

### Terraform configuration and HCL
The author phase is where you write Terraform code in, in tf files.

A Terraform directory can consist of multiple files and directories. A Terraform configuration consists of: A root module, also referred to as the root configuration file, And an optional tree for child modules.

Child modules are optional, and can be variables, outputs, providers, and so forth.

The root module is the working directory in which Terraform commands are run.

The language used to write configurations is the HashiCorp Configuration language, or HCL. HCL is a configuration language, not a programming language. Terraform uses HCL to define resources in your Google Cloud environment, create dependencies with those resources, and define the data to be fetched.

HCL syntax:
- Blocks are lines of code that belong to a certain type
    - Examples include resource, variable, and output.
- Arguments are part of a block and used to allocate a value to a name.
- Identifiers are names of an argument, block type, or any Terraform-specific constructs.
    - Identifiers can include letters, underscores, hyphens, and digits, but cannot start with a digit. 
- Expressions can be used to assign a value to an identifier within a code block
- Comment syntax start with a # for a single-line comment.
- the blocks or files does not matter.

### Author Phase Terms and Concepts
Version arguments constrain the provider to a specific version or a range of versions to prevent downloading a new provide that may contain breaking changes. If the version isn't specified, Terraform will automatically download the most recent provider during initialization.

### Terraform Commands
Commands:
- init: Initialize the provider with plugin
    -  ensures that the Google provider plugin is downloaded and installed in a subdirectory of the current working directory, along with various other bookkeeping files
- plan: Preview the resources that will be created after terraform apply
    - detailing all the resources that will be created, modified, or destroyed upon executing terraform apply.
    - Compares the current configuration to the prior state and notes any differences.
    - builds an execution plan that only modifies what is necessary to reach your desired state.
    - use -out=FILE option to Optionally save the generated plan to a file
- apply: Create real infrastructure
    - creates the resources, and establishes the dependencies.
    - The symbols next to the resources and arguments indicate the action performed on the resource.
        - \+ means will be created
        - \-\+ means will be destroyed and recreate the resource
        - ~ means the resource will be updated in-place
        - \- means will be destroyed
- destroy: destroy infrastructure resources
    - Terraform determines the order in which things must be destroyed. E.g.: VPC network can't be deleted if it still has resources
    - Consider all resources have been removed from the configuration
    - It's useful to manage ephemeral infrastructure
    - Can algo destroy specific resources by specifying a target in the command
    - It is a rare event in production enviroments
    - It will destroy the data associated to any resource
- fmt: Autoformat to match canonical conventions

Code conventions (best practices):
- *Separate meta arguments from the other arguments* by placing them first or last in the code with a blank line
- use two spaces for identation
- Align values at the equal sign
- Place nested blocks below arguments
- Separate blocks by one blank line
- **terraform fmt automatically aplies all formatting rules and recommended styles to assist with readability and consistency**

### The terraform validator
Between the plan and apply phases, is the option to validate. The Terraform validator:
- is a tool for enforcing policy compliance as part of an infrastructure CI/CD pipeline
- pre-deployment checks are run against organizational policies.
- helps mitigate configuration errors that can cause security and governance violations.

Businesses are shifting toward infrastructure-as-code, and with that change comes the risk that configuration errors can cause security and governance violations. Use the Terraform Validator to detect policy violations and provide warnings or halt deployments before they reach production.

Constraints 
- define the source of truth for security and governance requirements
- must be compatible with tools across every stage of the application lifecycle, from development, to deployment, to auditing.

Terraform Validator Benefits:
- Enforce policies: Enforce policies at any stage of application development
- Remove manual error: Remove manual errors by automating policy validation
- Reduce time to learn: Reduce learning time by using a single paradigm for all policy management
- The Terraform Validator is used to ensure that the configuration adheres to the set of constraints.

Use cases:
- Platform teams can easily add guardrails to infrastructure CI/CD pipelines, to ensure that all requests for infrastructure are validated before deployment to the cloud.
- Application teams and developers can validate their Terraform configurations against a central policy library to identify misconfigurations early in the development process.
- Security teams can create a centralized policy library that is used by all teams across the organization to identify and prevent policy violations.

gcloud beta terraform vet is different from the terraform validate command.
- `gcloud beta terraform vet`: related to constraints
- `terraform validate`: is used for testing syntax and the structure of your configuration without deploying any resources