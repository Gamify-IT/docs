# Architecture of Finitequiz

Project: <https://github.com/Gamify-IT/finitequiz> \
Scripts: <https://github.com/Gamify-IT/finitequiz/tree/main/src>

## Purpose

Being a single choice question style minigame that lets users choose one correct answer from a bunch of wrong answers

## General code structure

- `__mocks__`: Mocking behavior for testing
- `assets`: Static assets like the logo
- `components`: Re-usable Vue components
- `router`: Frontend site page routing
- `ts`: Data models and backend communication
- `views`: The displayed pages. Currently consists of only the GameView that contains the whole game

## Starting the service

See the [README](https://github.com/Gamify-IT/finitequiz#readme).

## What to look at

_Everything_

## What to ignore

_NA_

## Known Design Flaws

- Exactly one answer must be correct, not more or less

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for Finitequiz.

## Tests

In general, the following things are tested for Finitequiz:
- everything manually with a testplan
- Unit tests for Sonarqube funtionality
