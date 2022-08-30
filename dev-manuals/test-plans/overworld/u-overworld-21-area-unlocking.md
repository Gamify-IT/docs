# Overworld: Area unlocking (`u.overworld-21`)

Version: v1.0, 2022-08-30, create test plan \
Author: Gilian Rehm, Florian Wüst

## Description

This use case verifies that unlocking areas works as intended.  

## Precondition

The tester is logged in.
All minigames in world 1 except one are completed.

## Postcondition

All minigames in world 1 are completed.
Dungeon 1 of world 1 is unlocked.

## Typical procedure

1. Player walks to not completed minigame
1. Player completes minigame
1. Dungeon 1 world 1 unlocks

## Alternative procedures

3.1. Nothing unlocks because there is no (further) unlockable area \
3.2. Dungeon 1 cannot be unlocked - try to unlock one of the remaining dungeons in order \
3.3. No dungeon in world 1 can be unlocked - try to unlock one of the remaining worlds in order

## Criticality

High

## Linkages

N/A
