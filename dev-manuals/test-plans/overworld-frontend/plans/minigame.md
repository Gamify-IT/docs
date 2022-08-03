# Name: Minigame

Number: U.minigame.1  
Version: V0.1, 2022-08-03, create test case  
Author: Florian Wüst  
Tester: -  

## Description

This use case verifies that everything regarding minigames in the overworld works as intended.  
This includes loading the minigame and player data from the backend as well as setting up the minigame object  
with the minigame name and configuration and the correct player specific highscore and status. 

## Precondition

The minigame object is configurated in the overworld (world and index are set) and the needed data exists in the backend.

## Postcondition

The minigame object is set up according to the data in the data base. 

## Typical procedure

1. The tester starts the game with a running backend.  
2. The tester walks to the minigame spot.  
3. The minigame spot is displayed accordingly to the data in the backend.
4. The minigame spot has the correct color (blue = completed, red = not completed) accordingly to the player specific highscore.  
5. The tester walks into the minigame spot.  
6. The minigame overview panel opens.
7. The displayed minigame and player specific highscore are correct as set in the backend. 
8. The tester presses the 'start' button  
9. The correct minigame starts  
10. The correct configuration is loaded

## Alternative procedures

3.1 The minigame spot is not displayed, because it was not configurated in the backend.  
3.2 The minigame spot is not displayed, even tho it was configurated.  
4.1 The minigame spot has the wrong color.  
6.1 The minigame overview panel doesn't open.  
7.1 The minigame and / or the player specific highscore are not correct  
9.1 A wrong minigame starts  
9.2 Nothing starts at all  
10.1 Not the correct configuration is loaded.  

## Criticality

High

## Linkages

-
