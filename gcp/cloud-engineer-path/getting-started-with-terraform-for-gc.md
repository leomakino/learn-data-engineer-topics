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

## Writing Infrastructure Code for Google Cloud
### Resources
Resources are infrastructure elements.

Resources, In GC, include instances, instance templates, groups, VPC networks, firewall rules, VPN tunnels, Cloud Routers, and more.

Terraform uses the underlying APIs of each Google Cloud service to deploy your resources.

A provider is a plugin that provides a collection of resource types.

- The resource block is used to declare a single infrastructure object.
- Some resource arguments are mandatory for resource creation, and others are optional.
- Attributes can be used to define any advanced features associated with a resource.

A declared resource is identified by its type and name. Therefore, the resource name must be unique within the module.

### Meta-arguments for resources
The Terraform language defines several meta-arguments, which can be used with any resource type to change the behavior of resources.
- **Count** creates multiple instances, depending on the value you define.
- **for_each** creates multiple instances according to a map or set of strings.
- **Depends_on** is used to specify explicit dependencies
- **Lifecycle** defines the lifecycle of a resource.

With the lifecycle argument you can prevent destruction of a resource for compliance purposes, and create a resource before destroying the replaced resource. This approach is often used for high availability.

Count:
- replace redundant code by adding the count argument at the beginning of the resource definition.
- tells Terraform to create n instances of the same kind.
- The count index starts at 0 and increments by 1 for each resource.


*If some of their arguments need distinct values that can't be directly derived from an integer, it's safer to use for_each.*

for_each:
- Terraform will create one instance for each member of the string.
- Consider a scenario where you need three similar instances configured in three specific zones and you want the names to have zones as prefixes for identification. Instead of writing lengthy repetitive code, you can use the for_each argument to assign specific values.

### Resource dependencies
A dependency graph helps you understand your infrastructure before deploying it. Terraform builds a dependency graph from your configurations to generate plans and refresh state. Terraform creates a dependency graph to determine the correct order of operations. 

Graph command: `terraform graph | dot -Tpng > graph.png`

The attributes are interpolated during run time, and primitives such as variables, output values, and providers are connected in a dependency tree.

Terraform can handle two kinds of dependencies: implicit and explicit.
- Implicit dependencies are known to Terraform
    - E.g.1: cannot create a compute instance unless the network is created
    - E.g.2: cannot assign a static IP address for a Compute Engine instance until a static IP is reserved.
    - A given resource can only be created upon creation of another resource.
- explicit dependencies are unknown. You need to explicitly mention dependencies that Terraform cannot see.
    - E.g. 1:  let’s say you use a specific Cloud Storage bucket to run an application. That dependency is configured inside the application code and not visible to Terraform. **In this scenario, you can use depends_on to explicitly declare the dependency.**
    - The depends_on argument gives you the flexibility to control the order in which Terraform processes the resources in a configuration.
    - E.g.2: you need to create two VMs—server and client —and want the client VM to only be created upon the successful creation of the server VM. This dependency is not visible to Terraform and has to be explicitly mentioned.

The order in which the resources are defined has no effect on how Terraform applies your changes, so organize your configuration files in a way that makes the most sense for you and your team.

### Variables
With variables, you can parameterize values shared between resources. Input variables serve as parameters for Terraform, allowing easy customization and sharing without having to alter the source code. Variables separate source code from value assignments.

Variables must be declared in the variable block. *It’s recommended that you save all variable declarations within a separate file named variables.tf*.

There are two rules for naming variables.
1. the name of the variable must be unique within a module.
1. variable names cannot be keywords.


Terraform can automatically deduce the type and default values. 

Terraform supports the following primitive variable types: 
- Bool
- Number
- string

```tf
variable "variable_name" {
    type = <variable_type>
    description = "<variable description>"
    default = "<default value for variable>"
    sensitive = true
}
```

To access the value of a variable declared within the module, you can use the expressions var.

The default value can be overridden by assigning a value in environment values, or .tfvars files or -var option.

The description string is often included in documentation, so it should be written from the perspective of the user rather than its maintainer. Comments can be used by the maintainer.

Sensitive, as the name suggests, is a variable argument used to protect sensitive information from being displayed in command outputs or log files

There are several ways to set **variable values to variables**: Terraform automatically loads the variable definitions files as long as they are exactly named terraform.tfvars, terraform.tfvars.json, .auto.tfvars, or auto.tfvars.json.

```bash
# .tfvars file (Recommended method)
tf apply -var-file my-vars.tfvars

# CLI option
tf apply -var project_id="my-project"

# environment variables
TF_VAR_project_id="myproject" \
tf apply

# Using terraform.tfvars
tf apply
```

### Variables best practices
Parameterize only when necessary:
- Only parameterize values that must vary for each instance or environment
- Changing a variable with a default value is backward-compatible
- removing a variable is not backward-compatible.
- Avoid alternating between var-files and command-line options. Command-line options are ephemeral and easy to forget, and they cannot be checked into source control.
- Variables must have descriptions.

### Output values
Output values are similar to return values in common programming languages. With outputs, you can view information about the infrastructure resources you created on the command line.

Output values are used for several purposes. The most common use case is to print root module resource attributes in the CLI after its deployment. Most of the server details are calculated at deployment and can only be inferred post-creation.

Output values are also **used to pass information generated by one resource to another**.  Most of the server details are calculated at deployment and can only be inferred post-creation.
- For example, you can extract server-specific values – such as an IP address – to another resource that requires this information.

Output values are declared using the output block. The keyword ‘output’ indicates that the label associated with the keyword is the name of the output value.

The arguments that can be included within an output block are:
- value: returns a value to the user of the module
- Description: provides an explanation of the purpose of the output and the value expected.
- sensitive: used to mask the value to a resource attribute.

```tf
output "name" {
    description = "purpose of the output and the value expected"
    # value = <resource_type>.<resource_name>.<attribute>
    value = google_storage_bucket_object.picture.self_link
}
```

best practices for output values
- declare them in a separate file named output.tf
- Only output useful information, such as computed information
- Avoid outputting values that simply regurgitate variables or provide known information
- provide meaningful names and descriptions.
- mark sensitive outputs

### Terraform Registry and Cloud Foundation Toolkit
Resources available to help you write infrastructure code for Google Cloud:
1. Terraform Registry
    - is an interactive resource for discovering a wide selection of integrations and configuration packages, otherwise known as providers and modules.
    - includes solutions developed by HashiCorp, third-party vendors, and the Terraform community.
1. Cloud Foundation Toolkit (CFT)
    -  provides a series of reference modules for Terraform that reflect Google Cloud best practices.
    - is a collection of Google Cloud Terraform modules built and maintained by Googlers.
1. Cloud Foundation Fabric (CFF)
    - a collection of Terraform modules and end to end examples meant to be cloned as a single unit and used for fast prototyping or decomposed and modified for usage in organizations.