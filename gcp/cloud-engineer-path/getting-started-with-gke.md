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

*A more efficient way to resolve the dependency problem is to implement abstraction at the level of the application and its dependencies.* You don't have to virtualize the entire machine, or even the entire operating system–just the user space. The user space is all the code that resides above the kernel, and it includes applications and their dependencies. *This is what it means to create containers.*

Containers:
- are isolated user spaces for running application code.
- are lightweight because they don't carry a full operating system
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

### Working with Cloud Build
The objectives of this lab are:
- Use Cloud Build to build and push containers
- Use Artifact Registry to store and deploy containers

---
Building containers with DockerFile and Cloud Build

You can write build configuration files to provide instructions to Cloud Build as to which tasks to perform when building a container. These build files can fetch dependencies, run unit tests, analyses and more.

1. Create an empty quickstart `nano quickstart.sh`
1. Add the following lines in to the file
```bash
#!/bin/sh
echo "Hello, world! The time is $(date)."
```
3. Create an empty Dockerfile `nano Dockerfile`
1. Add the following Dockerfile command
```dockerfile
# use the Alpine Linux base image
FROM alpine
# adds the quickstart.sh script to the / directory in the image
COPY quickstart.sh /
# This configures the image to execute the /quickstart.sh script
CMD ["/quickstart.sh"]
```
5. make the quickstart.sh script executable: `chmod +x quickstart.sh`
1. Create a new Docker repository named quickstart-docker-repo
```bash
gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker \
    --location="REGION" --description="Docker repository"
```
7. build the Docker container image in Cloud Build: `gcloud builds submit --tag "REGION"-docker.pkg.dev/${DEVSHELL_PROJECT_ID}/quickstart-docker-repo/quickstart-image:tag1`

--- 

Building containers with a build configuration file and Cloud Build
Cloud Build also supports custom build configuration files. In this task you will incorporate an existing Docker container using a custom YAML-formatted build file with Cloud Build.

1. `nano cloudbuild.yaml`
1. Include the lines
```yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: [ 'build', '-t', 'YourRegionHere-docker.pkg.dev/$PROJECT_ID/quickstart-docker-repo/quickstart-image:tag1', '.' ]
images:
- 'YourRegionHere-docker.pkg.dev/$PROJECT_ID/quickstart-docker-repo/quickstart-image:tag1'
```
3. start a Cloud Build using cloudbuild.yaml as the build configuration file `gcloud builds submit --config cloudbuild.yaml`

### Kubernetes
Kubernetes is an open source platform for managing containerized workloads and services. It makes it easy to orchestrate many containers on many hosts, scale them as microservices, and easily deploy rollouts and rollbacks.

Kubernetes is a set of APIs that you can use to deploy containers on a set of nodes (computing instances) called a cluster. The system is divided into a set of primary components that run as the control plane and a set of nodes that run containers.

You can describe a set of applications and how they should interact with each other, and Kubernetes determines how to make that happen. 

ubernetes supports declarative configurations. When you administer your infrastructure declaratively, you describe the desired state you want to achieve, instead of issuing a series of commands to achieve that desired state.

Kubernetes also allows imperative configuration, in which you issue commands to change the system's state. One of the primary strengths of Kubernetes is its ability to automatically keep a system in a state you declare. Therefore, experienced Kubernetes administrators use imperative configuration only for quick temporary fixes and as a tool when building a declarative configuration.

features:
- Kubernetes supports different workload types.
    - It supports stateless applications, such as Nginx or Apache web servers, and stateful applications where user and session data can be stored persistently.
    - supports batch jobs and daemon tasks
- It can automatically scale containerized applications in and out based on resource utilization.
- It allows users to specify resource request levels and resource limits for workloads.
- It is extensible through a rich ecosystem of plugins and addons.

Kubernetes Custom Resource Definitions let developers define new types of resources that can be created, managed, and used in Kubernetes. it's open-source, Kubernetes is portable and can be deployed anywhere-whether on premises or on another cloud service provider.

### Google Kubernetes Engine
Google Kubernetes Engine is a managed Kubernetes service hosted on Google's infrastructure. It's designed to help deploy, manage, and scale Kubernetes environments for containerized applications.

Google Kubernetes Engine offers a mode of operation called GKE Autopilot, which is designed to manage your cluster configuration, like nodes, scaling, security, and other preconfigured settings.

The virtual machines that host containers in a GKE cluster are called nodes. GKE has a node auto-repair feature that was designed to repair unhealthy nodes. It performs periodic health checks on each node of the cluster and nodes determined to be unhealthy are drained and recreated.

