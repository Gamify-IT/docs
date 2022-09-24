# Architecture of Chickenshock-backend

Chickenshock is a minigame which is part of the Gamify-IT platform.
The intention with this game is to make answering single choice questions fun.

## Table of Contents

* [Links](#links)
* [General code structure](#general-code-structure)
* [Starting the service](#starting-the-service)
* [What to look at](#what-to-look-at)
* [What to ignore](#what-to-ignore)
* [Class diagrams](#class-diagrams)
  * [Overview complete application](#overview-complete-application)
  * [ConfigController](#configcontroller)
  * [GameResultController](#gameresultcontroller)
* [Known Design Flaws](#known-design-flaws)
* [Known Bugs](#known-bugs)
* [Tests](#tests)

## Links

- The [user docs](../../../user-manuals/minigames/chickenshock.md) explain how to play the game.
- The program code is available at [here](https://github.com/Gamify-IT/chickenshock-backend).
- The overview of the architecture can be found [here](../overview.md).

## General code structure

This [Java code of the backend](https://github.com/Gamify-IT/finite-quiz-backend/blob/adef8dd1e681d655d26852d7c5741e254db16e57/src/main/java/de/unistuttgart/finitequizbackend) has the following package structure
- `data`: Contains the data objects and DTOs
- `controllers`: Containers the server routes
- `services`: Contains the business logic
- `clients`: Contains the b2b (backend-2-backend) communication methods
- `repositories`: Contains the database repositories


## Starting the service

See the [README](https://github.com/Gamify-IT/chickenshock-backend#readme).

## What to look at

The controllers for the API requests are a good point to start.
From there you can follow the code flow to the other components.

- The [GameController](https://github.com/Gamify-IT/moorhuhn-backend/blob/c6e06e04b968c9db81eb946061f9f07e89a56afc/src/main/java/de/unistuttgart/chickenshockbackend/controller/GameResultController.java) provides the API for the game results.
- The [ConfigurationController](https://github.com/Gamify-IT/moorhuhn-backend/blob/c6e06e04b968c9db81eb946061f9f07e89a56afc/src/main/java/de/unistuttgart/chickenshockbackend/controller/ConfigController.java) provides the API to configure the game.

## What to ignore

Everything is ready for review.

## Class diagrams

### Overview complete application
![overview class diagram of complete application](assets/chickenshockClassOverview.webp)
This simplified class diagram shows how the most important services, mappers and repositories in the project are interlinked.

### ConfigController
![class diagram of ConfigController](assets/chickenshockConfigController.webp)
This class diagram shows an overview of the ConfigController class.

### GameResultController
![class diagram GameResultController](assets/chickenshockGameResultController.webp)
This class diagram shows an overview of the GameResultController class.
The data structure of `GameResult` and its contents are shown at the left and bottom of the diagram.

## Known Design Flaws

There are no known design flaws.

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for Chickenshock-backend.

## Tests

We use the following test strategies in the Chickenshock-backend:

- unit tests
