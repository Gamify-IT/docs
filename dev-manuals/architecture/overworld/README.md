# Architecture of overworld

## Purpose

This service connects the minigames and provides the base game platform.

## General code structure

All selfwritten code files are stored in [Assets/Scripts](https://github.com/Gamify-IT/overworld/tree/main/Assets/Scripts) and are used by gameobjects in the scenes which are stored in [Assets/Scenes](https://github.com/Gamify-IT/overworld/tree/main/Assets/Scenes).

## Starting the service

See the README or the user manual.

## What to look at

- [Assets/Scripts/Barriers/*](https://github.com/Gamify-IT/overworld/tree/main/Assets/Scripts/Barriers) (TODO: adjust comments)
- [Assets/Scripts/GameManager/GameManagerV2.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/GameManager/GameManagerV2.cs) (TODO: adjust comments)
- [Assets/Scripts/GameManager/GameSettings.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/GameManager/GameSettings.cs) (TODO: adjust comments)
- [Assets/Scripts/GameManager/JsonHelper.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/GameManager/JsonHelper.cs) (TODO: adjust comments)
- [Assets/Scripts/GameManager/NPCTalkEvent.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/GameManager/NPCTalkEvent.cs) (TODO: adjust comments)
- [Assets/Scripts/GameManager/Data Classes/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/GameManager/Data%20Classes) (TODO: adjust comments)
- [Assets/Scripts/GameManager/DTOs/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/GameManager/DTOs) (TODO: adjust comments)
- [Assets/Scripts/HUD/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/HUD) (TODO: adjust comments)
- [Assets/Scripts/Interactable/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/Interactable) (TODO: adjust comments, restructure NPC.cs)
- [Assets/Scripts/MinigameLoading/Configuration.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/MinigameLoading/Configuration.cs) (TODO: adjust comments)
- [Assets/Scripts/MinigameLoading/Minigame.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/MinigameLoading/Minigame.cs) (TODO: adjust comments)
- [Assets/Scripts/MinigameLoading/MinigameData.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/MinigameLoading/MinigameData.cs) (TODO: adjust comments)
- [Assets/Scripts/MinigameLoading/MinigameStarting.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/MinigameLoading/MinigameStarting.cs) (TODO: adjust comments)
- [Assets/Scripts/Player/Animation.cs](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scripts/Player/Animation.cs) (TODO: adjust comments, rename)
- [Assets/Scripts/Scene Loading/*](https://github.com/Gamify-IT/overworld/blob/main/Assets/Scene%20Loading) (TODO: adjust comments, remove commented out code, rename loadmaps -> LoadMaps)
- [Assets/Plugins/LoadMinigame.jslib](https://github.com/Gamify-IT/overworld/blob/main/Assets/Plugins/LoadMinigame.jslib)

## What to ignore

- Assets/Scripts/GameManager/GameManager.cs (TODO: delete)
- Assets/Scripts/GameManager/EnterArea.cs (TODO: delete)
- Assets/Scripts/MinigameLoading/LoadMinigame.cs (TODO: delete)
- Assets/Scripts/Player/mymove.cs (TODO: delete)
- Assets/Scripts/MoveTilesEditor.cs

## Known Design Flaws

- Unity :,)
- UniTask return values are not working correctly

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/> by searching for overworld.

## Tests

Everything is manually tested with [these testplans](https://github.com/Gamify-IT/docs/tree/main/dev-manuals/test-plans/overworld).
