# Overworld

The overworld is the core of the Gamify-IT platform.
It is the main interface for students to interact with the platform.

## Overview

The overworld consists of multiple `worlds` and `dungeons`.
Throughout these areas, students can discover course contents like playable [minigames](../README.md) and dialogues with `NPCs`.  
The player (the character in the middle of the picture) can walk around and interact with various objects such as the NPC on the left or with books to learn something.  
The `HUD` helps navigating with the minimap and keeping track of the progress with the progress bar.  
![overworld](../../images/overworld.webp)

## Gameplay

### NPCs

The player can talk to other characters in the world to obtain information.  
The lecturer can specify what each `NPC` has to say.  
This can be used to give tips or to summarize important topics for the player.
![npc dialogue](../../images/npc-dialogue.webp)

### Books

For large amounts of information, you can use books.  
They are similar to NPCs:
They can also be configured by the lecturer and are meant to provide assistance.  
Unlike NPCs, however, they show all content combined on one big page instead of splitting it up into sentences.  
Hence, there are different ways to display information and help the player.  
![books](../../images/books.webp)

### Minigames

The main purpose of the overworld is to allow the player to test and increase his knowledge and understanding by playing `minigames`. Minigames can be started at `minigame spots`, displayed as the red circle in the picture. The lecturer can set up the questions and possible answers in the [lecturer interface](../lecturer-interface/README.md). Once the player enters the area of the minigame spot an information panel is opened. It displays the type of the game as well as the best result achieved by the player. The color of the minigame spot shows how good the player performed at the specific minigame. If the spot is `red` as shown in the picture, the player has not yet gotten enough points to `complete` the minigame. Once he finished a playthrough with the specified amount of points, the minigame spot turns `blue` which shows that he has finished it. The minigame can still be played and better results can be achieved, but the player doesn't have to in order to progress to the next area.  
![minigame](../../images/minigame-spot.webp)

### Teleporters
As player paths through the world can get long and repetitive, we added `teleporters` to make life easier. Teleporters are spread over worlds and their dungeons. In the beginning of the game, all teleporters are locked. To `unlock` one, the player needs to walk towards it. Unlocked teleporters are indicated by a `green` shining T as shown in the picture, locked teleporters are indicated by a `brown` T. When a teleporter is unlocked it becomes a destination for all other teleporters that are unlocked. By interacting with it, the player can choose between available target destinations which are sorted by worlds.
![teleporter-unlocked](https://user-images.githubusercontent.com/98211563/210592123-c1f4dc35-8732-4674-8d7b-6542a5619ab4.png)


## Progress

There are multiple `worlds` with optional `dungeons` each. The lecturer can configure each of them in the lecturer interface. Once some playable content is added, the world or dungeon becomes playable, but is locked at first. If a player has achieved enough points in all minigames of an area, he completed it. He can then progress to the next one, which is either the next dungeon of the world or the next world, if no further dungeon exists or is not configured by the lecturer. To help the player navigate and keep track of his progress, the `HUD` comes into play. The minimap in the top right corner helps to get around and highlights the positions of important objects like NPCs (displayed with the character head symbol) or dungeon entrance points (displayed with a cave symbol). The progress bar shows the `furthest area` the player can play, displayed as the yellow number, and the `ratio of completed minigames` as the blue bar. With each completed minigames, the bar fills up until all are done and the next area is unlocked.

## Controls

The player has a lot of options to interact with the game:  
They can move around, they can adjust their (movement) speed, can interact with objects and characters, can open menus, and can zoom the game or minimap.  
The respective keys for each of those actions are listed below and can also be found in-game in the pause menu (press the <kbd>ESC</kbd> button and navigate to the `keybindings` tab).  
![keybindings](../../images/keybindings.webp)

## Sounds

Different sounds play throughout the game for complete immersion.

#### Background music

Each world has its own background music, dungeons have their own distinct music as well. During transitions between worlds or when entering a dungeon, the music changes smoothly.

#### Open sound of minigame spot

Once the player enters the area of the minigame spot, the corresponding sound will be played, indicating that the minigame is open.

#### Sound for completed achievement

When the player completes an achievement, a panel will appear at the bottom of the screen with a message about the achievement. A notification sound will play at this time to draw the player's attention to the panel that has just appeared.

#### Click sound

The game has many interactive buttons. When the player presses one of the buttons, the corresponding click sound is played, e.g. when the map is zoomed in/out, when the pause menu is opened, when a category in menu is selected, etc.

#### Sound for interaction with NPC

A sound symbolising that the NPC has said hello will be played when the player interacts with an NPC.

#### Sound for interaction with book

When the player interacts with the book, a magical opening sound plays.

#### Sound for movement

As the player moves in the game, the sound of rustling grass is played to represent footsteps. When the player accelerates, the sound of movement also changes its speed.

#### Sound for teleporter opening

If the player is on a teleporter, the teleporter will be unlocked. This event is also accompanied by a characteristic sound to attract more attention.

#### Sounds for UFO

Once the player has selected the final teleportation location, a UFO will follow him, accompanied by an alien sound. Upon reaching the end point of the teleportation, the player will also be brought back by the UFO. At this point, the sound of the aliens will play, but this time in reverse.

## Volume control

The player has the ability to control the volume of sounds in the game . The control button is located in the pause menu in the upper right corner. When the player press the button, the volume of the sounds goes to the next level, which is accompanied by a change of image of the button. There are 4 volume levels in total in the game: muted, low volume, medium volume and high volume.
The volume of sounds the player chooses will also apply to all the minigames the player play going forward.
![volume-control](../../images/volume_button.webp)

## Developer

If you are a developer wanting to change or add something in the overworld, please refer to the [developer README](../../dev-manuals/services/overworld/README.md)
