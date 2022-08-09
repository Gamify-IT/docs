# Lecturer-Interface show minigames of area (`u.lecturer-interface-11`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The minigames of an area are listed on a view. For minigames of a world the path is `/courses/<course-id>/worlds/<world-index>/minigames` and for a dungeon `/courses/<course-id>/worlds/<world-index>/dungeons/<dungeon-index>/minigames`.

## Precondition

At least one course is created. The tester is on the view of an area minigames list as described in the description above.

## Postcondition

The view lists the list of minigames with the posibillity to change the minigame and change the configuration.

## Typical procedure

1. The view shows at least 12 minigames
2. Every minigame has a little space with a dropdown where minigames can be selected
3. Every minigame has an edit button where the configurations can be edited

## Alternative procedures

## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)