GKE is integrated with several services: 
- Cloud Build uses private container images securely stored in Artifact Registry to automate the deployment.
- IAM helps control access by using accounts and role permissions.
- Google Cloud Observability provides an understanding into how an application is performing.
- Virtual Private Clouds, which provide a network infrastructure including load balancers and ingress access for your cluster.

## Kubernetes Architecture
### Kubernetes concepts
Kubernetes object model: Each item Kubernetes manages is represented by an object, and you can view and change these objects attributes and state.

Declarative management: Kubernetes needs to be told how objects should be managed, and it will work to achieve and maintain that desired state.

A Kubernetes object is defined as a persistent entity that represents the state of something running in a cluster: its desired state and its current state.

Kubernetes objects have two important elements:
1. an object spec for each object being created. It's here that the desired state of the object is defined by you.
1. the object status, which represents the current state of the object provided by the Kubernetes control plane.

Kubernetes control plane is a term to refer to the various system processes that collaborate to make a Kubernetes cluster work.

Pods:
- Pods are the foundational building block of the standard Kubernetes model, and they're the smallest deployable Kubernetes object. 
- Every running container in a Kubernetes system is in a Pod.
- A Pod creates the environment where the containers live, and that environment can accommodate one or more containers.
- If there is more than one container in a Pod, they are tightly coupled and **share resources**, like networking and storage.
- Kubernetes assigns each Pod a unique IP address, and every container within a Pod shares the network namespace, including IP address and network ports.
- Containers within the same Pod can communicate through localhost, 127.0.0.1
- A Pod can also specify a set of storage volumes that will be shared among its containers.

### Kubernetes components
Control plane:
- Kube-APIserver
- etcd
- kubernetes scheduler
- kube-cloud-manager
- kube-controller-manager

A Pod can also specify a set of storage volumes that will be shared among its containers.

A cluster needs computers, and these computers are usually virtual machines. One computer is called the **control plane**, and the others are called **nodes**. The node's job is to run Pods, and the control plane's is to coordinate the entire cluster.

Several critical Kubernetes components run on the control plane:
1. kube-APIserver component, which is the only single component that you'll interact with directly.
    - The job of this component is to accept commands that view or 
    change the state of the cluster.
    - **kubectl command**: connect to the kube-APIserver and communicate with it using the Kubernetes API
    - it also authenticates incoming requests, determines whether they are authorized and valid, and manages admission control.
    - any query or change to the cluster's state must be addressed to the kube-APIserver.
1. **etcd** component is the **cluster's database**
    - Its job is to reliably store the state of the cluster.
    - This includes all the cluster configuration data,along with more dynamic information such as what nodes are part of the cluster, what Pods should be running, and where they should be running.
1. **kube-scheduler** is responsible for scheduling Pods onto the nodes
    - evaluates the requirements of each individual Pod and selects which node is most suitable.
    - it **doesn't** do the work of actually launching Pods on nodes
    - whenever it discovers a Pod object that doesn't yet have an assigned node, it chooses a node and writes the name of that node into the Pod object.
1. **kube-controller-manager component**: it continuously monitors the state of a cluster through the kube-APIserver
    - Whenever the current state of the cluster doesn't match the desired state, kube-controller-manager will attempt to make changes to achieve the desired state.
    - It's called the controller manager because many Kubernetes objects are maintained by loops of code called controllers, which handle the process of remediation. *The Node Controller's job is to monitor and respond when a node is offline.*
1. **kube-cloud-manager** component manages controllers that interact with underlying cloud providers.
    - if you manually launched a Kubernetes cluster on Compute Engine, kube-cloud-manager would be responsible for bringing in Google Cloud features like load balancers and storage volumes.

Nodes:
- Each node runs a **small family of control-plane** components called a **kubelet**
  - kubelet is like an Kubernetes's agent on each node.
  - When the kube-APIserver wants to start a Pod on a node, it connects to that node's kubelet.
  - Kubelet uses the container runtime to start the Pod and monitors its lifecycle, including readiness and liveness probes, and reports back to the kube-APIserver.
- kube-proxy: maintains network connectivity among the Pods in a cluster.

How is GKE different from Kubernetes?
- GKE manages all the control plane components for us.
- GKE still exposes an IP address to which we send all of our Kubernetes API
- Node configuration and management depends on the type of GKE mode you use.
- With the Autopilot mode, which is recommended, GKE manages the underlying infrastructure such as node configuration, autoscaling, auto-upgrades, baseline security configurations, and baseline networking configuration.
- With the Standard mode, you manage the underlying infrastructure, including configuring the individual nodes.