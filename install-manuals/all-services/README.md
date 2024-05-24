# How to run all services via docker 

## Prerequisite

### Install docker

[Install Docker](https://docs.docker.com/engine/install/)

#### Docker Desktop (not recommended for production use)

[Install Docker Desktop on windows](https://docs.docker.com/desktop/windows/install/)

[Install Docker Desktop on linux](https://docs.docker.com/desktop/linux/install/)

[Install Docker Desktop on macos](https://docs.docker.com/desktop/mac/install/)

For additional information on the installation, refer to the [Docker Documentation](https://docs.docker.com/desktop/) under the 
install section for your respective operating system.

## Run
All services are available as docker containers. The preferred way to host is to use a `docker compose` file.
To run the whole application in docker go to the [run-config](https://github.com/Gamify-IT/run-config) repository.
In this repository we provide a script to set up the docker-compose file on your machine.
You just need to download the script and execute it. 

You should now see a new folder being created in the directory of the script. This folder should contain a 
`docker-compose.yaml` file. To execute this file with docker, open a terminal in the directory of the file 
and execute the following commands (while the docker engine is running): 

To start it you can use
```bash
docker compose up
```
To remove the containers you can use
```bash
docker compose down
```

In the future you can also you the graphical interface of docker desktop to start/stop the container.

## Usage
After the container started successfully you can open the app at [localhost](http://localhost).
Since you are using the application locally, no users or courses are created initially. 
If you want to create a new user with lecturer privileges (= can create and edit courses) refer to the [Keycloak Manual](./keycloak.md).
