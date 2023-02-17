# Memory: Playthrough Singleplayer(`u.memory-1`)

Version: V1.0, 17.02.2023 
Author: Patrick Ng, Maximilian Wohlfarth

## Description

This use case verifies that a normal run through the game works correctly.

## Precondition

Correct data is transfered into pairs for the memory game

## Postcondition

The game was finished and at the top of the left box is written "Well done!" + there are no cards left.
Additionally, the summory box contains all found pairs.

## Typical procedure


1. open website via npm run serve
2. click on Singleplayer
3. click on a card to flip it
4. click on another card to flip it. 
5. Focus on the borders of the flipped cards. The border should be either green or red depending if the pair is matching or not. Green for matching red for no match.
6. Try flipping a third card, while there are already two cards flipped. It should not be possible.
7. redo step 3, 4 and 5 until no card is left 
8. Focus on the Summary box. All the found pairs should be correctly displayed.
9. There should be a "Well done!" at the top of the left box.

## Alternative procedures

N/A

## Criticality

High

## Linkages

