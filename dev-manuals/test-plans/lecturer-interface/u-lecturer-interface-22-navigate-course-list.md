# Lecturer-Interface: Navigate course list (`u.lecturer-interface-22`)


Version: V1.0, 30.08.2022 \
Author: Aaron Schmid

## Description

The course list can be navigated

## Precondition

At least three course are created. 
The tester sees the list of courses and has focus on one course.

## Postcondition

A original course is selected.

## Typical procedure

1. Click <kbd>down</kbd>
2. The course below is focused
3. Click <kbd>up</kbd>
4. The course above is focused

## Alternative procedures

2.1 no course below \
2.1.1 the first course is selected \
4.1. no course above \
4.1.1 the last course is selected

## Criticality

Medium

## Linkages

- [Show courses (`u.lecturer-interface-1`)](u-lecturer-interface-01-show-courses.md)
