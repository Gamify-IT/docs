# Gamify-IT Glossary

Explanations for words that might need an explanation. Click on a letter to jump to the section.

Imagine the phrase: `A xy is ...` when writing an explanation.

```
❌ Overworld: An overworld is a world that ...
✅ Overworld: a world that ...
```

[A](#a) [B](#b) [C](#c) [D](#d) [E](#e) [F](#f) [G](#g) [H](#h) [I](#i) [J](#j) [K](#k) [L](#l) [M](#m) [N](#n) [O](#o) [P](#p) [Q](#q) [R](#r) [S](#s) [T](#t) [U](#u) [V](#v) [W](#w) [X](#x) [Y](#y) [Z](#z)

## A

### Area

- a part of the gamefield where the player can move, abstract class for [World](#world) and [Dungeon](#dungeon)

### Asset

- bundle of graphics, [sprites](#sprite), [tiles](#tile) audio, [unity](#unity) script, etc.

### Asset pack

- a downloadable file containing [assets](#asset) e.g. in the [Unity](#unity) [asset store](https://assetstore.unity.com/)

## B

## C


## D

### Dungeon

- a cave/building or similar which can be accessed through a [level](#level)
- can vary in size and content/look
- See the concept [here](/archive/protocols/global/2022-06-03-protocol-1.md)
  - squares are the entrances to a dungeon

## E

## F

## G

## H

### HUD

- The HUD (head-up display) is frequently used to simultaneously display several pieces of information including the main character's health, items, and an indication of game progression

## I

### Issue

- Representation of a Task on GitHub

## J

## K

## L

### Level

- subdivision of a [World](#world)
- can have a few entrances to [dungeons](#dungeon)
- levels can be interconnected
- See the concept [here](/archive/protocols/global/2022-06-03-protocol-1.md)
  - 2, 3, 4, ... on the left side of the picture are levels

## M

### Minigame

- a injectable game that runs as an independent service and can get invoked by the [overworld](#overworld).

### Multiplayer

- a game mode allowing multiple players to interact and play together simultaneously in real time. For the overworld multiplayer, click [here](../architecture/multiplayer/README.md).

## N

### NPC

- a non player character which can be interacted with. These characters can appear in the overworld, in dungeons or in games.

## O

### Overworld

- the first world the player will see after starting the game. Here he can explore the world and start [minigames](#minigame).

## P

## Q

### Quality of Life (QoL)

- describes how easy a user can use a service
- does not regard whether the actual functionality exists 

## R

## S

### Sprite

- pice of graphic (not necessarily only one `.png` file).

## T

### Task

- Represented as an issue on GitHub

### Tile

- a graphic square that can tile a plane to form worlds.

### Tile map

- a file containing multiple [tiles](#tile).
- a unity component that displays a plane and you can draw [tiles](#tile) on it.

### Tile palette

- unity palette where you can create configure [tiles](#tile).

## U

### Unity

- game engine we use

## V

## W

### World

- a region limited in size where the player can move and interact with the environment, i.e. with [NPCs](#npc)
- a world can contain multiple [Levels](#level)
- See the concept [here](/archive/protocols/global/2022-06-03-protocol-1.md)
  - big circle is world

## X

## Y

## Z
