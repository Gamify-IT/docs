# Bugfinder` Show general feedback (`u.bugfinder-4`)


Version: V1.1, 05.08.2022, Improve format and wording	
Author: Timo Schnaible, Leon Hofmeister
Tester: -

## Description

After submitting their solution, the player gets feedback. The player automatically asks the chat partner if his solution is correct or not. Additionally, correctly fixed bugs get visually highlighted while incorrectly/ not fixed bugs get highlighted in another distinct color.

## Precondition

The tester selected **some, but not all,** bugs and didn't submit his solution.

## Postcondition

The bugs aren't editable and a feedback is shown.

## Typical procedure

1. Submit your corrections to the chat partner
2. A chat message from the player appears where he says he found the bugs
3. The bug feedback appears with correctly identified bugs highlighted in one color (`green`?), and incorrect code in another (`red`?)
4. The feedback chat messages appear

## Alternative procedures

2.1 No chat message appears \
3.1 The code doesn't highlight \
3.2 The code highlights cannot be easily distinguished \
3.3 The code highlights the wrong words \
4.1 No chat message appears \
4.2 The chat message contains a wrong feedback

## Criticality

High

## Linkages

- [Bug selection (`u.bugfinder-2`)](u-bugfinder-2-bug-selection.md)
- [Show detailed feedback (`u.bugfinder-5`)](u-bugfinder-5-show-detailed-feedback.md)
- [Show next code (`u.bugfinder-6`)](u-bugfinder-6-show-next-snippet.md)
