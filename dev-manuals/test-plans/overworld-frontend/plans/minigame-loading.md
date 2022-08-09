# Name: Minigame loading

Number: U.minigame.2  
Version: V0.3, 2022-08-09, adapt typical procedure  
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
 
1. The tester walks to the minigame spot.  
2. The tester walks into the minigame spot.  
3. The minigame overview panel opens.
4. The tester presses the 'start' button  
5. The correct minigame starts  
6. The correct configuration is passed

## Alternative procedures

N/A

## Criticality

High

## Linkages

U.minigame.1 (minigame spots)
