# Architecture of Bugfinder-backend

Bugfinder is a minigame which is part of the Gamify-IT platform.

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

- The [user docs](../../../user-manuals/minigames/bugfinder.md) explain how to play the game.
- The program code is available [here](https://github.com/Gamify-IT/bugfinder-backend).
- The overview of the architecture can be found [here](../general-architecture.md).
- The frontend architecture is described [here](../bugfinder/README.md).

## General code structure

This [Java backend](https://github.com/Gamify-IT/bugfinder-backend) has the following package structure
- `code`: Contains all files for code, like controller, repositories, service classes, entity classes, DTOs
- `configuration`: Contains all files for configuration, repositories, like controller, service classes, entity classes, DTOs
- `gameresult`: Contains all files for gameresult, repositories, like controller, service classes, entity classes, DTOs
- `solution`: Contains all files for solution, repositories, like controller, service classes, entity classes, DTOs


## Starting the service

See the [README](https://github.com/Gamify-IT/bugfinder-backend#readme).

## What to look at

The controllers for the API requests are a good point to start.  
From there you can follow the code flow to the other components.

## What to ignore

Nothing at the moment.

## Class diagrams

**TODO**

## Known Design Flaws

There are no known design flaws.

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for Bugfinder-backend.

## Tests

We use the following test strategies in the Bugfinder-backend:

- unit tests
