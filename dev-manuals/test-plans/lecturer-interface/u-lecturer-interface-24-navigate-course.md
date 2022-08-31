# Lecturer-Interface: Navigate course (`u.lecturer-interface-24`)


Version: V1.0, 30.08.2022 \
Author: Aaron Schmid

## Description

The different input options can be navigated.

## Precondition

At least one course is created. 
The tester is on the view of the course (`/courses/<course-id>`)
and sees the input options of a course.
Some tab of the sidebar is focused.

## Postcondition

The focus is on the original input option.

## Typical procedure

1. Click <kbd>right</kbd>
2. The focus is on the first input option
3. Click <kbd>down</kbd>
4. The focus is on the input option below
5. Click <kbd>up</kbd>
6. The focus is on the input option above

## Alternative procedures

4.1 no input option below \
4.1.1 the first input option is selected \
6.1. no input option above \
6.1.1 the last input option is selected

## Criticality

Medium

## Linkages

- [Show courses (`u.lecturer-interface-23`)](u-lecturer-interface-23-navigate-sidebar.md)
