# Lecturer-Interface: Navigate world (`u.lecturer-interface-25`)


Version: V1.0, 30.08.2022 \
Author: Aaron Schmid

## Description

The different input options can be navigated.

## Precondition

At least one course is created. 
The tester is on the view of the course (`/courses/<course-id>/worlds/<world-id>`)
and sees a list of dungeons.
Some tab of the sidebar is focused.

## Postcondition

The focus is on the active toggle in the original row.

## Typical procedure

1. Click <kbd>right</kbd>
2. The focus is on the first topic input option
3. Click <kbd>down</kbd>
4. The focus is on the topic input option blow
5. Click <kbd>up</kbd>
6. The focus is on the input option above
7. Click <kbd>right</kbd>
8. The focus is on the activate-toggle in the same row
9. Click <kbd>down</kbd>
10. The focus is on the activate-toggle blow

## Alternative procedures

4.1 no topic input option below \
4.1.1 the first topic input option is selected \
6.1. no topic input option above \
6.1.1 the last topic input option is selected \
10.1 no activate-toggle below \
10.1.1 the first activate-toggle is selected \

## Criticality

Medium

## Linkages

- [Show courses (`u.lecturer-interface-23`)](u-lecturer-interface-23-navigate-sidebar.md)
