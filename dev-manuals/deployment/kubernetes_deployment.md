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

## Deployment using Terraform
To create a deployment and maintain it we use terraform. We provide the necessary files in the run-config repository
within a [terraform folder](https://github.com/Gamify-IT/run-config). With the `git clone` command with a terminal inside your preferred directory you can get the folder on your disk.
Inside this folder you must add the admin-config provided by the professor. The name of the config must be set to `kubeconfig.yaml`.

The content of the folder should have a structure like this:
```
<gamify-it-tf>
 |_ .terraform                 # Includes provider plug-ins needed by Terraform
 |_ files                      # Includes the keycloak-realm-template
 |_ .terraform.lock.hcl        # Management of providers, handled by Terraform
 |_ backend.tf                 # Configurations for the backend resources.
 |_ frontend.tf                # Configurations for the frontend resources.
 |_ gamify.tfvars              # Variable values for selected Terraform configurations
 |_ ingress.tf                 # Configurations for the ingress resource.
 |_ keycloak.tf                # Configurations for keycloak instance.
 |_ kubeconfig.yaml            # The config provided by the professor.
 |_ main.tf                    # Configurations of providers to connect to the Kubernetes cluster.
 |_ postgres.tf                # Configurations for the postgres database set up.
 |_ reverse_proxy.tf           # Configurations for reverse proxy associated with the project.
 |_ terraform.tfstate          # Current state of the infrasturcture, e.g. current configurations, modifications
 |_ terraform.tfstate.backup   # Stores the current state before modifications to it happen.
 |_ variables.tf               # Variables needed for the project to be set, e.g namespace, credentials, versions.
```

These files will be used by Terraform, when you ask it to apply your deployment on a cluster.
To do so, open a terminal from inside the Terraform folder in your selected directory and use the following commands.

Start terraform and follow the instructions:
```shell
terraform init
```

When you update variables in `gamify.tfvars` you need apply them by using this command:
```shell
terraform apply --var-file gamify.tfvars
```

To test it locally you can map the reverse proxy service's endpoint to your localhost address using kubectl in a terminal inside Lens:
```shell
kubectl -n gamify-it port-forward service/gamify-it-reverse-proxy 80:80
```
Or you can run it in a terminal. Therfore you need to run the following command in a terminal to connect to Kubernetes on the cluster:
```shell
$env:KUBECONFIG="$HOME\.kube\config;$HOME\.kube\admin-config"
```
Here we assume that your `.kube` file is in your `$HOME` directory as described in the first steps chapter. 

If the mapping was successful, you should be able to access the application via `https://localhost`

## What now?
After completing all the steps above, you should see the pods running in the `Workloads/Pods` section of Lens Desktop. They should all be set to `Running`.
It is advised that you make yourself familiar with the other sections of lens, since you can find the parts of your deployment there and monitor them as well.

## Removing your deployment
To remove the resources created by Terraform open a terminal from inside the terraform folder and run following command
```shell
terraform destroy
```
Terraform will then prompt you to confirm the action.