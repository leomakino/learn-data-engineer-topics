# Getting Started with Google Kubernetes Engine
Kubernetes is an orchestration framework for software containers. Containers are a way to package and run code that's more efficient than virtual machines. Kubernetes provides the tools you need to run containerized applications in production and at scale.

Google Kubernetes Engine (GKE) is a managed service for Kubernetes

## Introduction to Containers and Kubernetes
Essential concepts:
- containers: A container is a standard unit of software that packages up code and all its dependencies
- container images
- Kubernetes
- Google Kubernetes Engine

### Containers

running multiple applications problems:
1. every time you start a VM, its operating system takes time to boot up
1. applications that share dependencies are not isolated from each other
1. a dependency upgrade for one application might cause another to stop working.

*A more efficient way to resolve the dependency problem is to implement abstraction at the level of the application and its dependencies.* You don’t have to virtualize the entire machine, or even the entire operating system–just the user space. The user space is all the code that resides above the kernel, and it includes applications and their dependencies. *This is what it means to create containers.*

Containers:
- are isolated user spaces for running application code.
- are lightweight because they don’t carry a full operating system
- can be created and shut down quickly, because they just start and stop operating system processes and do not boot an entire VM or initialize an operating system for each application.
- are a code-centric way to deliver high-performing, scalable applications.
- provide access to reliable underlying hardware and software

The application code is packaged with all the dependencies it needs, and the engine that executes the container is responsible for making them available at runtime.