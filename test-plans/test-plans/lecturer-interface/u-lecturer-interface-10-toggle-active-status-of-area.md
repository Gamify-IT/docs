# Lecturer-Interface: Change active status of area (`u.lecturer-interface-10`)


Version: V1.0, 09.08.2022 \
Author: Max Kästner

## Description

The active status of a world or dungeon (which is linked to the world of a view) can be changed on the world view.

## Precondition

At least one course with a world is created. The tester is located where the area can be configured.

## Postcondition

The active status of an area was updated and is shown in the view.

## Typical procedure

1. Click the active switch button of an area (select world/dungeon by static name)
2. The switch button inverted the `active` state.
3. Depending on the previous state:
    - If the area was previously not active, a success message appears
    - If the area was previously active, a warning message appears

## Alternative procedures


## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)