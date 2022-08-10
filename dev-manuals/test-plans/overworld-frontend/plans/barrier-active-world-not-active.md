# Barrier: Block inactive worlds (`u.barrier-3`)

Number: U.barrier.3  
Version: V0.2, 2022-08-10, add one step to procedure  
Author: Florian Wüst, Michael Linder  
Tester: -  

## Description

This use case verifies that a barrier is placed if the target area has been disabled by the lecturer.  

## Precondition

The barrier is configured in the overworld and in the backend. The target area is set as `inactive`.  
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
