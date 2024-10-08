# Integrate a completely new minigame

## Table of content

- [Integrate a completely new minigame](#integrate-a-completely-new-minigame)
  - [Table of content](#table-of-content)
  - [Getting started](#getting-started)
  - [Minigame structure](#minigame-structure)
    - [Backend: Configuration routes](#backend-configuration-routes)
  - [Integrate into the reverse proxy and the run config](#integrate-into-the-reverse-proxy-and-the-run-config)
    - [Reverse proxy repository](#reverse-proxy-repository)
    - [Run config (deployment)](#run-config-deployment)
    - [Docker deployment](#docker-deployment)
  - [Integrate into the overworld backend](#integrate-into-the-overworld-backend)
    - [Add the minigame to the `Minigame` enum](#add-the-minigame-to-the-minigame-enum)
    - [Add FeignClient](#add-feignclient)
    - [Implement configuration cloning](#implement-configuration-cloning)
  - [Integrate cloning into the minigame:](#integrate-cloning-into-the-minigame)
  - [Integrate into the lecturer interface](#integrate-into-the-lecturer-interface)
    - [Add the minigame as enum](#add-the-minigame-as-enum)
    - [Add DTOs](#add-dtos)
    - [Add a REST client](#add-a-rest-client)
    - [Create a configuration modal](#create-a-configuration-modal)
      - [Add configuration import/ export](#add-configuration-import-export)
  - [Backend-to-backend communication](#backend-to-backend-communication)

## Getting started

This document shows how to integrate a new minigame.  
The new minigame usually consists of two microservices, a frontend and a backend.  
After this tutorial, this minigame will be playable from the overworld, the minigame backend will submit statistics to the overworld backend, and the lecturer interface will allow to configure the minigame.


## Minigame structure

As described above, both frontend and backend of the minigame should exist already. 

### Backend: Configuration routes

In order to provide a uniform interface for minigame configurations in all minigame backends, both the routes `/configurations` (for `POST` and GET), and `/configurations/{id}` where `id` is a `UUID` (for `PUT` and `GET`), must exist.

## Integrate into the reverse proxy and the run config 

To ensure all REST requests function correctly, the following changes need to be made:

### Reverse proxy repository

- Add the minigame name to the service env in the `Dockerfile`:
  ``` dockerfile
  ENV SERVICES="default keycloak bugfinder chickenshock crosswordpuzzle fileserver finitequiz memory regexgame towercrush towerdefense <YOUR_MINIGAME_NAME>"
  ```
- Update the `body-main.conf`:
  ``` config
  set $<YOUR_MINIGAME_NAME> ###DEPLOYMENT_NAME###-<YOUR_MINIGAME_NAME>###LOCAL_DOMAIN###;
  set $<YOUR_MINIGAME_NAME> ###DEPLOYMENT_NAME###-<YOUR_MINIGAME_NAME>-backend###LOCAL_DOMAIN###;
- Add a new `body-<YOUR_MINIGAME_NAME>.conf`:
  ``` config
  location /minigames/<YOUR_MINIGAME_NAME>/ {
        rewrite    ^/minigames/<YOUR_MINIGAME_NAME>/(.*)$ /$1 break;
        proxy_pass      http://$<YOUR_MINIGAME_NAME>;
    }

    location /minigames/<YOUR_MINIGAME_NAME>/api/ {
        rewrite    ^/minigames/minigame/(.*)$ /$1 break;
        proxy_pass      http://$<YOUR_MINIGAME_NAME>_backend;
    }
  ```
### Run config (deployment)

- Add the minigame name to the service env in the `create-deployment.sh`:
  ```shell
  SERVICES="default keycloak bugfinder chickenshock crosswordpuzzle fileserver finitequiz memory regexgame towercrush <YOUR_MINIGAME_NAME>"
  ```
- Create a new `docker-compose-<YOUR_MINIGAME_NAME>.yaml`:
  ``` docker
  version: "3.8"

  services:

    <YOUR_MINIGAME_NAME>-db:
      extends:
        file: docker-compose-template-services.yaml
        service: template-db
      container_name: ${DEPLOYMENT_NAME}-<YOUR_MINIGAME_NAME>-db
      volumes:
      - <YOUR_MINIGAME_NAME>-db:/var/lib/postgresql/data

    <YOUR_MINIGAME_NAME>-backend:
      extends:
        file: docker-compose-template-services.yaml
        service: template-backend
      container_name: ${DEPLOYMENT_NAME}-<YOUR_MINIGAME_NAME>-backend
      image: ghcr.io/gamify-it/<YOUR_MINIGAME_NAME>-backend:$VERSION
      depends_on:
        - <YOUR_MINIGAME_NAME>-db
      environment:
        - POSTGRES_URL=postgresql://${DEPLOYMENT_NAME}-<YOUR_MINIGAME_NAME>-db:5432/postgres

    <YOUR_MINIGAME_NAME>:
      extends:
        file: docker-compose-template-services.yaml
        service: template-frontend
      container_name: ${DEPLOYMENT_NAME}-<YOUR_MINIGAME_NAME>
      image: ghcr.io/gamify-it/<YOUR_MINIGAME_NAME>:$VERSION

  volumes:
    <YOUR_MINIGAME_NAME>-db:
      name: ${DEPLOYMENT_NAME}-<YOUR_MINIGAME_NAME>-db
  ```

### Docker deployment

To integrate the minigame into the `docker-compose.yaml` files of a repository,
you need to add the necessary services, such as the frontend, backend and database, as needed.

## Integrate into the overworld backend

### Add the minigame to the `Minigame` enum

Add `YOUR_MINIGAME` to the `Minigame` enum in `de.unistuttgart.overworldbackend.data.enums.Minigame`

### Add FeignClient

A `FeignClient` needs to be configured to communicate with your REST-API.
Add the class `<YOUR_MINIGAME_NAME>Client` to the package `de.unistuttgart.overworldbackend.client`.
The code in this class should look like following:

```java
@FeignClient(value = "finitequizClient", url = "${finitequiz.url}/configurations")
public interface FinitequizClient {
  @PostMapping("/{id}/clone")
  UUID postClone(@CookieValue("access_token") final String accessToken, @PathVariable UUID id);
}
```
Also add the url to the minigame backend in `application.properties`, e.g.:

```properties
<YOUR_MINIGAME_NAME>.url= http://localhost/minigames/<YOUR_MINIGAME_NAME>/api/v1
```
From now the overworld backend is able to make requests to the minigame backend.

### Implement configuration cloning

You need the `FeignClient` created above to not break course cloning.

Edit the method `de.unistuttgart.overworldbackend.service.CourseService#cloneMinigameTask`.
This method is responsible to clone the minigames of a course, so that a new minigame task gets the same configuration, but with a new ID.  
This is needed because the configuration ID of tasks must be unique. Add the case for your minigame in the switch statement, e.g.:

```java
case <YOUR_MINIGAME_NAME>:
        cloneId = <YOUR_MINIGAME_NAME>Client.postClone(accessToken, minigameTask.getConfigurationId());
        break;
```
The code snippet above is an example to clone a configuration with questions.

## Integrate cloning into the minigame:

The backend of the minigame has to provide a route to clone a configuration preferably at `/configurations/{id}/clone`.
This logic should deep copy a configuration (without the object IDs) for example by implementing the `clone()` method in every object.
Additionally, the minigame should validate that only lecturers can clone a configuration.
It can do this by requiring a cookie (we recommend the cookie name `access_token` to conform with all other minigames) for the request that is a [JWT token](https://jwt.io/) that, when verified, should have the role `lecturer`.

## Integrate into the lecturer interface

### Add the minigame as enum

Add `YOUR_MINIGAME` to the Minigame enum in `overworld-models.ts` in the package `ts.models`.

### Add DTOs

You need a copy of your `Configuration` class and subsequent classes called by it in the lecturer interface.
Add these DTOs in the package `ts.models`.
For example:

```typescript
export class <YOUR_MINIGAME_NAME>Configuration {
  id?: string;
  name: string;
  questions: <YOUR_MINIGAME_NAME>Question[];

  public constructor(name: string, questions: <YOUR_MINIGAME_NAME>Question[]) {
    this.name = name;
    this.questions = questions;
  }
}

export class <YOUR_MINIGAME_NAME>Question {
  id?: string;
  questionText: string;
  answer: string;

  public constructor(questionText: string, answer: string) {
    this.questionText = questionText;
    this.answer = answer;
  }
}
```

### Add a REST client

Add the URL of the backend in the `config.ts`

```typescript
<YOUR_MINIGAME_NAME>ApiUrl: "/minigames/<YOUR_MINIGAME_NAME>/api/v1",
```

Add a class <YOUR_MINIGAME_NAME>-rest-client.ts in package `ts.rest-clients`, e.g.

```typescript
import axios, { AxiosResponse } from "axios";

import config from "@/config";

import { <YOUR_MINIGAME_NAME>Configuration } from "@/ts/models/<YOUR_MINIGAME_NAME>-models";

export async function post<YOUR_MINIGAME_NAME>Config(
  <YOUR_MINIGAME_NAME>Config: <YOUR_MINIGAME_NAME>Configuration
): Promise<AxiosResponse> {
  return axios.post(
    `${config.<YOUR_MINIGAME_NAME>ApiUrl}/configurations`,
    <YOUR_MINIGAME_NAME>Config
  );
}

export async function get<YOUR_MINIGAME_NAME>Config(
  id: string
): Promise<AxiosResponse> {
  return axios.get(`${config.<YOUR_MINIGAME_NAME>ApiUrl}/configurations/${id}`);
}
```

### Create a configuration modal

Create a new configuration modal under the package `components.EditMinigameModals`.  
We can't document exactly what the code should look like, as it varies a lot, but you can orient yourself on the existing edit components.  
It is important that the minigame configurations are loaded and updated in the component.  
When a modal gets closed, emit `closedModal` and when a configuration gets updated emit `updateMinigameConfiguration`.

The minigames edit view is in the class `MinigameTasksView.vue` under the package `views`.

Create a new variable:

```typescript
const show<YOUR_MINIGAME_NAME>Modal = ref(false);
```

Add your minigame in the `editMinigameConfiguration` method:

```typescript
case Minigame.<YOUR_MINIGAME_NAME>:
    show<YOUR_MINIGAME_NAME>Modal.value = true;
    break;
```

Append the following at the bottom of the `closedEditModal` method:

```typescript
show<YOUR_MINIGAME_NAME>Modal.value = false;
```

Add the new edit modal. Put the modal after the other modals at the bottom of the file.

```typescript
<Edit<YOUR_MINIGAME_NAME>Modal
    :showModal="show<YOUR_MINIGAME_NAME>Modal"
    :minigame="editedMinigame"
    @updateMinigameConfiguration="updateMinigameConfiguration"
    @closedModal="closedEditModal"
  />
```

#### Add configuration import/ export

Go in the edit modal component of the minigame. 
You need following imports:

```typescript
import { saveAs } from "file-saver";
import { arrayOf, defaultValue, object, string, int } from "checkeasy"; // depends on your configuration attributes
import { importConfiguration } from "@/ts/import-configuration";
import ImportExportConfiguration from "@/components/ImportExportConfiguration.vue";
```

To make a configuration downloadable, create the method downloadConfiguration:

```typescript
function downloadConfiguration() {
  const { ["id"]: unused, ...clonedConfiguration } = configuration.value;
  const clonedQuestions = Array<<YOUR_MINIGAME_NAME>Question>();
  for (let question of configuration.value.questions) {
    const { ["id"]: unused, ...clonedQuestion } = question;
    clonedQuestions.push(clonedQuestion);
  }
  clonedConfiguration.questions = clonedQuestions;
  const blob = new Blob([JSON.stringify(clonedConfiguration)], {
    type: "text/json",
  });
  saveAs(blob, "<YOUR_MINIGAME_NAME>-configuration.json");
}
```
This exports the configuration object as json without their IDs.

Of course we need also a importFile method:

```typescript
async function importFile(event: any) {
  const file = event.target.files[0];
  const validator = object({
    time: defaultValue(60, int()),
    questions: arrayOf(
      object({
        text: string(),
        rightAnswer: string(),
        wrongAnswers: arrayOf(string()),
      })
    ),
  });
  try {
    const result: <YOUR_MINIGAME_NAME>Configuration = await importConfiguration(
      file,
      validator,
      toast
    );
    configuration.value = result;
  } catch (e) {
    console.log("Import was not successful");
  }
}
```
The validator depends on the attributes of the configuration class. You need to customize the validator to match your configuration class. More information about the library can be found [here](https://github.com/smbwain/checkeasy/blob/master/README.md).

Finally the component to import and export a file needs to be added, which displays a import and an export button. Simply add the following code in your modal:

```php
<ImportExportConfiguration
    @export="downloadConfiguration"
    @importFile="importFile"
/>
```

## Backend-to-backend communication

The minigame backend must send a score after every player's game run to the overworld backend after a player's playthrough. The score must be a natural number between `0` and `100`, where `100` means "no further improvements possible"  and `0` means "everything is wrong".  
The minigame backend is responsible for calculating this score, the overworld backend simply stores it. 

The following shows how to do it in Java with `Spring`, `Lombok`, and `FeignClient`.

First, create the `OverworldResultDTO`:

```java
/**
 * The class to specify all details the overworld backend needs to
 * submit a game result of a player.
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
public class OverworldResultDTO {

  final String game = "<YOUR_MINIGAME_NAME>";
  UUID configurationId;
  long score;
  String userId;
}
```

Add the url of the overworld backend in `application.properties`:

```properties
overworld.url= http://localhost/overworld/api/v1
```

Create the ResultClient

```java
@FeignClient(value = "resultClient", url = "${overworld.url}/internal")
public interface ResultClient {
  @PostMapping("/submit-game-pass")
  void submit(OverworldResultDTO resultDTO);
}
```

Implement somewhere in your minigame backend the logic to send the game results:

```java
@Autowired
private ResultClient resultClient;

public void saveGameResult(final GameResultDTO gameResultDTO, final String userId) {
    final OverworldResultDTO resultDTO = new OverworldResultDTO(
      gameResultDTO.getConfigurationId(),
      calculateScore(gameResultDTO), // needs to be written
      userId
    );
    try {
      resultClient.submit(resultDTO);
    } catch (final FeignException.BadGateway badGateway) {
      final String warning =
        "The Overworld backend is currently not available. The result was NOT saved. Please try again later.";
      log.warn(warning, badGateway);
      throw new ResponseStatusException(HttpStatus.SERVICE_UNAVAILABLE, warning);
    } catch (final FeignException.NotFound notFound) {
      String warning = String.format("The result could not be saved. Unknown User '%s'.", userId);
      log.warn(warning, notFound);
      throw new ResponseStatusException(HttpStatus.NOT_FOUND, warning);
    }
  }
```
