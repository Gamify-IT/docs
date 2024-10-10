# Overworld: Teleporter Unlocking (`u.overworld-25`)

Version: v1.0, 2022-01-05, create test plan \
Author: Patrick Holtz

## Description

This use case tests whether the unlocking process works correctly and the resulting data is saved correctly in the backend.

## Precondition

The tester is logged in.  
A teleporter `1` is unlocked.  
The tester stands in front of a teleporter `2` **in another area** and opens its menu.

## Postcondition

A unlocked teleporter shows up in the menu of every other teleporter even after a restart.

## Typical procedure

1. Teleporter `1` should show up in the menu.
2. Teleport to `1`, and open its menu.
3. Teleporter `2` should show up in the menu.
4. Teleport to `2`.
5. Go back to the course selection menu and start the overworld again.
6. Repeat steps `1.-3.` once.

## Alternative procedures

N/A

## Criticality

Medium

## Linkages

N/A
