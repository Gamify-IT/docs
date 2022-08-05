# Bugfinder feedback (u.bugfinder-4)


Version: V1.0, 05.08.2022
Author: Timo Schnaible
Tester: -

## Description

When the player selected the bugs he submits his solution with the `Submit` button and gets feedback. Then a chat message from the player appears and the virtual chat partner answers if the bugs are correct or not. Additionally the code gets highlighted in green for correctly selected bugs and in red for wrong or not selected bugs.

## Precondition

The tester selected bugs and didn't submit.

## Postcondition

The bugs aren't editable and a feedback is shown.

## Typical procedure

1. Press start to start the game
2. The first code snipped is shown
3. Select the bugs
4. Press the `Submit` button
5. A chat message from the player appears where he says he found the bugs
6. The bug feedback appears with green and red highlighted code
7. The feedback chat messages appear

## Alternative procedures

5.1 The code doesn't highlight \
5.2 The code highlights with wrong colors \
5.3 The code highlights the wrong words \
6.1 No chat message appears \
6.2 The chat message contains a wrong feedback

## Criticality

High

## Linkages

- [Bug selection (u.bugfinder-2)](u-bugfinder-2-bug-selection.md)
- [Detailed feedback (u.bugfinder-5)](u-bugfinder-5-detailed-feedback.md)
- [Next code (u.bugfinder-6)](u-bugfinder-6-next-code.md)