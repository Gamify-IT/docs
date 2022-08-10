# HUD: Submenus work (`u.hud-5`)

Number: U.hud.5
Version: V0.1, 2022-08-10, create test case
Author: Michael Linder
Tester: -

## Description

This test verifies that sub-menus inside the menu work as intended.  

## Precondition

Overworld is loaded.

## Postcondition

## Typical procedure

1. The tester opens the menu with <kbd>Esc</kbd>
2. Click the `Achievements` button and ensure it opens the `Achievements` sub-menu
3. Scroll up and down (if possible)
4. Click the `back` button to close the sub-menu and (re-)open the menu
5. Repeat `2.-4.` for the `Keybindings` submenu
8. Click the `Character Selection` button and ensure it opens the `Character Selection` sub-menu
9. Click the left arrow and right arrow buttons to cycle through characters
10. The characters have different sprites
11. Only the main Player model has a `confirm` button
12. Click the `back` button to close the sub-menu and (re-)open the menu

## Alternative procedures

N/A

## Criticality

Medium

## Linkages

N/A
