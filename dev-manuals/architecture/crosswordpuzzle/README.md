# Architecture of Crosswordpuzzle

## Purpose

The user can play a crosswordpuzzle out of given questions.

## Table of Contents
<!-- TOC -->
* [Links](#links)
* [General code structure](#general-code-structure)
* [Starting the service](#starting-the-service)
* [What to look at](#what-to-look-at)
* [What to ignore](#what-to-ignore)
* [Known Design Flaws](#known-design-flaws)
* [Known Bugs](#known-bugs)
* [Tests](#tests)
<!-- TOC -->

## Links

- The [user docs](../../../user-manuals/minigames/crosswordpuzzle.md) explain how to play the game.
- The program code is available [here](https://github.com/Gamify-IT/crosswordpuzzle).
- The overview of the architecture can be found [here](../general-architecture.md).
- The backend architecture is described [here](../crosswordpuzzle-backend/README.md).

## General code structure

- `assets`: Static assets like the logo
- `components`: Re-usable Vue components
- `router`: Frontend site page routing
- `ts`: Data models and backend communication
- `types`: Types of the crosswordpuzzle
- `store`: Store to get data between views
- `views`: The displayed pages. Currently consists of only the GameView that contains the whole game

## Starting the service

See the [README](https://github.com/Gamify-IT/crosswordpuzzle#readme).

## What to look at

_Everything_

## What to ignore

_NA_

## Known Design Flaws

Nothing

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for Crosswordpuzzle.

## Tests

In general, the following things are tested for Crosswordpuzzle:
- everything manually with a testplan
- Unit tests for Sonarqube funtionality
