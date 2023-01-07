# Overworld: Teleporter Scene Loading (`u.overworld-26`)

Version: v1.0, 2022-01-05, create test plan \
Author: Patrick Holtz

## Description

This use case tests whether data remains after the player teleporters towards another scene.

## Precondition

The tester is logged in.

## Postcondition

--

## Typical procedure

1. Unlock a teleporter `1` in some world.
1. Unlock a teleporter `2` in another world or dungeon.
1. Open the menu of teleporter `2`
1. Teleporter `1` should show up. Teleport towards it. 
1. When arriving at teleporter `1`, open its menu.
1. Teleporter `2` should show up.

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A
