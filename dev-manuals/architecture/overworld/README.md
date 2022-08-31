# Architecture of overworld

## Purpose

This service connects the minigames and provides the base game platform.

## General code structure

All selfwritten code files are stored in [Assets/Scripts](https://github.com/Gamify-IT/overworld/tree/main/Assets/Scripts) and are used by gameobjects in the scenes which are stored in [Assets/Scenes](https://github.com/Gamify-IT/overworld/tree/main/Assets/Scenes).

## Starting the service

See the [README](https://github.com/Gamify-IT/overworld#readme).

## What to look at

- [Assets/Scripts/Barriers/*](https://github.com/Gamify-IT/overworld/tree/main/Assets/Scripts/Barriers)
- [Assets/Scripts/GameManager/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/GameManager)
- [Assets/Scripts/HUD/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/HUD)
- [Assets/Scripts/Interactable/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/Interactable)
- [Assets/Scripts/MinigameLoading/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/MinigameLoading)
- [Assets/Scripts/Player/Animation.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/Player/Animation.cs)
- [Assets/Scripts/Scene Loading/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/Scene%20Loading)
- [Assets/Plugins/LoadMinigame.jslib](https://github.com/Gamify-IT/overworld/blob/main/Assets/Plugins/Load%20Minigame.jslib)

## What to ignore

- Assets/Scripts/MoveTilesEditor.cs (because it is UnityEditor only)

## Known Design Flaws

- UniTask return values are not working correctly

## Known Problems

- There is currently only one player in only one course
  -> you have to reset the DB every time before testing, e.g. when testing unlocking behavior
- The way player- and course- data is being communicated from the level selection screen to the overworld or from the overworld to the minigames is currently highly unstable or non-existing. See also the single-player and -course restriction above.
  
## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/> by searching for overworld.

## Tests

Everything is manually tested with [these testplans](https://github.com/Gamify-IT/docs/tree/main/dev-manuals/test-plans/overworld).
