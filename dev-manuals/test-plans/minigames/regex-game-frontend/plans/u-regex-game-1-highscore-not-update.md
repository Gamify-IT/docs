# Highscore not update test (`u.regex-game-1`)

Version: V1.0, 07.08.2022 \
Author: Leon Layer \
Tester: -

## Description

Tests if the high score not increases when a lower or same score is reached.

## Precondition

The game is in a state where the maximum possible higscore has not yet been reached.

## Postcondition

by playing, if the current higscore will not be exceeded, the higscore will be updated in the menu. 

## Typical procedure

1. the tester plays the game but does not have a score of 0.
2. the tester sees his previous higscore in the menu wich is not 0.
3. by trying again, he doesnt surpasses his previous best performance
4. the game will not update his higscore in the meu.

## Alternative procedures

2.1. In the menu still 0 or another wrong score is displayed as highscore \
3.1. the highscore is updated and a lower highscore is displayed \

## Criticality

Low

## Linkages

