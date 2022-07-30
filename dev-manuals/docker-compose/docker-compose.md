# Use Docker Compose Files

Manual to use our Docker Compose files to get a minimal setup with all dependencies.

## Run everything in Docker

To run everything inside Docker you can use our `docker-compose.yaml` file (Not available in unity projects). 
It builds the container locally and starts it with all dependencies. \
This is useful to test the Docker build or when you want to test PR reviews.

To start it you can use
```bash
docker compose up
```
To remove the containers you can use
```bash
docker compose down
```

## Run the project locally

To run the project outside Docker you can use our `docker-compose-dev.yaml` file. 
It starts all dependencies with a reverse proxy pointing to your local development server. \
This is useful to test the project while developing and use all your IDE features (debugger, hot-reload, ...).

To start it you can use
```bash
docker compose -f docker-compose-dev.yaml up
```
To remove the containers you can use
```bash
docker compose -f docker-compose-dev.yaml down
```

#### Unity
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

#### Unity
In unity projects you have to build a WebGL-build into the `build` folder. Get more hints [here](docker-compose-unity.md)