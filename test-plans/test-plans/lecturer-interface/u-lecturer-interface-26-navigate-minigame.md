# Lecturer-Interface: Minigame navigation (`u.lecturer-interface-26`)


Version: V1.0, 30.08.2022 \
Author: Aaron Schmid

## Description

The different input options can be navigated.

## Precondition

At least one course is created. 
The tester is on the view of the course (`/courses/<course-id>/worlds/<world-id>/minigames`)
and sees a list of minigames.
A sidebar tab is focused.

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

4.1. no input option below - the first input option is focused \
6.1. no input option above - the last input option is focused \
10.1. no minigame selection below - the first minigame selection is focused \
14.1. no edit button below - the first edit button option is focused \
16.1. no edit button above - the last topic edit button is focused

## Criticality

Medium

## Linkages

- [Sidebar navigation (`u.lecturer-interface-23`)](u-lecturer-interface-23-navigate-sidebar.md)
