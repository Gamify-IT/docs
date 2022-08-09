# Lecturer-Interface change active status of area (`u.lecturer-interface-10`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The active status of a world or dungeon (which is linked to the world of a view) can be changed on the world view.

## Precondition

At least one course is created. The tester is on the view of a world of a course (`/courses/<course-id>/worlds/<world-index>`)

## Postcondition

The active status of an area was updated and is shown in the view.

## Typical procedure

1. Click the active switch button of an area (select world/dungeon by static name)
2. The switch button switched from ative to not active or from not active to active.
3. Depends on the status before:
    - In case the area was not active before, a green toast message appears which contains the area was activated
    - In case the area was active before, a red toast message appears which contains the area was deactivated

## Alternative procedures

3.1 No toast message appears

## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)