# Bugfinder Show detailed feedback (`u.bugfinder-5`)


Version: V1.1, 05.08.2022, Improve format and wording \
Author: Timo Schnaible, Leon Hofmeister \
Tester: -

## Description

After submitting their corrected version, the player gets feedback where he sees which bugs he selected correctly. To get detailed feedback, he can hover over the highlighted bugs. A popup now shows the correctness of his solution for several categories (`Was a bug`, `Error type` and `Code fixed`).

## Precondition

The player selected bugs and didn't submit their solution yet.

## Postcondition

Player saw in which category he failed.

## Typical procedure

1. Press the `Submit` button
2. The feedback appears
3. Hover over a highlighted bug
4. A popup appears with feedback about the correctness in each category
5. Hover next to the bug
6. The popup disappears

## Alternative procedures

4.1 The popup doesn't appear \
4.2 The popup is empty \
4.3 The popup contains the wrong feedback \
6.1 The popup doesn't disappear

## Criticality

High

## Linkages

- [Show general feedback (`u.bugfinder-4`)](u-bugfinder-4-show-general-feedback.md)
- [Bug selection (`u.bugfinder-2`)](u-bugfinder-2-bug-selection.md)
