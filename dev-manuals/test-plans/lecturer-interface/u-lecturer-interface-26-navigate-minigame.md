# Lecturer-Interface: Navigate minigame (`u.lecturer-interface-26`)


Version: V1.0, 30.08.2022 \
Author: Aaron Schmid

## Description

The different input options can be navigated.

## Precondition

At least one course is created. 
The tester is on the view of the course (`/courses/<course-id>/worlds/<world-id>/minigames`)
and sees a list of minigames.
Some tab of the sidebar is focused.

## Postcondition

The focus is on the edit button in row below the original row.

## Typical procedure

1. Click <kbd>right</kbd>
2. The focus is on the first input option
3. Click <kbd>down</kbd>
4. The focus is on the input option below
5. Click <kbd>up</kbd>
6. The focus is on the input option above
7. Click <kbd>right</kbd>
8. The focus is on the minigame selection
9. Click <kbd>down</kbd>
10. The focus is on the minigame selection below
11. Click <kbd>right</kbd>
12. The focus is on edit button
13. <kbd>down</kbd>
14. The focus is on the edit button below
15. Click <kbd>up</kbd>
16. The focus is on the edit button in the row below the original row

## Alternative procedures

4.1 no input option below \
4.1.1 the first input option is selected \
6.1. no input option above \
6.1.1 the last input option is selected \
10.1 no minigame selection below \
10.1.1 the first minigame selection is selected \
14.1 no edit button below \
14.1.1 the first edit button option is selected \
16.1. no edit button above \
16.1.1 the last topic edit button is selected

## Criticality

Medium

## Linkages

- [Show courses (`u.lecturer-interface-23`)](u-lecturer-interface-23-navigate-sidebar.md)
