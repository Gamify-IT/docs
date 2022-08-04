# Name: Barrier

Number: U.barrier.1  
Version: V0.1, 2022-08-03, create test case  
Author: Florian Wüst  
Tester: -  

## Description

This use case verifies that everything regarding barriers in the overworld works as intended.  
This includes loading the needed area data from the backend as well as setting up the barrier object  
accordingly depending on whether the area is set as active in the backend and the player has also unlocked the area.

## Precondition

The barrier object is configurated in the overworld (area origin and destination are set) and the needed data exists in the backend.

## Postcondition

The barrier object is set up according to the data in the data base.

## Typical procedure

1. The tester starts the game with a running backend.  
2. The tester walks to the barrier spot.  
3. The barrier is displayed.  

## Alternative procedures

3.1 The barrier is not displayed, because it shouldn't be due to the data in the backend.
3.2 The barrier is not displayed, even though it should be.

## Criticality

High

## Linkages

-
