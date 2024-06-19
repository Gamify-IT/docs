# Development with Docker
## General Information
Each repository has a `docker-compose.yaml` and `docker-compose-dev.yaml` file. Some repositories additionally have a `docker-compose-dev-e2e.yaml` or `docker-compose-complete.yaml` and `docker-compose-complete-dev.yaml` files.

In the following, the general usage of the first three files will be described, followed by the other files and some exceptions.

If nothing else is stated, the console commands should be run in the project root directory. 

## Functionality
### **docker-compose.yaml**
This file functions the same no matter if your repository is a frontend or backend. It provides all dependencies for your project (e.g. overworld, lecturer-interface, databases, etc.) and runs them as docker containers. \
Additionally it will build your local project files as a docker container and run this container as well.

To use this file, utilize the following console commands:
```sh
docker compose up --build
```
This command builds and starts the containers, while the second command removes the containers again.
```sh
docker compose down
```
Make sure that docker is installed and running on your machine, before executing these commands in the project directory.


### **docker-compose-dev.yaml**
This file also provides all necessary dependencies for the project, but it does not build your local changes as a docker container. Instead, it is intended to start the project locally with your IDE, so that you can use IDE-features such as hot-reload and debuggers.

To start up the dependencies, run the following command:
```sh
docker compose -f docker-compose-dev.yaml up
```
To remove the containers use:
```sh
docker compose -f docker-compose-dev.yaml down
```

You then need to start up the project locally. Make sure that you have all the needed tools and dependencies installed to do so, as described in the README of each repository.

#### Vue frontend
If your project is a vue frontend, the general process to run the project locally is as follows:
Make sure you have node.js installed.
When first opening the project, run:
```sh
npm install
```
to install all dependencies of the project.
You can then run:
```sh
npm run serve
```
to start up the project in development mode. \
You can access the minigames via the overworld, or directly with http://localhost/minigames/{minigame_name}.

#### Java backend
If you wish to start a java backend, make sure that [maven](https://maven.apache.org/download.cgi), [postgresql](https://www.postgresql.org/download/) and [java](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) are installed. \
Postgres needs to be running on your machine before compiling the project.

You can compile the project with:
```sh
mvn install
```
You then need to change into the target directory:
```sh
cd target
```
And start up the project jar file:
```sh
java -jar {minigame_name}-service-0.0.1-SNAPSHOT.jar
```

Since java is a compiled language, hot reload like with vue-js is not possible, you need to recompile the project and run the newly compiled files to make changes visible.
If you wish to test api requests, a tool like [postman](https://www.postman.com/downloads/) is recommended.

### **docker-compose-dev-e2e.yaml**
Some minigames also have this file in either their front- or backend repository. It serves the same purpose as the `docker-compose-dev.yaml` file, except it starts neither the frontend nor the backend of the minigame. This way, you could run both locally if you wish to. It is not recommended to use this file though, since it currently creates issues with your ports, since you can't run two different applications on the same port. 

To start the containers use:
```sh
docker compose -f docker-compose-dev-e2e.yaml up
```
To remove the containers use:
```sh
docker compose -f docker-compose-dev-e2e.yaml down
```

## Exceptions
### Regexgame
The regexgame frontend has a slightly different way to run the project. You can still use the `docker-compose.yaml` file like described above, but if you want to run the project locally, you need to follow these steps: \
First make sure to use VSCode, with the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension installed and active. You can then start the dependencies as described above. To run the project, you need to use:
```sh
npm run dev
```
You can then access the minigame at http://localhost/minigames/regexgame/ or via the overworld.

### Unity
Unity projects are an exception since they can't be run in your typical IDE (such as IntelliJ).
You can't build a local container of the project, therefore these repositories don't contain a `docker-compose.yaml` file. See [Docker with Unity](https://gamifyit-docs.readthedocs.io/en/latest/dev-manuals/languages/docker/docker-compose-unity.html) for more information (*unchecked information, may be inaccurate or incomplete*).

#### Chickenshock
Chickenshock contains a `docker-compose-dev.yaml` file, which works as described above, except you need to build the project with unity.

#### Overworld
The `docker-compose-dev.yaml` file in the overworld doesn't enable you to run the project locally, instead it pulls the latest image of the main branch from GitHub and runs it with the dependencies.

The `docker-compose-dev-e2e.yaml` file works the same, but it doesn't run the overworld-backend, so that you can run it locally.

### **docker-compose-complete.yaml and docker-compose-complete-dev.yaml**
These files are an exception to the overworld-backend. They work exactly like their 'non-complete' counterpart, with the difference that the 'non-complete' versions only run the bare minimum, meaning no minigames, where as the 'complete' version run all minigames as containers.
