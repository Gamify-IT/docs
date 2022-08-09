# Name: Minigame spot configured and not done

Number: U.minigame.4  
Version: V0.1, 2022-08-09, create test case
Author: Florian Wüst  
Tester: -  

## Description

This use case verifies that loading the minigame and player data for a configurated minigame from the backend works as intended. Futhermore, player specific data like the highscore and the status of the minigame needs to be loaded. All that info has to be stored in the minigame object.

## Precondition

The minigame object is configured in the overworld (world and index are set) and the needed data exists in the backend.  
The game is started and the backend runs.

## Postcondition

The minigame object is set up according to the data in the data base.

## Typical procedure

1. The tester walks to the minigame spot.  
2. The minigame spot is displayed and has a red color. 
3. The tester walks into the minigame spot.  
4. The minigame overview panel opens.
5. The displayed minigame and player specific highscore are correct as set in the backend.

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A