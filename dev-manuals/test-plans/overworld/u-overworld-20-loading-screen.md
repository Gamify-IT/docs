# Overworld: Loading screen (`u.overworld-20`)

Version: v1.0, 2022-08-27, create test plan \
Author: Florian Wüst, Gilian Rehm

## Description

This use case verifies that the loading screen works as intended.  

## Precondition

The tester is logged in

## Postcondition

The tester is in the overworld.

## Typical procedure

1. The loading screen opens  
2. The loading bar is at 0% and states "LOADING DATA..."
3. The loading bar is at 50% and states "LOADING WORLD..."
4. The loading bar completes and the tester is in the overworld

## Alternative procedures

3.1 if there is an error while fetching data from the backend, a screen appears stating that and the tester can start a demo version of the game

## Criticality

High

## Linkages

N/A
