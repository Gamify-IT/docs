# Overworld: Barrier not present on playable worlds (`u.overworld-5`)
 
Version: V1.3, 2022-08-11, adapt to new template \
Author: Florian Wüst, Michael Linder  

## Description

This use case verifies that no barrier is placed if the target area can be played by the player.  

## Precondition

The barrier is configured in the overworld and in the backend. The player has unlocked the target area.  
The game is started and the backend runs.

## Postcondition

The barrier is visible and cannot be passed.

## Typical procedure

1. The tester walks to the barrier spot
2. The barrier is not displayed
3. The tester can walk through the spot where the barrier otherwise is

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A