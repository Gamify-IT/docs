# Crosswordpuzzle finish game (`u.crosswordpuzzle-3`)

Version: v1.0, 2022-08-12, created test plan \
Author: Aaron Schmid


## Description

This use case verifies that the game can be finished.

## Precondition

A configuration has been stored in the backend and selected in the frontend.

## Postcondition

A modal is shown where you result is displayed.

## Typical procedure

1. Open the crossword-puzzle
2. Press the `start` button
3. Input the correct answers in the crosswordpuzzle
4. Press the `Evaluate` button
5. A modal is shown that says `Congratulations!` `Everything right!`

## Alternative procedures
3.1 Input wrong answers in the crosswordpuzzle \
    3.1.1 Press the `Evaluate` button \
    3.1.2 A modal is shown that says `Not the correct answers` `Maybe the next time`

## Criticality

High

## Linkages

- [restart game (`u.crosswordpuzzle-4`)](u-crosswordpuzzle-4-restart-game.md)