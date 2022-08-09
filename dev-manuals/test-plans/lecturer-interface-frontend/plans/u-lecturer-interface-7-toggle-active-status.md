# Lecturer-Interface toggle active status (`u.lecturer-interface-7`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The active status of a specific course can be changed on its view.

## Precondition

At least one course is created. The tester is on the view of the course (`/courses/<course-id>`)

## Postcondition

The active status of the course was toggled.

## Typical procedure

1. Click the active switch button
2. The switch button switched from ative to not active or from not active to active.
3. Depends on the status before:
    - In case the course was not active before, a green toast message appears which contains the course was activated
    - In case the course was active before, a red toast message appears which contains the course was deactivated

## Alternative procedures

3.1 No toast message appears

## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-3-show-specific-course.md)