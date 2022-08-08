# Name: Dungeon entrance and exit

Number: U.dungeon.1
Version: V0.2, 2022-08-08, remove "wrong" alternative procedures
Author: Florian Wüst
Tester: -

## Description

This use case verifies that entering and exiting a dungeon from a world works as intended.  

## Precondition

The world and dungeon scene are listed in the build settings and a scene transition to the dungeon is placed at the dungeon entrance  
and a scene transition to the world is placed at the dungeon exit.

## Postcondition

The dungeon can be entered and exited.  

## Typical procedure

1. The tester starts the game, no backends required.  
2. The tester walks at the dungeon entrance point.  
3. The dungeon is loaded and the world is unloaded.  
4. The tester walks at the dungeon exit point.  
5. The world is loaded and the dungeon is unloaded.  

## Alternative procedures



## Criticality

High

## Linkages
