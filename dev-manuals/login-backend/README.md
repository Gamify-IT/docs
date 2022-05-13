# Login Backend
This Markdown file contains all necessary informations for developers about the Login Backend repository.

## Requirements
- Go https://go.dev 1.16 or higher
- GoLand: https://www.jetbrains.com/go/ for running start scripts in IDE
- Docker / Docker desktop: https://www.docker.com/products/docker-desktop to build and run as docker container
- (Postgres database)

## Starting with this repository
First, make sure Goland knows your Docker path: Check in 
`Files -> Settings -> Build, Execution, Deployment -> Docker`  
If in the left coloumn is no Docker registered, add Docker by clicking the top left add Button.

## Project structure

| File / Directory                     | Description                                                                               |
|--------------------------------------|-------------------------------------------------------------------------------------------|
| `main.go`                            | Entry point of the program                                                                |
| `swagger/`                           | Contains the API specification (Swagger)                                                  |
| `prisma/`                            | Database schema (Prisma)                                                                  |
| `src/handlers/`                      | Our HTTP handler implementations (Go)                                                     |
| `src/handlers/handlers.go`           | Adds all our handler functions to the server                                              |
| `src/gen/`                           | Generated files from Prisma and Swagger. Do not edit or commit generated files!           |
| `src/gen/restapi/configure_login.go` | Configuration for the HTTP server. The only file in `src/gen/` that can be safely edited. |

This repository contains run configurations which are loaded automatically when you open the project in GoLand. To run the project, select the go build configuration in the top right toolbar.

## Run application
You can run the application in three ways. 
- Directly from GoLand
- Command line with go commands
- Build docker image and run a container

### In IDE
The `go build` configuration (top right of GoLand) performs the following tasks for you:

- starts a postgres database with docker
- generates the Swagger code for the server
- generates the Prisma database client
- compiles & runs the project

### From command line
You need to run your own postgres database.
```sh
export PORT=4000
export POSTGRES_URL=postgresql://postgres:password@localhost:5432/postgres # Update credentials
export JWT_KEY=secretKey

go generate
go run github.com/prisma/prisma-client-go migrate deploy # When there is new database scheme, it needs to mirgrate
go run .

```

### From Dockerfile
You need to run your own postgres database.

#### Build docker image
```sh
docker build -t login-backend .
```
#### Start container
```sh
docker run --name login-backend -p 4000:4000 -e "POSTGRES_URL=postgresql://postgres:password@localhost:5432/postgres" -e "JWT_KEY=secretKey"
```


## Migrating the database
When changes to the database are made, you can create a migration by running
```sh
POSTGRES_URL=postgresql://postgres:password@localhost:5432/postgres go run github.com/prisma/prisma-client-go migrate dev --name $MIGRATION_NAME
```
inside the project root dir.\
To apply all pending migrations, simply run
```sh
POSTGRES_URL=postgresql://postgres:password@localhost:5432/postgres go run github.com/prisma/prisma-client-go migrate deploy
```
inside the project root dir.

## JWT (Json Web Tokens)
To encode a JWT, a secret key is needed. 
This secret key needs to be stored under the environment variable `JWT_KEY`.

## Go-Swagger
This Rest-API uses Go-Swagger. So the `swagger/swagger.yml` is the base of the rest api. You find documentation about the swagger.yml here: https://swagger.io/docs/specification/basic-structure/.

After changes were made in `swagger.yml` file you should run `go genrate` that the files will be generated. With the generated objects you can work.