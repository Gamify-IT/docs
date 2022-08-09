# Bugfinder Revert bug correction (`u.regex-game-3`)


Version: V1.0, 07.08.2022 \
Author: Leon Layer \
Tester: -

## Description

A new quiz is added to the game, i.e. a new regex with three possible answers. the game automatically tests whether the new quiz is correct, i.e. whether two possible answers are incorrect and the regex does not match, and whether one possible answer is correct and the regex does match. when trying to add an incorrect quiz to the game, an error message is logged in the browser console.

## Precondition

When the game is started, the console does not display a message about an incorrect quiz. 

## Postcondition

When the game is started, the console does not display a message about an incorrect quiz. 

## Typical procedure

1. the tester opens the file data.ts and inserts a new correct quiz in such a way that it is additionally included in the list of return values of the function. 

        export function quizData(): Quiz[] {} 

2. There is no error message in the browser console.
3. The quiz is displayed at the right place in the game.

## Alternative procedures

## Criticality

Medium

## Linkages

