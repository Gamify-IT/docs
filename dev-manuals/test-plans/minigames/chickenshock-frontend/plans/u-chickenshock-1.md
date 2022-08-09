# Chickenshock Game playthrough (`u.chickenshock-1`)

Version: v0.1, 2022-08-09  
Author: Martin Lautenschlager, Levi Otterbach
Tester: -

## Description

This use case verifies that a normal run through the game works correctly.

## Precondition

The tester initializes the game field in the overworld with a fitting configuration of the chickenshock game and walks into the game field to start the chickenshock minigame

## Postcondition

The game result the tester achieved is saved in the chickenshock database

## Typical procedure

1. The tester presses the start button
2. The game scene is loaded
3. A random question with corresponding answers of the given config is loaded. The question is shown on the big sign, there are as many chickens as possible answers and the timer in the top left of the screen starts counting down
4. The tester can move the camera in a restricted area by moving around his mouse and can shoot the weapon by pressing the left mouse button
5. When aiming the crosshair on a chicken and shooting the chicken is killed and disappears. Corresponding feedback is shown on the big sign and the remaining chickens. The tester cannot shoot the weapon anymore
6. After 1 second the remaining chickens disappear, a new question with new chickens is loaded and the tester can shoot the weapon again
7. When the timer runs out the end screen will be loaded
8. The end screen shows the amount of points the tester scored (can be negative)
9. Pressing "Quit" returns the tester to the overworld

## Alternative procedures

6.1 If the answered question was the last one, the tester will be sent to the end screen, continue with 8.
9.1 Pressing play again restarts the game, continue with 2.

## Criticality

High

## Linkages

