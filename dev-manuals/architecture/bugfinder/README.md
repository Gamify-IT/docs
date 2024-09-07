# Architecture of Bugfinder

## Purpose

Being a small and fun minigame to learn programming by finding bugs in code snippets and correcting them.

## General code structure

This repository has the following package structure:

- `assets`: Contains assets like pictures
- `components`: Contains re-usable Vue components
- `dummy`: Dummy data like code snippets and their solution
- `models`: Contains the data models
- `service`: Contains the game logic
- `store`: Interacts with the vue state store vuex (currently unused)
- `views`: Contains the complete views displayed by this single-page application

## Starting the service

See the [README](https://github.com/Gamify-IT/bugfinder#readme).

## What to look at

- everything

## What to ignore

- nothing

## Known Design Flaws

- no known issues

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for `bugfinder`.

## Tests

In general, the following things are tested for `Bugfinder`:
- `components/CodeBox.vue` complete as unit tests
- `service/code-visualizer.ts` complete as unit tests
- `service/code-feedback.ts` complete as unit tests

- everything else manually with a testplan
