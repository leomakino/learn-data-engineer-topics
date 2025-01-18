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

### Container images
An application and its dependencies are called an **image**, and a container is simply a running instance of an image.

By building software into container images, developers can package and ship an application without worrying about the system it will run on. *But to build and run container images, you need software.* One option is Docker.

Although docker can be used to create and run applications in containers, it doesn't offer a way to orchestrate those applications at scale, like Kubernetes does.

A container has the power to isolate workloads, and this ability comes from a combination of several Linux technologies:
1. **Linux process**: Each Linux process has its own virtual memory address space separate from all others, and Linux processes can be rapidly created and destroyed.
1. **Linux namespaces**: Containers use Linux namespaces to control what an application can see, such as process ID numbers, directory trees, IP addresses...
1. **Linux cgroups** control what an application can use, such as its maximum consumption of CPU time, memory, I/O bandwidth, and other resources.
1. **Union File Systems**

A container image is structured in layers, and the tool used to build the image reads instructions from a file called the **container manifest**. For Docker-formatted container images, that's called a Dockerfile. Each instruction in the Dockerfile specifies a layer inside the container image. Each layer is read-only, but when a container runs from this image, it will also have a writable ephemeral topmost layer.

A Dockerfile contains four commands, each of which creates a layer.
1. FROM: creates a base layer, which is pulled from a public repository
1. COPY: adds a new layer, which contains some files copied in from your build tool's current directory
1. RUN: Builds the apllication by using the make command and puts the results of the build into a third layer
1. CMD: the last layer specifies what command you should run within the container when it's launched.

It's not a best practice to build your application in the same container where you ship and run it. The best practice is: Application packaging relies on a multi-stage build process. In other words, One container builds the final executable image and a separate container receives only what is needed to run the apllication. When launching a new container from an image, the container runtime adds a new writable layer on top of the underlying layers. This layer is called the container layer. All changes made to the running container, such as writing new files, modifying existing files, and deleting files, are written to this thin writable container layer. And they're ephemeral, which means that when the container is deleted. 


how can you get or create containers? Google maintains **Artifact Registry** at pkg.dev, which contains public open-source images. Container images are also available in other public repositories, like the **Docker Hub registry and GitLab**.

Google provides a managed service for building containers called C**loud Build**. Cloud Build is integrated with Cloud IAM and was designed to retrieve the source code builds from different code repositories, including Cloud Source Repositories, GitHub and Bitbucket. Each build step in Cloud Build runs in a Docker container.


Cloud Build can deliver the newly built images to various execution environments, including Google Kubernetes Engine, App Engine, and Cloud Run functions.