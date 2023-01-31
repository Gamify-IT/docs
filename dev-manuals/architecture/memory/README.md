# Architecture of Memory

## Purpose

```md
Being a conventional memory game where players have to memorize cards in order to find matching pairs.
```

## General code structure

```md
The frontend has the following package structure
- `assets`: images / global style used in the project
- `components`: .vue components
- `router`: manages routing between singleplayer and multiplayer
- `types`: typescript files containing the data structures and controllers
```

## Starting the service

See the README or the user manual. (to be improved)

## What to look at

For data structures see: [DataModels](https://github.com/Gamify-IT/memory/blob/main/src/types/data-models.ts) or [DTOs](https://github.com/Gamify-IT/memory/blob/main/src/types/dtos.ts)

The following class diagram will help understand the architecture:
![overview class diagram of complete application](assets/memory-class-diagram.svg)


## What to ignore

N/A

## Known Design Flaws

N/A

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for memory.

## Tests

We use unit tests for testing.
