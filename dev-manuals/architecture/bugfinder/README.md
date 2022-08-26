# Architecture of `Bugfinder`

## Purpose

The frontend should be an easy to use web application for finding bugs in code snippets and correcting them. At the moment are just example codes provieded in a config file, for the future (currently in progress) a backend provides these code snippets which will be loaded from the backend.

## General code structure

```md
This backend has the following package structure
- `assets`: Contains assets like pictures
- `dummy`: Dummy data like code snippets and their solution
- `models`: Contains the models
- `service`: Contains the game logic
- `store`: Contains the vue store (not used)
- `views`: Contains the views
```

## Starting the service

See the [README](https://github.com/Gamify-IT/bugfinder/blob/main/README.md)

## What to look at

- everything

## What to ignore

- nothing

## Known Design Flaws

- no knowing issues

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for `bugfinder`.
At the moment no knowing issues.

## Tests

In general, the following things are tested for `Bugfinder`:
- `components/CodeBox.vue` complete as unit tests
- `service/code-visualizer.ts` complete as unit tests
- `service/code-feedback.ts` complete as unit tests

- everything else manually with a testplan
