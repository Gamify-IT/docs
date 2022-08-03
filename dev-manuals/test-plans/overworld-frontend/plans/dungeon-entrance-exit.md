# Name: Dungeon entrance and exit

Number: U.dungeon.1
Version: V0.1, 2022-08-03, create test plan
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

3.1 The dungeon is not loaded and / or the world is not unloaded.  
5.1 The world is not loaded and / or the dungeon is not unloaded.  

## Criticality

High

## Linkages
