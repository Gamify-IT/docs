# Overworld: Minigame spot (`u.overworld-11`)
 
Version: V1.2, 2022-08-11, adapt to new template \
Author: Florian Wüst   

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
3. The minigame spot is colored red
4. Walk **in**to the minigame spot
4. The minigame overview panel opens
5. The displayed minigame and player specific highscore are the ones stored in the backend

## Alternative procedures

3.1 The player already achieved a highscore above 50 for that minigame: the minigame spot is colored blue

## Criticality

High

## Linkages

N/A
