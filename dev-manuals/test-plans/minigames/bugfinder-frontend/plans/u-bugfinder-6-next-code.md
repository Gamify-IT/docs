# Bugfinder detailed feedback (u.bugfinder-5)


Version: V1.0, 05.08.2022
Author: Timo Schnaible
Tester: -

## Description

When the player submited his solution he can get to the next code snipped by pressing the `Next Code` button which replaced the `Submit` button. The button is only shown if there is another code snipped. Additionally the virtual chat partner asks for help with another bug in the chat.

## Precondition

The tester submited and another code snipped exists.

## Postcondition

The next code snipped is shown.

## Typical procedure

1. Press start to start the game
2. The first code snipped is shown
3. Select the bugs
4. Press the `Submit` button
5. The `Submit` button gets replaced by the `Next Code` button
6. The virtual chat partner asks for help with another bug
7. Press the `Next Code` button
8. A chat message from the player appears where he says he wants to help
10. The virtual chat partner is happy about the help
9. The next code snipped appears 


## Alternative procedures

5.1. The `Next Code` button doesn't appear
5.2. The `Submit` button doesn't disappear
6.1. No chat message appears
6.2. A wrong chat message appears
8.1. No chat message appears
8.2. A wrong chat message appears
10.1. No chat message appears
10.2. The virtual chat partner is unhappy about the help
11.1. Th next code snipped doesn't appear


## Criticality

High

## Linkages