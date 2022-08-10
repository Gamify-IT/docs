# Name: Barrier active, world not active

Number: U.barrier.3  
Version: V0.2, 2022-08-10, add one step to procedure  
Author: Florian Wüst, Michael Linder  
Tester: -  

## Description

This use case verifies that a barrier is placed if the destination world is not set as active by the lecturer.  

## Precondition

The barrier object is configured in the overworld (area origin and destination are set) and the needed data exists in the backend. This includes that the destination world is set as 'inactive'.  
The game is started and the backend runs.

## Postcondition

The barrier object is set up as active and therefore is visible.

## Typical procedure

1. The tester walks to the barrier spot.  
2. The barrier is displayed.  
3. The tester can not walk through or around the barrier

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A
