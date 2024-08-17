# Cloud Deployment with Kubernetes
The project has a cloud deployment, which is running on Prof. Beckers cluster. To access the cluster,
you need to request an admin-config from Prof. Becker.



## First steps: local setup
The first thing you need is [kubectl](https://kubernetes.io/de/docs/tasks/tools/install-kubectl/).
Follow the download instructions and check if the installation was successful with the 
```shell
kubectl version
```
command. Locate/create the .kube directory in your home directory (as described in the installation manual).
In this directory create a `config` file (no file ending).
You should end up with the following structure (the cache folder will be created on first use of kubectl).
```
%USER%
 |_ .kube
     |_ config 
     |_ cache
```
Open the `config` file with an editor of your choice, e.g. notepad++ and copy the admin-config into this file.
You can run
```shell
kubectl config view
```
in your terminal to see if you were successful (the output should be the admin-config).

**Note:** Since the cluster is hosted at the university, you can only access it from the university network, either 
in person at campus or with the vpn.



### Switching config context
If you have multiple entries in your config file, and you want to switch between them, use 
```shell
kubectl config use-context <context-name>
```
where the context name is listed behind the name tag in the config file for the respective context.

With 
```shell
kubectl config get-contexts
```
you can see all available contexts, with the currently active on being marked with an asterisk (*).



### Lens
An alternative to using the command line to deploy your helm chart to the cluster, is [Lens](https://k8slens.dev/download).
Lens is a GUI for kubernetes, and simplifies the deployment process drastically. Just download it and follow the installation
instructions. \
If you already have the admin config added to your kubeconfig, you should be able to see the cluster by changing
to the catalog on the left and browsing through the list. You can open more information about the cluster by clicking on it
(while in the university network). There you can see more information about the cluster resources, the pods of the cluster
and more. We recommend looking around a bit to make yourself familiar with the programm.



## Creating a deployment 
To create a deployment from scratch a so-called [helm chart](helm_chart.md) is used to create and maintain it, 
[helm](https://helm.sh/docs/intro/install/) is used. Simply follow the installation instructions
on their page.

Helm charts are simply put a collection of files and folders, with certain names and structures. But in the end 
it still is just a fancy word for a collection of files and folders.

To start creating a helm chart, run the following command:
```shell
helm create <chart-name>
```

This will create a new helm chart with the following structure:
```
<chart-name>
 |_ .helmignore    # Contains patterns to ignore when packaging Helm charts.
 |_ Chart.yaml     # Information about your chart
 |_ values.yaml    # The default values for your templates
 |_ charts/        # Charts that this chart depends on
 |_ templates/     # The template files
     |_ tests/     # The test files
```
In the end, this helm chart will be deployed onto the cluster, and contains the specifications for 
the images, resources and additional data, the cluster needs to make a kubernetes deployment.
But first you need to fill it with data. For more information about helm charts see [helm chart](helm_chart.md)

## Deploying your helm chart
If you are using our [provided helm chart](https://github.com/Gamify-IT/run-config) you can skip the creating section.
You need to download the helm chart and save it on your machine before continuing with the next steps.

If there doesn't exist a namespace for the deployment, you first need to create one yourself with:
```shell
kubectl create namespace <namespace>
```
Our helm chart folder contains so called `persistent volumes (pv)` which need to be deployed **before** deploying the actual
helm chart.\
To do so, connect to the cluster and open a terminal in lens and use the following command:
```shell
kubectl apply -f pv.yaml -n <namespace>
```
Then you need to pre-provision the secrets which are also provided in our helm chart folder:
```shell
kubectl apply -f keycloak-admin-secret.yaml -n <namespace>
```
Now you can deploy the actual helm chart, with:
```shell
helm install <your-deployment-name> "path-to-helm-chart" -n <namespace>
```

The name you choose in this step is necessary if you want to modify/uninstall the deployment.

After completing all the steps above, you should see the pods running in the `Workloads/Pods` section of lens, as well as
the pvs in the `Storage/Persistent Volumes` section.
It is advised that you make yourself familiar with the other sections of lens, since you can find the parts of your 
deployment there and monitor them as well.

## Removing your deployment
To completely remove all pods of the deployment you can delete the namespace:
```shell
kubectl delete namespace <namespace>
```
This will **not** delete the persistent volumes, they have to be deleted separately afterwards with the delete button in lens.

There are some issues with keycloak, where it won't use your set environment variables, due to data still being around on the cluster.
This can be fixed by uninstalling and redeploying in this way, other ways of removing the deployment like `helm uninstall` are 
not strong enough to clean up all the data.