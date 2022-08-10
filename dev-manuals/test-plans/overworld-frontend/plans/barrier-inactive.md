# Name: Barrier inactive

Number: U.barrier.1  
Version: V0.3, 2022-08-10, add one step to procedure  
Author: Florian Wüst, Michael Linder  
Tester: -  

## Description

This use case verifies that no barrier is placed if the destination world is set as active by the lecturer and the player has unlocked it.  

## Precondition

The barrier object is configured in the overworld (area origin and destination are set) and the needed data exists in the backend. This includes that the destination world is set as 'active' and the player has unlocked the world.  
The game is started and the backend runs.

## Postcondition

The barrier object is set up as inactive and therefore not visible.

## Typical procedure

1. The tester walks to the barrier spot.  
2. The barrier is not displayed.  
3. The tester can walk through the spot where the barrier otherwise is.

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A