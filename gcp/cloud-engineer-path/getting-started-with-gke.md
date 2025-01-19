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

### GKE modes
Autopilot:
- optimizes the management of Kubernetes with a hands-off experience
- only pay for what you use.

Standard:
- allows the Kubernetes management infrastructure to be configured in many different ways.
- This requires more management overhead, but produces an environment for fine-grained control.
- you pay for all of the provisioned infrastructure, regardless of how much gets used.

Benefits and functionality of Autopilot:
- optimized for production
- Autopilot defines the underlying machine type for your cluster based on workloads, which optimizes both usage and cost for the cluster and adapts to changing workloads.
- It lets you deploy production-ready GKE clusters faster.
- helps produce a strong security posture
  - Google helps secure the cluster nodes and infrastructure, and it eliminates infrastructure security management tasks.
  - By locking down nodes, Autopilot reduces the cluster's attack surface and ongoing configuration mistakes.
- Google monitors the entire Autopilot cluster, including control plane, worker nodes and core Kubernetes system components.
- provides a way to configure update windows for clusters to ensure minimal disruption to workloads.
- Google is fully responsible for optimizing resource consumption. **Only pay for Pods, not nodes**

Autopilot restrictions:
- The configuration options in GKE Autopilot are more restrictive than in GKE Standard.
- It has restrictions on access to node objects: Features like SSH and privilege escalation were removed and there are limitations on node affinity and host access.

The GKE Standard mode has the same functionality as Autopilot, but you're responsible for the configuration, management, and optimization of the cluster.

### Deploying GKE Autopilot lab
Clusters can be created across a region or in a single zone. A single zone is the default. When you deploy across a region the nodes are deployed to three separate zones and the total number of nodes deployed will be three times higher

### Kubernetes object management
All Kubernetes objects are identified by a unique name and a unique identifier.

If several objects are related, it's a best practice to define them all in the same YAML file. This makes things easier to manage.

1. Only one object can have a particular name at the same time in the same Kubernetes namespace.
1. every object created throughout the life of a cluster has a unique identifier, or UID, generated by Kubernetes.
1. there are labels: Labels help identify and organize objects.

In Kubernetes, a workload is spread evenly across available nodes by default. 

To maintain an application's high availability, you need a better way to manage it in Kubernetes than specifying individual Pods. One option is to declare a controller object.

Deployments are a great choice for long-lived software components like web servers, especially when you want to manage them as a group. Instead of using multiple YAML manifests or files for each Pod, you used a single Deployment YAML to launch three replicas of the same container. Within a Deployment object spec, the number of replica Pods, which containers should run the Pods, and which volumes should be mounted the following elements are defined.

## Kubernetes Operations
### kubectl command
kubectl is a utility used by administrators to control Kubernetes clusters. It's used to communicate with the Kube API server on the control plane.

**to work properly, kubectl must be configured with the location and credentials of a Kubernetes cluster.** And before kubectl can be used to configure a cluster, it must first be configured.

*kubectl stores its configuration in a file in the home directory in a hidden folder named $home/.kube/config.*

**kubectl config** shows the configuration of the kubectl command itself, whereas other kubectl commands show the configurations of cluster and workloads.

To connect kubectl to a GKE cluster, first retrieve the credentials for the specified cluster. This can be done with the “get-credentials” gcloud command in any other environment where the gcloud command-line tool and kubectl are installed.

By default, the gcloud “get-credentials” command writes configuration information into a config file in the . kube directory in the $HOME directory.

Although kubectl is a tool for administering the internal state of an existing cluster, it can't create new clusters or change the shape of existing clusters.

kubectl's syntax is composed of four parts:
1. the command
1. the type: like Pods, deployments, nodes, or other objects, including the cluster itself.
1. the name: specifies the object defined in TYPE. *The name field isn't always needed*
1. optional flags

The command specifies the action that you want to perform, such as get, describe, logs, or exec.

The kubectl command has many uses, from creating Kubernetes objects, to viewing them, deleting them, and viewing or exporting configuration files.

Connect kubectl to a GKE cluster:
```bash
gcloud container clusters \
get credentials [CLUSTER_NAME] \
-- region [REGION_NAME]
```

### Introspection
Introspection is the process of debugging problems when an application is running. It's the act of gathering information about the containers, pods, services, and other engines that run within the cluster.

We'll start with four commands to use to gather information about your app:
1. get: It shows the object's phase status as pending, running, succeeded, failed, or unknown, or CrashLoopBackOff.
    - Containers inside a Pod can be starting, restarting, or running continuously.
1. describe: investigate a Pod in detail
    - This command provides information about a Pod and its containers such as labels, resource requirements, and volumes.
1. exec: lets you run a single command inside a container and view the results in your own command shell.
    - This is useful when a single command, such as ping, will do.
