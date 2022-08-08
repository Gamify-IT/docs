# Name: Minigame spot configurated

Number: U.minigame.1  
Version: V0.2, 2022-08-08, split test case
Author: Florian Wüst  
Tester: -  

## Description

This use case verifies that loading the minigame and player data for a configurated minigame from the backend as well as setting up the minigame object  
with the minigame name and configuration and the correct player specific highscore and status works as intended.

## Precondition

The minigame object is configurated in the overworld (world and index are set) and the needed data exists in the backend.  
The game is started and the backend runs.

## Postcondition

The minigame object is set up according to the data in the data base.

## Typical procedure

1. The tester walks to the minigame spot.  
2. The minigame spot is displayed accordingly to the data in the backend.
3. The minigame spot has the correct color (blue = completed, red = not completed) accordingly to the player specific highscore.  
4. The tester walks into the minigame spot.  
5. The minigame overview panel opens.
6. The displayed minigame and player specific highscore are correct as set in the backend.

## Alternative procedures

   

## Criticality

High

## Linkages
