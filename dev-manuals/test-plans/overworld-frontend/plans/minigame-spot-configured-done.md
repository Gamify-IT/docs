# Minigames: Pre-game start (`u.minigames-1`)

Number: U.minigame.1  
Version: V0.2, 2022-08-09, split test case
Author: Florian Wüst  
Tester: -  

## Description

This test walks the user through the procedure necessary to start a minigame. Specifically, it tests that minigame spots are colored correctly and that a popup is shown before the minigame can be started.

## Precondition

The minigame (spot) is configured in the overworld and its backend.  
The game is started and the backend runs.
Optionally, the backend already has statistics for this minigame and player.

## Postcondition

Nothing changed for the backend.

## Typical procedure

1. Walk to the minigame spot
2. The minigame spot is displayed
3. The minigame spot is colored blue
4. Walk **in**to the minigame spot
4. The minigame overview panel opens
5. The displayed minigame and player specific highscore are the ones stored in the backend

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A
