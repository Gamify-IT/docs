# Use Docker Compose files with Unity

The usage of [Docker Compose files](docker-compose.md) with Unity projects differs from our other projects because we can't build the project in a docker container. Hence, no `docker-compose.yaml` exists.

To use our `docker-compose-dev.yaml` and `docker-compose-dev-e2e.yaml`, you have to build the WebGL-build yourself.

### WebGL build instructions

Firstly, open the build settings with `File` > `Build Settings`.  
![Opening the build settings](images/unity-open-build-settings.png)

Then you have to select `WebGL` and click `Build`.  
![Starting the build](images/unity-build-webgl.png)

Then you have to save it as `build` in the project's root directory.  
![Output](images/unity-build-output.png)

A `build` folder containing an `index.html` file and other data should exist now.