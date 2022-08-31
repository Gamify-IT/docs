# Lecturer-Interface: NPC navigation (`u.lecturer-interface-27`)


Version: V1.0, 30.08.2022 \
Author: Aaron Schmid

## Description

The different input options can be navigated.

## Precondition

At least one course is created. 
The tester is on the view of the course (`/courses/<course-id>/worlds/<world-id>/npcs`)
and sees a list of NPCs.
A sidebar tab is focused.

## Postcondition

The focus is on the edit button in the original row.

## Typical procedure

1. Click <kbd>right</kbd>
2. The focus is on the first input option
3. Click <kbd>down</kbd>
4. The focus is on the second input option
5. Click <kbd>up</kbd>
6. The focus is on the first input option
7. Click <kbd>right</kbd>
8. The focus is on edit button
9. Click <kbd>down</kbd>
10. The focus is on the edit button below
11. Click <kbd>up</kbd>
12. The focus is on the edit button on top

## Alternative procedures

4.1 no input option below - the first topic input option is focused \
6.1. no input option above - the last topic input option is focused \
10.1 no edit button below - the first edit button is focused \
12.1. no edit button above -  the last edit button is focused

## Criticality

Medium

## Linkages

- [Sidebar navigation (`u.lecturer-interface-23`)](u-lecturer-interface-23-navigate-sidebar.md)
