# Overworld

The overworld is the core of the Gamify-IT platform.
It is the main interface for students to interact with the platform.

## Overview

The overworld consists of multiple `worlds` and `dungeons`.
Throughout these areas, students can discover course contents like playable [minigames](../README.md) and dialogues with `NPCs`. The player (the character in the middle of the picture) can walk around and interact with various objects such as the NPC on the left or `books` providing useful information. The `HUD` helps navigating with the minimap and keeping track of the progress with the progress bar.  
![overworld](../../images/overworld.webp)

## Gameplay

### NPCs

The player can talk to other characters in the world to obtain information. The lecturer creating the course can specify what each `NPC` has to say and therefor give tips and summaries of important topics to the player.
![npc dialogue](../../images/npc-dialogue.webp)

### Books

For large amounts of information, there are also `books` to find. Those are very similar to NPC, they can also be configured by the lecturer and are meant to provide assistance. But unlike NPCs, they don't show multiple sentences but one big page. With that it is possible for the course creator to choose between different ways to display information and help the player.  
![books](../../images/books.webp)

### Minigames

The main purpose of the overworld is to allow the player to test and increase his knowledge and understanding by playing `minigames`. Minigames can be started at `minigame spots`, displayed as the red circle in the picture. The lecturer can set up the questions and possible answers in the [lecturer interface](../lecturer-interface/README.md). Once the player enteres the area of the minigame spot an information panel is opened. It displays the type of the game as well as the best result achieved by the player. The color of the minigame spot shows how good the player performed at the specific minigame. If the spot is `red` as shown in the picture, the player has not yet gotten enough points to `complete` the minigame. Once he finished a playthrough with the specified amount of points, the minigame spot turns `blue` which shows that he has finished it. The minigame can still be played and better results can be achieved, but the player doesn't have to in order to progress to the next area.  
![minigame](../../images/minigame-spot.webp)

## Progress

There are multiple `worlds` with optional `dungeons` each. The lecturer can configure each of them in the lecturer interface. Once some playable content is added, the world or dungeon becomes playable, but is locked at first. If a player has achieved enough points in all minigames of an area, he completed it. He can then progress to the next one, which is either the next dungeon of the world or the next world, if no further dungeon exists or is not configured by the lecturer. To help the player navigate and keep track of his progress, the `HUD` comes into play. The minimap in the top right corner helps to get around and highlights the positions of important objects like NPCs (displayed with the character head symbol) or dungeon entrance points (displayed with a cave symbol). The progress bar shows the `furthest area` the player can play, displayed as the yellow number, and the `ratio of completed minigames` as the blue bar. With each completed minigames, the bar fills up until all are done and the next area is unlocked.

## Controls

The player has a lot of options to interact with the game. He obviously move around, but also adjust his movement speed, interact with objects and characters, open menus and zoom the game and minimap in and out. The respective keys for each of those actions are listed here and can also be found in game a the pause menu opened with the `ESC` button at the `keybindings` tab.  
![keybindings](../../images/keybindings.webp)

## Developer

If you are a developer wanting to change or add something in the overworld, please refer to the [developer README](../../dev-manuals/services/overworld/README.md)
