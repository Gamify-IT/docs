# Deploying on Kubernetes

The _Gamify-IT_ architecture stack is intended to be deployed using _Docker Compose_.  
It is, however, possible to also deploy it on a _Kubernetes_ cluster.

## Prerequisites

1. A running Kubernetes cluster that can be accessed using `HTTPS`
2. `kubectl`
3. `kubectl` can access the cluster and create new pods
4. An internet connection
5. A shell/ command line tool to interact with your Computer, i.e. `bash` or `PowerShell`

## Deployment steps

1. [Install _Kompose_](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/#install-kompose) (if not present already)
1. Download the [main `docker-compose.yml`](https://raw.githubusercontent.com/Gamify-IT/run-config/main/docker-compose.yml). For your own sake, download it into a **newly created** directory without other files. If you intend to keep the artifacts of this process, choose wisely where
1. Navigate to the directory where you installed the `docker-compose.yml` in
1. Download the nginx [`default.conf`](https://raw.githubusercontent.com/Gamify-IT/run-config/main/nginx/conf.d/default.conf) into the same directory, i.e. using `curl -o default.conf https://raw.githubusercontent.com/Gamify-IT/run-config/main/nginx/conf.d/default.conf`
1. Adapt the `default.conf` to suit your needs, especially removing or adapting the SSL section
1. Execute `kubectl create configmap reverse-proxy-config --from-file=default.conf`
1. Execute `kompose convert`
1. Remove `reverse-proxy-claim0-persistentvolumeclaim.yaml` and `watchtower-*.yaml`. Those files are only needed when deploying from _Docker Compose_.
1. Replace
```yaml
- mountPath: /etc/nginx/conf.d
  name: reverse-proxy-claim0
  readOnly: true
```
with
```yaml
- mountPath: /etc/nginx/default.conf
  name: reverse-proxy-config
  subPath: default.conf
```
and
```yaml
- name: reverse-proxy-claim0
  persistentVolumeClaim:
    claimName: reverse-proxy-claim0
    readOnly: true
```
with
```yaml
- name: reverse-proxy-config
  configMap:
    name: reverse-proxy-config
    items:
      - key: default.conf
        path: default.conf
```
in `reverse-proxy-deployment.yaml`
1. Optional: move the `docker-compose.yml` up a directory to prevent showing an unimportant error in the next step
1. Execute `kubectl apply -f .`
1. Copy the nginx config into the reverse-proxy nginx volume: `kubectl cp default.conf reverse-proxy:/etc/nginx/conf.d/default.conf`
1. Restart the Pod: `kubectl get deployment reverse-proxy -o yaml && kubectl apply -f reverse-proxy-deployment.yaml`
1. Optional: Move the `docker-compose.yml` back into this directory
1. Optional: Remove this directory. The files are no longer explicitly needed, except for reproducibility in case you want to reset to this specific state at some point later in time

