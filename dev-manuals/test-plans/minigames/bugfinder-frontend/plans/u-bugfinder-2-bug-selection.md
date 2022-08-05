# Bugfinder bug selection (u.bugfinder-2)


Version: V1.0, 05.08.2022
Author: Timo Schnaible
Tester: -

## Description

When the the game is started, a code snipped is displayed and the player can select every word or whitespace as bug. When \a bug is selected a modal appears to correct the bug and select the type of the bug. If a whitespace is selected the error type selection is not shown. The bug can be confirmed by a `Ok`-button.

## Precondition

The tester started a new game.

## Postcondition

The selected bug is highlighted and the from the player corrected version is shown.

## Typical procedure

1. Press start to start the game
2. The first code snipped is shown
3. Press on a bug
4. The edit modal is displayed.
5. Correct the bug in the input field
6. Select an error type if no whitespace was selected
7. Press `Ok`
8. The corrected version is displayed and the bug is highlighted

## Alternative procedures

2.1. The game crashes \
4.1. Nothing happens \
8.1. The bug is not highlighted but the corrected version is displayed \
8.2. The corrected version is not displayed but the bug is highlighted \
8.3. The corrected version is not displayed and the bug is not highlighted 

## Criticality

High

## Linkages


