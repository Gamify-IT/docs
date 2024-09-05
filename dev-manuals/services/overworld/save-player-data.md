# Save Player Data

## Overview

To ensure that player data and progress are preserved after each session and can be restored upon logging back in, various information and data are stored in the Overworld Backend.

## Which data is currently saved

- Position of the player 
- Selected character
- Achievement progress
- Volume level settings
- Date Time 

## How data saving is realized 

### Achievement Progress
The achievement progress is saved separately from other player data in the `AchievementData` and `AchievementStatistic` class in the frontend and the `AchievementStatistic` class in the backend.
Please take a look [here](../../achievements/data-model.md) for a detailed description.

The following aspects are considered:

#### Achievement Progress

The contribution to each achievement is saved as a number and can be updated with the `IncreaseAchievementProgress` method. \
Not that you need to ensure that the progress stops increasing once the achievement is completed.

#### Whether the achievement has already been completed

Every time the `IncreaseAchievementProgress` method is called, it is checked wether the achievement is completed.

#### Interacted objects list
This list saves which objects (books, teleporters, NPCs, ...) the player has already interacted with. The list contains triples consisting of the world index, the dungeon index an object is located in, as well as the its ID. \
Note that for new objects you need to add this list to the new class.

### Other Player Data

All other player data is saved in the `PlayerStatistic` classes. Please take a look [here](../../architecture/overworld-backend/README.md) for the data model.

#### Player osition 

The player's position is saved as the x and y coordinates alongside the current world, dungeon index and the scene name.

#### Character

The selected character by the player is saved as the index in the character list.

#### Volume Level

There exist four different volume levels including one for mute.
These levels are managed in the `VolumeControllerButton` class in the Overworld Frontend. Moreover, these levels are also applied in other minigames. \
Note that the volume level is mapped to a keybinding in order to be saved effective. These mapping are defined in `ConvertKeyCodeToInt` and 
`ConvertIntToKeyCode` methods of the `Data Manager`class.

#### Date Time

Some achievements required a date or time to be saved. Since there are different types used in Java and C#, date times are converted to strings and back to transfer them easier.

## Where Data is saved when quitting

In general, data needs to be saved when the player returns to the lecturer interface or starts a minigame.

There are two different ways of saving data.

### In the Game Manager class

Achievements and the player statistic are saved via the `SavePlayerData` method in the backend. During the session, changes of the values are stored as follows in the `Data Manger` class:
- Logout position coordinates are determined via the transform object of the player 
- World index, dungeon index and scene name are saved in the Data Manager every time the player enters a new area. Below can be found an overview in which cases these information must be saved and where it is done.
  
    | Event             | Code Location     |
    | -------------     | -------------     |
    | Entering new world   | `LoadMaps` class   |
    | Entering/leaving dungeon | `LoadSubScene` class     |
    |            | 

- Character index is saved after the player selects a new one in the `SetupCharacter` method of the `Data Manager` class.

### In the Class where changes happened

The volume level is saved immediately in the `VolumeControllerButton` class since it is synchronized with the minigames.

## Where Data is retrieved when starting

The player data is retrieved from the backend in the `LoadScene` method of the `LoadingManager` class. After that, all values are initialized with the retrieved values in the corresponding `Process` methods of the `Data Manager` class.



