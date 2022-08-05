# Bugfinder bug cancellation (u.bugfinder-3)


Version: V1.0, 05.08.2022
Author: Timo Schnaible
Tester: -

## Description

When the player selected a bug he has the ability to cancel his selection. Therefore he clicks on the highlighted bug. Then the bug is removed and the word or whitespace is reseted to its original value and no longer highlighted.

## Precondition

The tester selected a bug and didn't submit. The selected bug is highlighted.

## Postcondition

The bug is no longer highlighted and the original value is shown.

## Typical procedure

1. Press start to start the game
2. The first code snipped is shown
3. Press on a bug
4. The edit modal is displayed.
5. Correct the bug in the input field
6. Select an error type if no whitespace was selected
7. Press `Ok`
8. The corrected version is shown and the bug is highlighted
9. Press on the corrected and highlighted version
10. The corrected version is no longer displayed and the bug is no longer highlighted

## Alternative procedures

8.1. The game crashes \
10.1. Nothing happens \
10.2. The bug is still highlighted but the corrected version is no longer shown \
10.3. The corrected version is still shown but the bug is no longer highlighted

## Criticality

High

## Linkages

- [Bug selection (u.bugfinder-2)](u-bugfinder-2-bug-selection.md)
- [Feedback (u.bugfinder-5)](u-bugfinder-4-feedback.md)
