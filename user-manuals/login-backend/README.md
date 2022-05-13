# Login Backend
This Markdown file contains all necessary informations for end users about the Login Backend repository.

## Requirements
- [Go](https://go.dev) 1.16 or higher
- [Docker](https://www.docker.com/) to run docker containers
- [Postgres](https://www.postgresql.org/) database

## Run application
You can run the application in two ways. 
- Command line with go commands
- Build docker image and run a container

### From command line
You need to run your own postgres database.
```sh
export PORT=4000
export POSTGRES_URL=postgresql://<user>:<password>@<host>:<url>/<database> # Update key words in '<>' with your credentials 
export JWT_KEY=<some secret key>

go generate
go run github.com/prisma/prisma-client-go migrate deploy # Migrate database scheme if it has changed
go run .
```

### From Dockerfile

#### Build docker image
```sh
docker build -t login-backend .
```
Or get it from our Github Package Registry if you have access to it
```sh
docker pull ghcr.io/gamify-it/login-backend:latest
```

#### Start container
```sh
docker run --name login-backend -p 4000:4000 -e "POSTGRES_URL=postgresql://<user>:<password>@<host>:<url>/<database>" -e "JWT_KEY=<secret key>"
```
Replace `<.*>` with the corresponding credentials.


## Updating
When you update the login backend, changes to the database could have been made, so make sure to migrate the database structure simply by running
```sh
POSTGRES_URL=postgresql://<user>:<password>@<host>:<url>/<database> go run github.com/prisma/prisma-client-go migrate deploy
```

## JWT (Json Web Tokens)
To encode a JWT, a secret key is needed. 
This secret key needs to be stored under the environment variable `JWT_KEY`.
KEEP IT PRIVATE!
