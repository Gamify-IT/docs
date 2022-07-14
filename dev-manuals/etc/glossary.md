# Gamify-IT Glossary

Explanations for words that might need an explanation. Click on a letter to jump to the section.

Imagine the phrase: `A xy is ...` when writing an explanation.

```
❌ Overworld: An overworld is a world that ...
✅ Overworld: a world that ...
```

[A](#a) [B](#b) [C](#c) [D](#d) [E](#e) [F](#f) [G](#g) [H](#h) [I](#i) [J](#j) [K](#k) [L](#l) [M](#m) [N](#n) [O](#o) [P](#p) [Q](#q) [R](#r) [S](#s) [T](#t) [U](#u) [V](#v) [W](#w) [X](#x) [Y](#y) [Z](#z)

(#a)=

## A

(#area)=

### Area

- a part of the gamefield where the player can move, abstract class for [World](#world) and [Dungeon](#dungeon)

(#asset)=

### Asset

- bundle of graphics, [sprites](#sprite), [tiles](#tile) audio, [unity](#unity) script, etc.

### Asset pack

- a downloadable file containing [assets](#asset) e.g. in the [Unity](#unity) [asset store](https://assetstore.unity.com/)

(#b)=

## B

(#c)=

## C

(#d)=

## D

(#dungeon)=

### Dungeon

- a cave/building or similar which can be accessed through a [level](#level)
- can vary in size and content/look
- See the concept [here](/protocols/global/2022-06-03-protocol-1.md)
  - squares are the entrances to a dungeon

(#e)=

## E

(#f)=

## F

(#g)=

## G

(#h)=

## H

### HUD

- The HUD (head-up display) is frequently used to simultaneously display several pieces of information including the main character's health, items, and an indication of game progression

(#i)=

## I

### Issue

- Representation of a Task on GitHub

(#j)=

## J

(#k)=

## K

(#l)=

## L

(#level)=

### Level

- subdivision of a [World](#world)
- can have a few entrances to [dungeons](#dungeon)
- levels can be interconnected
- See the concept [here](/protocols/global/2022-06-03-protocol-1.md)
  - 2, 3, 4, ... on the left side of the picture are levels

(#m)=

## M

(#minigame)=

### Minigame

- a injectable game that runs as an independent service and can get invoked by the [overworld](#overworld).

(#n)=

## N

(#npc)=

### NPC

- a non player character which can be interacted with. These characters can appear in the overworld, in dungeons or in games.

(#o)=

## O

(#overworld)=

### Overworld

- the first world the player will see after starting the game. Here he can explore the world and start [minigames](#minigame).

(#p)=

## P

(#q)=

## Q

(#QoL)=

### Quality of Life (QoL) features

- are features that are `nice to have` and make things easier/smoother
- dont change the gameplay itself
- not explicitly necessary, but can improve the player experience

(#r)=

## R

(#s)=

## S

(#sprite)=

### Sprite

- pice of graphic (not necessarily only one `.png` file).

(#t)=

## T

### Task

- Represented as an issue on GitHub

(#tile)=

### Tile

- a graphic square that can tile a plane to form worlds.

### Tile map

- a file containing multiple [tiles](#tile).
- a unity component that displays a plane and you can draw [tiles](#tile) on it.

### Tile palette

- unity palette where you can create configure [tiles](#tile).

(#u)=

## U

(#unity)=

### Unity

- game engine we use

(#v)=

## V

(#w)=

## W

(#world)=

### World

- a region limited in size where the player can move and interact with the environment, i.e. with [NPCs](#npc)
- a world can contain multiple [Levels](#level)
- See the concept [here](/protocols/global/2022-06-03-protocol-1.md)
  - big circle is world

(#x)=

## X

(#y)=

## Y

(#z)=

## Z
