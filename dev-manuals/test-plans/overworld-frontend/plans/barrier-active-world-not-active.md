# Name: Barrier active, world not active

Number: U.barrier.3  
Version: V0.1, 2022-08-09, create test case 
Author: Florian Wüst  
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

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A
