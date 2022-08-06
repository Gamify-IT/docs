# Bugfinder Show next code (`u.bugfinder-6`)


Version: V1.1, 05.08.2022, Improve format and remove redundant procedure parts \
Author: Timo Schnaible, Leon Hofmeister \
Tester: -

## Description

After submitting a solution, there can be a new snippet with new bugs. Additionally, the chat partner asks for help again.

## Precondition

The tester submitted a solution already and another code snippet exists.

## Postcondition

The next code snippet is shown.

## Typical procedure

1. The `Submit` button was replaced with a `Next Code` button
2. The chat partner asks for help with another bug
3. Press the `Next Code` button
4. A chat message from the player appears where he says he wants to help
5. The virtual chat partner is happy about the help
6. The next code snippet appears


## Alternative procedures

1.1. The `Next Code` button doesn't appear \
1.2. The `Submit` button doesn't disappear \
2.1. No chat message appears \
2.2. A wrong chat message appears \
2.2.1. The chat partner doesn't want any further help \
4.1. No chat message appears \
4.2. A wrong chat message appears \
5.1. No chat message appears \
5.2. The virtual chat partner is unhappy about the help \
6.1. The next code snippet doesn't appear

## Criticality

High

## Linkages

- [Show general feedback (`u.bugfinder-4`)](u-bugfinder-4-show-general-feedback.md)
- [Bug selection (`u.bugfinder-2`)](u-bugfinder-2-bug-selection.md)
