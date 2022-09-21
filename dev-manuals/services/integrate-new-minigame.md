# Table of content

* [Getting started](#getting-started)
    * [Minigame structure](#minigame-structure)
    * [Integrate the new minigame in the overworld backend](#integrate-the-new-minigame-in-the-overworld-backend)
    * [Integrate the new minigame in the lecturer interface](#integrate-the-new-minigame-in-the-lecturer-interface)
    * [Integrate the new minigame in the lecturer interface](#send-game-results-from-the-minigame-backend-to-the-overworld-backend)

# Getting started

This document presents an overview, how a minigame can be integrated to the project. The new minigame usually contains two microservices, a frontend and a backend. With this documentation, the developer is able to integrate the minigame to make the game playable from the overworld, player game runs will be submitted to the overworld backend, the minigame can be configured trough the lecturer interface and cloning courses with the new minigame works.


## Minigame structure

As described in the beginning, the minigame contains a backend and a frontend. 

### Provide a configurations interface in the backend

In order to provide a uniform interface for minigame configurations in all minigame backends, create an interface `/configurations` with POST and GET and `/configurations/{id}` where id is a `UUID` with PUT and GET to create, update and fetch configurations.

## Integrate the new minigame in the overworld backend

### Add the minigame in the minigames enum class:

Add `YOUR_MINIGAME` in `Minigame` enum class under folder `de.unistuttgart.overworldbackend.data.enums`

### Add required Data Transfer Objects in the overworld backend

Add required Data Transfer Objects like the Configurations class and potentially Question classes (depends on your data models) in the package `de.unistuttgart.overworldbackend.data.minigames.<YOUR_MINIGAME_NAME>`.
Example Configuration class:
```java
@Data
@FieldDefaults(level = AccessLevel.PRIVATE)
public class <YOUR_MINIGAME_NAME>Configuration {

    UUID id;
    Set<<YOUR_MINIGAME_NAME>Question> questions;
}
```

### Add FeignClient

A `FeignClient` needs to be configured to communicate with your REST-API.
Add the class `<YOUR_MINIGAME_NAME>Client` to the package `de.unistuttgart.overworldbackend.client`.
The code in this class should look like following:
```java
@FeignClient(value = "<YOUR_MINIGAME_NAME>Client", url = "${<YOUR_MINIGAME_NAME>.url}/configurations")
public interface BugfinderClient {
  @GetMapping("/{id}")
  BugfinderConfiguration getConfiguration(
    @CookieValue("access_token") final String accessToken,
    @PathVariable("id") UUID id
  );

  @PostMapping("/")
  BugfinderConfiguration postConfiguration(
    @CookieValue("access_token") final String accessToken,
    BugfinderConfiguration bugfinderConfiguration
  );
}
```
Also add the url to the minigame backend in `application.properties`, e.g.:
```properties
<YOUR_MINIGAME_NAME>.url= http://localhost/minigames/<YOUR_MINIGAME_NAME>/api/v1
```
From now the overworld backend is able to make requests to the minigame backend.

### Support course cloning with the new minigame

To support course cloning the `FeignClient` for the minigame backend is needed.

Enter the class `CourseService` in the package `de.unistuttgart.overworldbackend.service`. The method `cloneMinigameTask` in this class in responsible to clone the minigames of a course, so that a new course gets the same configuration, but with new configuration ids. This is important, because two minigame tasks (do not care if they are the same course or not) are not allowed to have a same configuration id. In the method `cloneMinigameTask` you have to integrate the cloning process of your minigame. Add the case of your new minigame in the switch statement, e.g.:

```java
case <YOUR_MINIGAME_NAME>:
    if (minigameTask.getConfigurationId() == null) {
        return new MinigameTask(
            Minigame.<YOUR_MINIGAME_NAME>,
            minigameTask.getDescription(),
            null,
            minigameTask.getIndex()
        );
    } else {
        <YOUR_MINIGAME_NAME>Configuration config = <YOUR_MINIGAME_NAME>Client.getConfiguration(
            currentAccessToken,
            minigameTask.getConfigurationId()
        );
        config.setId(null);
        config.getQuestions().forEach(question -> question.setId(null));
        config = <YOUR_MINIGAME_NAME>Client.postConfiguration(currentAccessToken, config);
        return new MinigameTask(
            Minigame.<YOUR_MINIGAME_NAME>,
            minigameTask.getDescription(),
            config.getId(),
            minigameTask.getIndex()
        );
    }
```
The code snippet above is an example to clone a configuration with questions.

## Integrate the new minigame in the lecturer interface

### Add the minigame as enum

Add `YOUR_MINIGAME` in `overworld-models.ts` the Minigame enum in package `ts.models`

### Add required Data Transfer Objects

Add required Data Transfer Objects like the Configurations class and potentially Question classes (depends on your data models) in the package `ts.models`.
Example:
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

### Add a rest client

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

Create a new configuration modal under the paclage `components.EditMinigameModals`.
We can't document exactly what the code should look like, as it varies a lot, but you can orient yourself on the existing edit components. It is important to say that the minigame configurations should be loaded and updated in the component. When a modal gets closed call an `closedModal emit` and when a configuration gets updated call a `updateMinigameConfiguration emit`.

The minigames edit view is in the class `MinigameTasksView.vue` under the package `views`.

Create a new variable:
```typescript
const show<YOUR_MINIGAME_NAME>Modal = ref(false);
```

Add in the editMinigameConfiguration method your minigame:
```typescript
case Minigame.<YOUR_MINIGAME_NAME>:
    show<YOUR_MINIGAME_NAME>Modal.value = true;
    break;
```

Add in the closedEditModal method following at the bottom:
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

#### Integrate import/export in the edit modal

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
```typescript
<ImportExportConfiguration
    @export="downloadConfiguration"
    @importFile="importFile"
/>
```

## Send game results from the minigame backend to the overworld backend

The minigame backend must send a score after every player's game run to the overworld backend after a player's playthrough. The score must be between 0 and 100, where 100 is a completely correct run and 0 is a completely wrong run. The score must be calculated by the minigame backend itself. 

Create the OverworldResultDTO:
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