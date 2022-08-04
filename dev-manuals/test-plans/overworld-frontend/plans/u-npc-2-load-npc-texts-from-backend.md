# NPC load text from backend (`u.npc-2`)

Number: u.npc-2  
Version: v0.2, 2022-08-04, fix grammar and format  
Author: Florian Wüst, Gilian Rehm, Leon Hofmeister  
Tester: -

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

- [NPC: Dialogue box is shown](u-npc-3-show-npc-dialogbox.md)
