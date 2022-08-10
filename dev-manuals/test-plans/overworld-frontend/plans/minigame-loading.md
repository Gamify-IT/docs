# Minigame: Loading works (`u.minigame-2`)

Number: U.minigame.2  
Version: V0.3, 2022-08-09, adapt typical procedure  
Author: Florian Wüst  
Tester: -  

## Description

This use case verifies that everything regarding minigames loading in the overworld works as intended.  
This includes loading the correct minigame with the right configuration.

## Precondition

The minigame is configured in the overworld, including that its spot is visible and it has a configuration.

## Postcondition

The correct minigame with the right configuration gets loaded.

## Typical procedure

1. The tester walks to the minigame spot
2. The tester walks into the minigame spot
3. The minigame overview panel opens
4. The tester presses the `start` button
5. The correct minigame starts  
6. The correct configuration is passed

## Alternative procedures

4.1. The user doesn't want to start a game - he aborts starting by pressing `cancel`

## Criticality

High

## Linkages

- [Minigame Spots (`u.minigame-1`)](u-minigame-1-spot-is-well-configured.md)
