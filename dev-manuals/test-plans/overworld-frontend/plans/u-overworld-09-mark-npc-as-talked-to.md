# Overworld: NPC mark as talked to (`u.overworld-9`)

Version: v1.2, 2022-08-11, adapt to new template \
Author: Florian Wüst, Gilian Rehm, Leon Hofmeister  

## Description

This test case verifies that a NPC shows whether he has something new to say or not.

## Precondition

The NPC is configured in the overworld, corresponding data exists in the backend, and the NPC has not been talked with yet.

## Postcondition

The NPC has no new things to say and the sprite to show that he has something new to say is no longer visible

## Typical procedure

1. The tester starts the game
2. The tester goes to the NPC
3. The tester checks that the "I have unheard content" sprite is shown
4. The tester talks with the NPC
5. The tester checks that the NPC no longer has the "I have unheard content" sprite

## Alternative procedures

5.1 The sprite is still shown because the NPC still has something new to say

## Criticality

Medium

## Linkages

N/A
