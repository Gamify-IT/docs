# Barrier: Block locked worlds (`u.barrier-2`)

Number: U.barrier.2  
Version: V0.4, 2022-08-10, add one step to procedure  
Author: Florian Wüst, Michael Linder
Tester: -  

## Description

This use case verifies that a barrier blocks a target area if it exists but the player has not yet unlocked it.  

## Precondition

The barrier is configured in the overworld and in the backend. The player has not yet unlocked the target area.  
The game is started and the backend runs.

## Postcondition

The barrier is visible and cannot be passed.

## Typical procedure

1. The tester walks to the barrier spot
2. The barrier is displayed
3. The tester can not walk through or around the barrier

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A
