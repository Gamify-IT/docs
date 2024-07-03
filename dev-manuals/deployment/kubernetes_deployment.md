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

## Creating a deployment 
[//]: # (TODO insert link to helm explanation)
To create a deployment from scratch a so-called [helm chart]() is used to create and maintain it, 
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
But first you need to fill it with data.