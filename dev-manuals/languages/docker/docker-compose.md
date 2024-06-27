# Use Docker Compose Files

**Deprecated/Incomplete, refer to [Development with Docker](../../../install-manuals/all-services/docker_dev.md)**

Manual to use our Docker Compose files to get a minimal setup with all dependencies.
The Docker Compose makes the services accessible at [http://localhost](http://localhost).

## Run everything in Docker

To run everything inside Docker you can use our `docker-compose.yaml` file (Not available in unity projects). 
It builds the container locally and starts it with all dependencies. \
This is useful to test the Docker build or when you want to test PR reviews.

To start it you can use
```bash
docker compose up --build
```
To remove the containers you can use
```bash
docker compose down
```

## Run the project locally

Many repositories contain a `docker-compose-dev.yaml` file. This file can be used to test the repository 
with all the needed dependencies. To do so, open a terminal in the directory of the file (should be the base 
of the repository) and execute the following commands:

To start it you can use
```bash
docker compose -f docker-compose-dev.yaml up
```
To remove the containers you can use
```bash
docker compose -f docker-compose-dev.yaml down
```

This is useful to test the project while developing and use all your IDE features (debugger, hot-reload, ...).


### Unity

In unity projects you have to build a WebGL-build into the `build` folder. Get more hints [here](docker-compose-unity.md)

## Run frontend and backend locally

To run the frontend and backend outside Docker you can use our `docker-compose-dev-e2e.yaml` file which is placed in the frontend. 
It starts all dependencies with a reverse proxy pointing to your local backend and frontend development server. \
This is useful to test the project while developing frontend and backend and use all your IDE features (debugger, hot-reload, ...).

To start it you can use
```bash
docker compose -f docker-compose-dev-e2e.yaml up
```
To remove the containers you can use
```bash
docker compose -f docker-compose-dev-e2e.yaml down
```

### Unity

In unity projects you have to build a WebGL-build into the `build` folder. Get more hints [here](docker-compose-unity.md).
