# Name: Dungeon entrance and exit

Number: U.dungeon.1
Version: V0.3, 2022-08-09, remove post condition and adapt typical procedure
Author: Florian Wüst
Tester: -

## Description

This use case verifies that entering and exiting a dungeon from a world works as intended.  

## Precondition

The world and dungeon scene are listed in the build settings and a scene transition to the dungeon is placed at the dungeon entrance  
and a scene transition to the world is placed at the dungeon exit.

## Postcondition

N/A

## Typical procedure

1. The tester walks at the dungeon entrance point.  
2. The dungeon is loaded and the world is unloaded.  
3. The tester walks at the dungeon exit point.  
4. The world is loaded and the dungeon is unloaded.  

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A