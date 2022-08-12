# Overworld: NPC show dialogue box (`u.overworld-08`)
 
Version: v1.2, 2022-08-11, adapt to new template \
Author: Florian Wüst, Gilian Rehm, Leon Hofmeister  

## Description

This test case verifies that the dialogue lines of a NPC are displayed correctly, if talked to.

## Precondition

The NPC exists and can be talked with.

## Postcondition

- The dialogue box is displayed

## Typical procedure

1. The tester starts the game
2. The tester goes to the NPC
3. The tester starts a dialogue
4. The dialog box is displayed

## Alternative procedures

4.1 The dialog box is not displayed

## Criticality

Medium

## Linkages

- [NPC load text from backend (`u.overworld-7`)](u-overworld-07-load-npc-texts-from-backend.md)
