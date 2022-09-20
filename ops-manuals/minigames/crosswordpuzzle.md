# [Crosswordpuzzle](https://github.com/Gamify-IT/crosswordpuzzle)

This is a simple crosswordpuzzle. With given questions and answers it automatically generates a crosswordpuzzle.  

---

Run the docker container with the following command at port 8000:

```sh
docker run -d -p 8000:80 --name crosswordpuzzle ghcr.io/gamify-it/crosswordpuzzle:latest
```

Now you can access it at [http://localhost:8000](http://localhost:8000).  
To access it externally replace localhost with your IP.  

To monitor the container you can use the following command:

```sh
docker ps -a -f name=crosswordpuzzle
```

To stop the container you can use the following command:

```sh
docker stop crosswordpuzzle
```

To remove the container you can use the following command:

```sh
docker rm crosswordpuzzle
```

## Screenshot

![example auto generated crosswordpuzzle](https://user-images.githubusercontent.com/44726248/169154288-f37c3e86-d8ad-4e78-b2a3-c2cb6645a2d7.png "crosswordpuzzle")
