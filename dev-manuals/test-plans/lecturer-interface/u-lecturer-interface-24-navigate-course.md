# Lecturer-Interface: Course navigation (`u.lecturer-interface-24`)


Version: V1.0, 30.08.2022 \
Author: Aaron Schmid

## Description

The different input options can be navigated.

## Precondition

At least one course is created. 
The tester is on the view of the course (`/courses/<course-id>`)
and sees the input options of a course.
A sidebar tab is focused.

## Postcondition

The focus is on the original input option.

## Typical procedure

1. Click <kbd>right</kbd>
2. The initial input option is focused
3. Click <kbd>down</kbd>
4. The input option below is focused
5. Click <kbd>up</kbd>
6. The input option above is focused

## Alternative procedures

4.1 no input option below - the first input option is focused \
6.1. no input option above - the last input option is focused

## Criticality

Medium

## Linkages

- [Sidebar navigation (`u.lecturer-interface-23`)](u-lecturer-interface-23-navigate-sidebar.md)
