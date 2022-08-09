# Lecturer-Interface change game of minigame (`u.lecturer-interface-12`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The game of a minigame can be changed in a dropdown. For minigames of a world the path is `/courses/<course-id>/worlds/<world-index>/minigames` and for a dungeon `/courses/<course-id>/worlds/<world-index>/dungeons/<dungeon-index>/minigames`.

## Precondition

At least one course is created. The tester is on the view of an area minigames list as described in the description above.

## Postcondition

A game of a minigame was changed.

## Typical procedure

1. Click on a dropwdown of a minigame to change the game
2. Select a specific game
3. A feedback toast message appears which contains that game was updated
4. The game is now displayed in the dropdown

## Alternative procedures

3.1 No toast message appears \
3.2 A toast message appears which contains that there was an error updating the game \
4.1 The dropdown does not update

## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)