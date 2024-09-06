# Architecture of Tower Defense

## Purpose

Tower Defense is a minigame that is part of the Gamify-IT platform.
The intention with this game is to make answering single choice questions fun.

## Table of Contents

<!-- TOC -->
- [Architecture of Tower Defense](#architecture-of-tower-defense)
  - [Purpose](#purpose)
  - [Table of Contents](#table-of-contents)
  - [Links](#links)
  - [Purpose](#purpose-1)
  - [General code structure](#general-code-structure)
  - [Starting the service](#starting-the-service)
  - [What to look at](#what-to-look-at)
  - [What to ignore](#what-to-ignore)
  - [Known Design Flaws](#known-design-flaws)
  - [Known Bugs](#known-bugs)
  - [Tests](#tests)
<!-- TOC -->

## Links

- The [user docs](../../../user-manuals/minigames/tower-defense.md) explain how to play the game.
- The program code is available [here](https://github.com/Gamify-IT/tower-defense).
- The overview of the architecture can be found [here](../general-architecture.md).
- The backend architecture is described [here](../tower-defense-backend/README.md).

## Purpose

Being a fun-to-play minigame that lets users choose one correct answer from a bunch of wrong answers

## General code structure

Unity uses C# scripts. \
There is no "main"-class in Unity scripts. \
Each script that is put on a `GameObject` can have a `Start` method (called once when the `GameObject` is created), an `Awake` method (called once before `Start`), and an `Update` method (called on each frame). \
If the `GameObject` is destroyed everything attached to it will be destroyed as well, meaning no script attached to the destroyed `GameObject` will be executed again.

*WIP*

## Starting the service

See the [README](https://github.com/Gamify-IT/tower-defense#readme).

## What to look at

Generally all `.cs` files. 
The key script files that contain most of the actual game behavior are 

## What to ignore

*WIP*

## Known Design Flaws

N/A

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for Tower Defense.

## Tests

In general, the following things are tested for Tower Defense:
- everything manually with a testplan
