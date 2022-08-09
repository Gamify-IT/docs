# Highscore not update test (`u.regex-game-1`)

Version: V1.0, 07.08.2022 \
Author: Leon Layer \
Tester: -

## Description

Tests that the highscore doesn't change when score <= highscore.

## Precondition

The game is in a state where the maximum possible higscore has not yet been reached.

## Postcondition

The highscore has its original value.

## Typical procedure

1. the tester plays the game but does not have a score of 0.
2. the tester sees his previous higscore in the menu wich is not 0.
3. by trying again, he doesnt surpasses his previous best performance
4. the highscore in the menu is not updated

## Alternative procedures


## Criticality

Low

## Linkages

