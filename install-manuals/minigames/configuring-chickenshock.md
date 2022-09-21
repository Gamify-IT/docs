# Chickenshock

## Table of contents

<!-- TOC -->
* [Configuration](#configuration)
  * [Frontend](#frontend)
  * [Backend](#backend)
<!-- TOC -->

## Configuration

Currently, the following things can be configured.

### Frontend

In the [frontend](https://github.com/Gamify-IT/chickenshock) the following properties can be configured:

- `getQuestions` the URL path to the backend endpoint that returns the questions
- `saveRound` the URL path to the backend endpoint that saves the results of the game round
- `editorGetQuestions` when debugging in Unity: the URL path to the backend endpoint that returns the questions for the editor.
- `editorConfiguration` when debugging in Unity: fixed fallback configuration ID for testing
- `correctFeedbackText` the text displayed when the player answers a question correctly
- `wrongFeedbackText` the text displayed when the player answers a question incorrectly

These settings can be changed in the [frontend](https://github.com/Gamify-IT/chickenshock) by editing the file `Assets/Scripts/Properties/Chickenshock.properties`.

### Backend

The [backend](https://github.com/Gamify-IT/chickenshock-backend) can be configured via environment variables.
Alternatively you can edit the file `src/main/resources/application.properties`.

| Spring Property               | Environment variable          | Description                                                      | Default value                                |
|-------------------------------|-------------------------------|------------------------------------------------------------------|----------------------------------------------|
| `spring.sql.init.platform`    | `SPRING_SQL_INIT_PLATFORM`    | The kind of database you are using                               | `postgres`                                   |
| `spring.datasource.url`       | `SPRING_DATASOURCE_URL`       | The URL to the database                                          | `jdbc:postgresql://localhost:5432/postgres`  |
| `spring.datasource.username`  | `SPRING_DATASOURCE_USERNAME`  | The username to connect to the database                          | `postgres`                                   |
| `spring.datasource.password`  | `SPRING_DATASOURCE_PASSWORD`  | The password to connect to the database                          | `postgres`                                   |
| `server.servlet.context-path` | `SERVER_SERVLET_CONTEXT_PATH` | Base path for the API                                            | `/api/v1`                                    |
| `overworld.url`               | `OVERWORLD_URL`               | URL of the overworld backend service                             | `http://localhost/overworld/api/v1`          |
| `keycloak.issuer`             | `KEYCLOAK_ISSUER`             | Name of the issuer used in the authentication tokens             | `http://localhost/keycloak/realms/Gamify-IT` |
| `keycloak.url`                | `KEYCLOAK_URL`                | URL to connect to keycloak in order to fetch the validation keys | `http://localhost/keycloak/realms/Gamify-IT` |
| `springdoc.swagger-ui.path`   | `SPRINGDOC_SWAGGER_UI_PATH`   | Path to serve the API documentation                              | `/swagger-ui`                                |

A complete list of options can be seen in the [backend](https://github.com/Gamify-IT/chickenshock-backend) in `src/main/resources/application.properties`.
