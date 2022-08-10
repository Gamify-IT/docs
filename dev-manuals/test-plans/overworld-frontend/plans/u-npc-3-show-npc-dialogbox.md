# NPC show dialogue box (`u.npc-3`)

Number: u.npc-3  
Version: v0.2, 2022-08-04, fix grammar and format  
Author: Florian Wüst, Gilian Rehm, Leon Hofmeister  
Tester: -

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

- [NPC: Load text from backend](u-npc-2-load-npc-texts-from-backend.md)
