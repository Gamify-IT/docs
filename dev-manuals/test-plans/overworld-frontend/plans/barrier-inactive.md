# Name: Barrier inactive

Number: U.barrier.1  
Version: V0.1, 2022-08-08, create test case  
Author: Florian Wüst  
Tester: -  

## Description

This use case verifies that everything regarding barriers in the overworld works as intended.  
This includes loading the needed area data from the backend as well as setting up the barrier object as inactive.

## Precondition

The barrier object is configurated in the overworld (area origin and destination are set) and the needed data exists in the backend.
The game is started and the backend runs.

## Postcondition

The barrier object is set up as inactive and therefor not visible.

## Typical procedure

1. The tester starts the game with a running backend.  
2. The tester walks to the barrier spot.  
3. The barrier is not displayed.  

## Alternative procedures



## Criticality

High

## Linkages

-
