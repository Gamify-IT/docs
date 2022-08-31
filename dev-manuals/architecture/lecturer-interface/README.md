# Architecture of lecturer-interface

Code: <https://github.com/Gamify-IT/lecturer-interface/tree/main/src>

## Purpose

Configuring the overworld and the minigames.

## General code structure

This repository has the following package structure:

- `assets`: Contains assets like pictures
- `components`: Contains re-usable Vue components
- `models`: Contains the data models
- `service`: Contains the game logic
- `store`: Interacts with the vue state store vuex (currently unused)
- `views`: Contains the complete views displayed by this single-page application

## Starting the service

See the [README](https://github.com/Gamify-IT/lecturer-interface#readme).

## What to look at

_Everything_

## What to ignore

_NA_

## Known Design Flaws

- no known design flaws at the moment

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for lecturer-interface.

## Tests

In general, the following things are tested for `lecturer-interface`:
- General rendering as unit tests
- everything else manually with a testplan
