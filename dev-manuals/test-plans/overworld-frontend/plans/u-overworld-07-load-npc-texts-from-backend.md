# Overworld: NPC load text from backend (`u.overworld-7`)

Version: v1.2, 2022-08-11, adapt to new template \
Author: Florian Wüst, Gilian Rehm, Leon Hofmeister  

## Description

Verifies that the dialogue lines of a NPC can be loaded dynamically from the database, and the NPC uses those dialogue lines when talked to.

## Precondition

The NPC is configured in the overworld and corresponding data exists in the backend.

## Postcondition

The dialogue lines stored in the backend are set as the dialogue lines of the NPC.

## Typical procedure

1. The tester starts the game with a running database
2. The tester goes to the NPC
3. The tester starts a dialogue
4. The correct lines are shown

## Alternative procedures

4.1 Not the correct lines are shown

## Criticality

Medium

## Linkages

- [NPC show dialogue box (`u.overworld-08`)](u-overworld-08-show-npc-dialogbox.md)
