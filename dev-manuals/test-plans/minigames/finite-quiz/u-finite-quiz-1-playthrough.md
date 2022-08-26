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

1. The game is loaded with a valid config
2. A question with corresponding answers of the given config is loaded. The question is shown in the big box in the upper half of the screen and there are as many buttons in the lower half of the screen as there are possible answers.
3. The tester chooses an answer by clicking the button of the answer they want to choose.
4. After answering, corresponding feedback wether the question was answered right or wrong is shown for a short time
5. After the feedback, the next question is loaded
6. Once the tester answered all questions, a feedback screen is shown that informs the tester of his overall performance
7. Pressing "Close" exits the game

## Alternative procedures

x.1. Clicking "Restart" restarts the game with the same config \
x.2. Clicking "Close" exits the game 

## Criticality

High

## Linkages


