# Overworld: Loading screen (`u.overworld-20`)

Version: v1.0, 2022-08-27, create test plan \
Author: Florian Wüst, Gilian Rehm

## Description

This use case verifies that the loading screen works as intended.  

## Precondition

The tester is logged in, but not in the overworld yet.

## Postcondition

The tester is in the overworld.

## Typical procedure

1. The loading screen opens  
2. The loading bar is at 0% and states that it's now loading the data
3. The loading bar progresses and states that it's now loading the world
4. The loading bar completes and the tester gets sent into the overworld

## Alternative procedures

3.1 an error while fetching data from the backend - the user is notified of the error and can start a demo version of the game

## Criticality

High

## Linkages

N/A
