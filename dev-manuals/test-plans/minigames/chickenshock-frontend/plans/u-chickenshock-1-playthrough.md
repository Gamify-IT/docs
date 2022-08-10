# Chickenshock: Playthrough (`u.chickenshock-1`)

Version: V1.1, 2022-08-09, improve format \
Author: Martin Lautenschlager, Levi Otterbach, Leon Hofmeister

## Description

This use case verifies that a normal run through the game works correctly.

## Precondition

A configuration has been chosen that both the frontend and the backend know about. The backend has stored test data about this configuration.

## Postcondition

The game result the tester achieved is saved in the chickenshock database.
The game shows the endscreen.

## Typical procedure

1. The tester presses the "Start" button
2. The game scene is loaded
3. A random question with corresponding answers of the given config is loaded. The question is shown on the big sign, there are as many chickens as possible answers and the timer in the top left of the screen starts counting down
4. The tester can move the camera in a restricted area by moving around his mouse and can shoot the weapon by pressing the "Left Mouse" button
5. When aiming the crosshair on a chicken and shooting the chicken is killed and disappears. Corresponding feedback is shown on the big sign and the remaining chickens. The tester cannot shoot the weapon anymore
6. The remaining chickens disappear after a small delay, a new question is loaded and the tester can shoot the weapon again
7. When the timer runs out the end screen is loaded
8. The end screen shows the amount of points the tester scored (can also be negative)
9. Pressing "Quit" exits the game

## Alternative procedures

1.1. Hovering over the "?" symbol in the lower right corner shows a short tutorial of the game \
6.1. If the answered question was the last one, the tester will be sent to the end screen \
9.1. Pressing play again restarts the game

## Criticality

High

## Linkages

- [Exit without starting (`u.chickenshock-2`)](u-chickenshock-2-close-without-starting.md)

