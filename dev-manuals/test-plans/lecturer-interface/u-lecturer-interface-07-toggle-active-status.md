# Lecturer-Interface: Toggle active status (`u.lecturer-interface-07`)


Version: V1.0, 09.08.2022 \
Author: Max Kästner

## Description

The active status of a specific course can be changed on its view.

## Precondition

At least one course is created. The tester is on the view of the course (`/courses/<course-id>`)

## Postcondition

The active status of the course was toggled.

## Typical procedure

1. Click the active switch button
2. The switch button inverted the `active` state.
3. Depends on the status before:
    - In case the course was not active before, a green toast message appears which contains the course was activated
    - In case the course was active before, a red toast message appears which contains the course was deactivated

## Alternative procedures


## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
