# [Crosswordpuzzle](https://github.com/Gamify-IT/crosswordpuzzle)

This is a simple crosswordpuzzle. With given questions and answers it automatically generates a crosswordpuzzle.  

---

## Getting started

Clone the repository  

```sh
git clone https://github.com/Gamify-IT/crosswordpuzzle.git
```

Install the dependencies  

```sh
npm install
```

## Compile and Hot-Reload for Development

```sh
npm run dev
```

## Build

Build the Docker-Container

```sh
docker build -t crosswordpuzzle-dev
```

And run it at port 8000 with

```sh
docker run -d -p 8000:80 --name crosswordpuzzle-dev crosswordpuzzle-dev
```

To monitor, stop and remove the container you can use the following commands:

```sh
docker ps -a -f name=crosswordpuzzle-dev
```

```sh
docker stop crosswordpuzzle-dev
```

```sh
docker rm crosswordpuzzle-dev
```