1. logs: provides a way to see what is happening inside a Pod.
    - This is useful in troubleshooting, as the logs command can reveal errors or debugging messages written by the applications that run inside Pods.
    - if the Pod has multiple containers, you can use the -c argument to show the logs for a specific container inside the Pod.
    - stdout: Standard output on the console
    - stderr: Standard error messages

Example: Let's say you need to install a package, like a network monitoring tool or a text editor, before you can begin troubleshooting. To do so, you can launch an interactive shell using the `kubectl exec -it [POD_NAME] -- [command]` switch, which connects your shell to the container that allows you to work inside the container. This syntax attaches the standard input and standard output of the container to your terminal window or command shell. The -i argument tells kubectl to pass the terminal's standard input to the container, and the -t argument tells kubectl that the input is a TTY. If you don't use these arguments then the exec command will be executed in the remote container and return immediately to your local shell. 

It's not a best practice to install software directly into a container, as changes made by containers to their file systems are usually ephemeral. Instead, consider building container images that have exactly the software you need, instead of temporarily repairing them at run time.

### Deploying GKE Autopilot Clusters from Cloud Shell
create a kubernetes cluster for running containers : `gcloud container clusters create-auto $my_cluster --region $my_region`

In Kubernetes, authentication can take several forms. For GKE, authentication is typically handled with OAuth2 tokens and can be managed through Cloud Identity and Access Management across the project as a whole and, optionally, through role-based access control which can be defined and configured within each cluster.

In GKE, cluster containers can use service accounts to authenticate to and access external resources.


To create a kubeconfig file with the credentials of the current user (to allow authentication) and provide the endpoint details for a specific cluster (to allow communicating with that cluster through the kubectl command-line tool), execute the following command: `gcloud container clusters get-credentials $my_cluster --region $my_region`

This command creates a .kube directory in your home directory if it doesn't already exist. In the .kube directory, the command creates a file named config if it doesn't already exist, which is used to store the authentication and configuration information. The config file is typically called the kubeconfig file. Open the kubeconfig file with the nano text editor: `nano ~/.kube/config`

The kubeconfig file can contain information for many clusters. The currently active context (the cluster that kubectl commands manipulate) is indicated by the current-context property. 

After the kubeconfig file is populated and the active context is set to a particular cluster, you can use the kubectl command-line tool to execute commands against the cluster. 

- print out the content of the kubeconfig file: `kubectl config view`
- print out the cluster information for the active context: `kubectl cluster-info`
- print out the active context: `kubectl config current-context`
- print out some details for all the cluster contexts in the kubeconfig file: `kubectl config get-contexts`
- change the active context: `kubectl config use-context gke_${DEVSHELL_PROJECT_ID}_Region_autopilot-cluster-1`

Kubernetes introduces the abstraction of a Pod to group one or more related containers as a single entity to be scheduled and deployed as a unit on the same node.

deploy nginx as a Pod named nginx-1: `kubectl create deployment --image nginx nginx-1`

This command creates a Pod named nginx with a container running the nginx image. When a repository isn't specified, the default behavior is to try to find the image either locally or in the Docker public registry. In this case, the image is pulled from the Docker public registry.

- view all the deployed Pods in the active context cluster: `kubectl get pods`
- view the resource usage across the nodes of the cluster: `kubectl top node` and `kubectl top pods`

To be able to serve static content through the nginx web server, you must create and place a file into the container. place the file into the appropriate location within the nginx container in the nginx Pod to be served statically: `kubectl cp ~/test.html $my_nginx_pod:/usr/share/nginx/html/test.html`. *ou can specify other containers in a multi-container Pod by using the -c option, followed by the name of the container.*

A service is required to expose a Pod to clients outside the cluster. Services are discussed elsewhere in the course and used extensively in other labs. You can use a simple command to create a service to expose a Pod: `kubectl expose pod $my_nginx_pod --port 80 --type LoadBalancer`. This command creates a LoadBalancer service, which allows the nginx Pod to be accessed from internet addresses outside of the cluster.

view details about services in the cluster: `kubectl get services`

In this task, you connect to a Pod to adjust settings, edit files, and make other live changes to the Pod. *Note: Use this process only when troubleshooting or experimenting. Because the changes you make are not made to the source image of the Pod, they won't be present in any replicas.*

deploy your manifest, execute the following command: `kubectl apply -f ./new-nginx-pod.yaml`

In this task you use shell redirection to connect to the bash shell in your new nginx pod to carry out a sequence of actions.

start an interactive bash shell in the nginx container: kubectl exec -it new-nginx -- /bin/bash

Because the nginx container image has no text editing tools by default, you need to install one:
```bash
apt-get update
apt-get install nano
```

To connect to and test the modified nginx container (with the new static HTML file), you could create a service. An easier way is to use port forwarding to connect to the Pod directly from Cloud Shell. set up port forwarding from Cloud Shell to the nginx Pod (from port 10081 of the Cloud Shell VM to port 80 of the nginx container): `kubectl port-forward new-nginx 10081:80`
curl http://35.197.126.220/test.html