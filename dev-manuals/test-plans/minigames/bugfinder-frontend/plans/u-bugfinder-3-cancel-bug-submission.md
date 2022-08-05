# Bugfinder Cancel bug submission (`u.bugfinder-3`)


Version: V1.1, 05.08.2022, Improve format
Author: Timo Schnaible, Leon Hofmeister
Tester: -

## Description

When the player selects a bug, he has the ability to cancel his correction by clicking on the highlighted bug. Then, his correction is removed and the word or whitespace gets reset to its original value and is no longer highlighted.

## Precondition

The tester corrected a bug already.

## Postcondition

The bug is no longer highlighted and the original value is shown.

## Typical procedure

1. The corrected version of that bug is shown and the bug is highlighted
2. Click on the corrected and highlighted version
3. The corrected version is no longer displayed and the bug is no longer highlighted. Instead, the value at that place is the original text again.

## Alternative procedures

1.1. The game crashes \
3.1. Nothing happens \
3.2. The bug is still highlighted but the corrected version is no longer shown \
3.3. The corrected version is still shown but the bug is no longer highlighted

## Criticality

High

## Linkages

- [Bug selection (`u.bugfinder-2`)](u-bugfinder-2-bug-selection.md)
- [Show general feedback (`u.bugfinder-4`)](u-bugfinder-4-show-general-feedback.md)
