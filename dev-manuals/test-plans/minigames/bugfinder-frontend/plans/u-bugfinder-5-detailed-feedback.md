# Bugfinder detailed feedback (u.bugfinder-5)


Version: V1.0, 05.08.2022
Author: Timo Schnaible
Tester: -

## Description

When the player selected the bugs he submits his solution with the `Submit` button and gets feedback where he sees which bugs he selected correctly. To get a detaiiled feedback he can hover over the higlighted bugs. Then a popup shows the correctness of the categories `Selected right`, `Error type` and `Code fixed`.

## Precondition

The tester selected bugs and didn't submit.

## Postcondition

Player saw in which category he failed.

## Typical procedure

1. Press start to start the game
2. The first code snipped is shown
3. Select the bugs
4. Press the `Submit` button
5. The feedback appears
6. Hover over a highlighted bug
7. A popup appears with feedback about the correctness in each category
8. Hover next to the bug
9. The popup disappears

## Alternative procedures

7.1 The popup contains the wrong feedback \
7.2 The popup is empty \
7.3 The popup doesn't appear \
8.1 Accidently close the browser tab \
9.1 The popup doesn't disappear

## Criticality

Medium

## Linkages