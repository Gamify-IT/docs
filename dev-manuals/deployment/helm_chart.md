# Helm Charts

The provided helm chart has the following structure:
```
 helm chart/
  |_ pv.yaml
  |_ keycloak-admin-secret.yaml
  |_ gamify-it-helm-config/
     |_ .helmignore    
     |_ Chart.yaml     
     |_ values.yaml    
     |_ templates/    
        |_ NOTES.txt
        |_ _helpers.tpl
        |_ backend-deployment.yaml
        |_ frontend-deployment.yaml
        |_ hpa.yaml
        |_ ingress.yaml
        |_ reverse-proxy-deployment.yaml
        |_ reverse-proxy-service.yaml
        |_ services.yaml
        |_ statefulset.yaml
```
The content of these files will be briefly described here.


### helm chart/
#### pv.yaml
This file takes care of the deployment of the persistent volumes.

#### keycloak-admin-secret.yaml
This file contains the admin credentials for the keycloak admin console. The credentials itself, are stored
in the repository secrets.

### gamify-it-helm-config/
#### .helmignore
Analog to the `.gitignore` file. It tells helm which files/directories to ignore.

#### Chart.yaml
This file contains some metadata about the chart.

#### values.yaml
As previously mentioned this file contains all the environment variables and other data used to deploy the pods.
It is structured similar to a `docker-compose.yaml` file, but for all pods at once.


### templates/
#### NOTES.txt
This file provisioned by default when creating a helm chart, its information will be displayed after running 
`helm install`.

#### _helpers.tpl
This file contains functions to reference values across other files.

#### backend-deployment.yaml
This file takes care of the deployment of the backend pods, by providing a template after which the pods will be 
configured. This template will be filled with information from the `values.yaml`.

#### frontend-deployment.yaml
This file takes care of the deployment of the frontend pods, by providing a template after which the pods will be
configured. This template will be filled with information from the `values.yaml`.

#### hpa.yaml
This file provides a template for autoscaling, meaning the allocation of more computing power or replicas if needed.
This is currently disable in the values.yaml.

#### ingress.yaml
This file manages the external access onto the cluster, it contains rules to redirect requests to the corresponding 
service.

#### reverse-proxy-deployment.yaml
This file takes care of the deployment of the nginx reverse proxy, by providing a template after which the pods will be
configured. This template will be filled with information from the `values.yaml`.

#### reverse-proxy-service.yaml
This file configures the reverse proxy, so that it is accessible by other pods within the cluster.

#### services.yaml 
This file configures the pods, so that they are accessible by other pods within the cluster.

#### statefulset.yaml
This file takes care of the deployment of the database pods, by providing a template after which the pods will be
configured. This template will be filled with information from the `values.yaml`. It also creates the persistent 
volume claims, which links a database to its persistent volume.