# Login Backend
This Markdown file contains all necessary informations for end users about the Login Backend repository.

## Requirements
- Go https://go.dev 1.16 or higher
- Docker https://www.docker.com/ to run docker containers
- Postgres database

## Run application
You can run the application in two ways. 
- Command line with go commands
- Build docker image and run a container

### From command line
You need to run your own postgres database.
```sh
export PORT=4000
export POSTGRES_URL=postgresql://<user>:<password>@<host>:<url>/<database> # Update key words in '<>' with your credentials 
export JWT_KEY=secretKey

go generate
go run github.com/prisma/prisma-client-go migrate deploy # When there is new database scheme, it needs to mirgrate
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
docker run --name login-backend -p 4000:4000 -e "POSTGRES_URL=postgresql://<user>:<password>@<host>:<url>/<database>" -e "JWT_KEY=secretKey"
```
Update key words in '<>' with your credentials 


## Migrating the database
When changes to the database are made, apply all pending migrations, simply run
```sh
POSTGRES_URL=postgresql://<user>:<password>@<host>:<url>/<database> go run github.com/prisma/prisma-client-go migrate deploy
```

## JWT (Json Web Tokens)
To encode a JWT, a secret key is needed. 
This secret key needs to be stored under the environment variable `JWT_KEY`.
KEEP IT PRIVATE!
