# Lecturer-Interface show courses (`u.lecturer-interface-2`)


Version: V1.0, 08.08.2022 \
Author: Max Kästner

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
5. Enter a name, description and semester (in format `WS-22`) that combination does not already exist
6. Hit `Ok` button of modal
7. A feedback toast message appears which contains that course was created
8. The created course is listed in the courses view

## Alternative procedures

5.1: The semester is not in the right format: \
    5.1.1 Hit `Ok` button of modal \
    5.1.2 A feedback toast message appears which contains that course was not created \
    5.1.3 The courses view has no new course

## Criticality

High

## Linkages

- [Show courses (`u.lecturer-interface-1`)](u-lecturer-interface-01-show-courses.md)