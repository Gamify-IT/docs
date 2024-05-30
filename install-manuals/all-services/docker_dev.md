# Development with Docker
Each repository contains a `docker-compose-dev.yaml` file.
This file can be used to start the latest changes of the repository
with all necessary dependencies.

To do so, make sure your changes are pushed onto Github.
Then open a command prompt window in the directory of the `docker-compose-dev.yaml` 
file. There use the following commands to start and stop your docker container:

To start:
```sh
docker compose -f docker-compose-dev.yaml up
```
To stop:
```sh
docker compose -f docker-compose-dev.yaml down
```

Note:\
Since the development docker images are built whenever something is 
pushed to any branch except the main branch, it is advised that only 
one developer works on a repository at any given time. (Or at least changes are 
only made to one branch). If this is not the case the development image might not 
contain your changes, but those of your colleague if their changes were pushed more recently 
then yours.