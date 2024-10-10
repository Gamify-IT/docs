# Regex Game: Select an answer (`u.regex-game-2`)

Version: V1.0, 09.08.2022, initial test \
Author: Leon Hofmeister

## Description

Tests that the user can select right and wrong answers.

## Precondition

The game is started and preinitialized with at least two regexes. The first regex is shown.

## Postcondition

Both regexes were shown, one was answered correctly, one incorrectly.

## Typical procedure

1. Select a wrong answer
2. Negative feedback is shown
3. The player score doesn't change
4. The next regex is shown
5. Select a correct answer
6. Positive feedback is shown
7. The next regex is shown

## Alternative procedures

3.1. The player score decreases \
7.1. The game only has two regexes - the game ends

## Criticality

High

## Linkages

