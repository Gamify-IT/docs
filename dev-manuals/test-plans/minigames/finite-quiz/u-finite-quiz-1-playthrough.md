# Finite-Quiz: Playthrough (`u.finite-quiz-1`)

Version: V1.0, 2022-08-26
Author: Martin Lautenschlager, Levi Otterbach

## Description

This use case verifies that a normal run through the game works correctly.

## Precondition

A configuration has been chosen that both the frontend and the backend know about. The backend has stored test data about this configuration.

## Postcondition

The game result the tester achieved is saved in the finite-quiz database.
The game shows the achieved result.

## Typical procedure

1. The game has been started
2. A question and the possible answers are loaded. Both the question and all possible answers are presented visually as boxes. The question is visually distinct from its answer options
3. The tester chooses an answer by clicking on the answer they want to choose
4. For a short time, feedback is shown wether the chosen answer is correct or incorrect
5. The next question is loaded
6. Once the tester answered all questions, a feedback screen is shown that informs the tester of his overall performance
7. Pressing `Close` exits the game

## Alternative procedures

5.1. There is no next question - skip to step `6` \
7.1. Clicking `Restart` restarts the game with the same config

## Criticality

High

## Linkages


