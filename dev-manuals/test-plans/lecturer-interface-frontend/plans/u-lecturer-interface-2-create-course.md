# Lecturer-Interface show courses (`u.lecturer-interface-2`)


Version: V1.0, 08.08.2022
Author: Max Kästner
Tester: -

## Description

A course can be created on the courses view.

## Precondition

Nothing

## Postcondition

A new course was created.

## Typical procedure

1. Open the lecturer interface
2. The view displays a `create new course` button
3. Press the `create new course` button
4. A modal opens
5. Enter a name and semester (in format `WS-22`) that combination does not already exist
6. Enter a description
7. Hit `Ok` button of modal
8. A feedback toast message appears which contains that course was created
9. The created course is listed in the courses view

## Alternative procedures

2.1 view does not display the `create new course` button \
4.1 Nothing happens \
8.1 No toast message appears \
8.2 A toast message appears which contains that there was an error creating the course \
9.1 The created course is not listed in the courses view

## Criticality

High

## Linkages

- [Show courses (`u.lecturer-interface-1`)](u-lecturer-interface-1-show-courses.md)