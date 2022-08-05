# Bugfinder Bug selection (`u.bugfinder-2`)


Version: V1.1, 05.08.2022, Improve format and differentiate between whitespace- and non-whitespace bug
Author: Timo Schnaible, Leon Hofmeister
Tester: -

## Description

When a bug is selected, a modal appears to correct the bug and select the bug type. If whitespace is selected, the error type selection is not shown. The dialog can be closed succesfully.

## Precondition

The tester started a game with a snippet that contains (at least) one whitespace (=missing code) and one visible (=misspelled code) bug.

## Postcondition

The selected bug is highlighted and the player corrected version is shown instead of the original value.

## Typical procedure

1. Click on a non-whitespace bug
2. The edit modal is displayed
3. Correct the bug in the input field
4. Select an error type
5. Press `Ok`
6. The corrected version is displayed and the bug is highlighted
7. Click on a whitespace bug
8. The edit modal is displayed
9. Correct the bug in the input field
10. The modal does not have an option to select the error type
11. Press `Ok`
12. The second corrected version is displayed and the second bug is highlighted

## Alternative procedures

1.1. The game crashes \
6.1. Nothing happens \
6.2. The bug is not highlighted but the corrected version is displayed \
6.3. The corrected version is not displayed but the bug is highlighted \
6.4. The corrected version is not displayed and the bug is not highlighted \
10.1. There is an option to select the error type \
12.1. Nothing happens \
12.2. The bug is not highlighted but the corrected version is displayed \
12.3. The corrected version is not displayed but the bug is highlighted \
12.4. The corrected version is not displayed and the bug is not highlighted

## Criticality

High

## Linkages

- [Cancel bug submission (`u.bugfinder-3`)](u-bugfinder-3-cancel-bug-submission.md)
- [Show general feedback (`u.bugfinder-4`)](u-bugfinder-4-show-general-feedback.md)

