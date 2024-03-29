# Architecture of Chickenshock

## Purpose

Chickenshock is a minigame that is part of the Gamify-IT platform.
The intention with this game is to make answering single choice questions fun.

## Table of Contents

<!-- TOC -->
* [Links](#links)
* [Purpose](#purpose)
* [General code structure](#general-code-structure)
* [Starting the service](#starting-the-service)
* [What to look at](#what-to-look-at)
* [What to ignore](#what-to-ignore)
* [Known Design Flaws](#known-design-flaws)
* [Known Bugs](#known-bugs)
* [Tests](#tests)
<!-- TOC -->

## Links

- The [user docs](../../../user-manuals/minigames/chickenshock.md) explain how to play the game.
- The program code is available [here](https://github.com/Gamify-IT/chickenshock).
- The overview of the architecture can be found [here](../general-architecture.md).
- The backend architecture is described [here](../chickenshock-backend/README.md).

## Purpose

Being a fun-to-play minigame that lets users choose one correct answer from a bunch of wrong answers

## General code structure

Unity uses C# scripts. \
There is no "main"-class in Unity scripts. \
Each script that is put on a `GameObject` can have a `Start` method (called once when the `GameObject` is created), an `Awake` method (called once before `Start`), and an `Update` method (called on each frame). \
If the `GameObject` is destroyed everything attached to it will be destroyed as well, meaning no script attached to the destroyed `GameObject` will be executed again.

We decided to split our Chickenshock game into 3 main scenes:

- `Main Screen`: contains the content of the start screen
- `Game`: contains the content of the main game
- `End Screen`: contains the content of the end screen

## Starting the service

See the [README](https://github.com/Gamify-IT/chickenshock#readme).

## What to look at

Generally all `.cs` files. 
The key script files that contain most of the actual game behavior are the `Global.cs` file and the `ShootWeapon.cs` file. 

## What to ignore

We created a `ChickenshockProperties` file for less redundance. 
This is a static class because there is no option we know of that uses a normal `.properties` file in Unity.

## Known Design Flaws

N/A

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for Chickenshock.

## Tests

In general, the following things are tested for Chickenshock:
- everything manually with a testplan
