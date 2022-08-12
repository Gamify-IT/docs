# Overworld: Pause menu (`u.overworld-16`)

Version: V1.1, 2022-08-11, adapt to new template \
Author: Michael Linder, Florian Wüst

## Description

This use case verifies that the pause menu works as intended and that the game is paused while it is open.  

## Precondition

The overworld is loaded.

## Postcondition

The menu is not visible and the game is no longer paused. 

## Typical procedure

1. The tester opens the pause menu with <kbd>Esc</kbd>
2. The protagonist can no longer move or interact with anything, and the environment is paused
3. The tester closes the pause menu with <kbd>Esc</kbd>
4. The game is resumed and the protagonist can walk/interact again

## Alternative procedures

1.1. The tester opens the menu with the button in the upper-left corner \
3.1. The tester closes the menu with the `Resume` button

## Criticality

Medium

## Linkages

N/A
