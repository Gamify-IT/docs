# Add and set up areas

## Overview

To add new areas, you first need to [create it](create-new-world.md) and set up all needed objects of the area. In case of a world, you need to put it at the right place and set up the [world loading](world-loaders.md).

## How to add an area

To add a dungeon, you simply have to add it to a world using a [scene transition](scene-transition.md).  
To add a world, you need to set the position of the `Grid` game object so that it connects with the nearby worlds.  
-> picture inspector view  
To make this easier, you can load multiple worlds at once. To do that, open the new world and drag and drop a nearby scene in the `Hierarchy`.  
-> picture multiple scenes

## How to set up an area

To set up an area, you need to set up the following parts:  

1. Minigames, as specified [here](set-up-minigames.md)
2. NPCs, as specified [here](set-up-npcs.md)
3. Barriers, as specified [here](set-up-barriers.md)
4. Dungeon entrance or exit points, as specified [here](scene-transition.md)
5. Minimap, as specified [here](set-up-minimap.md)
