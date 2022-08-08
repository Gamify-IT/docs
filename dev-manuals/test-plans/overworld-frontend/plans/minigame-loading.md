# Name: Minigame loading

Number: U.minigame.2  
Version: V0.2, 2022-08-04, remove "wrong" alternative procedures  
Author: Florian Wüst  
Tester: -  

## Description

This use case verifies that everything regarding minigames loading in the overworld works as intended.  
This includes loading the correct minigame with the right configuration.

## Precondition

Use case U.minigame.1 works correctly.  
The minigame object is configurated in the overworld (minigame and configuration are set).

## Postcondition

The correct minigame with the right configuration gets loaded.

## Typical procedure

1. The tester starts the game with a running backend.  
2. The tester walks to the minigame spot.  
3. The tester walks into the minigame spot.  
4. The minigame overview panel opens.
5. The tester presses the 'start' button  
6. The correct minigame starts  
7. The correct configuration is passed

## Alternative procedures

 

## Criticality

High

## Linkages

U.minigame.1 (minigame spots)
