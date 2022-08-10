# Lecturer-Interface edit npc configuration (`u.lecturer-interface-15`)


Version: V1.0, 10.08.2022 \
Author: Max Kästner

## Description

The configuration of a npc can be edited in a modal. For npcs of a world the path is `/courses/<course-id>/worlds/<world-index>/npcs` and for a dungeon `/courses/<course-id>/worlds/<world-index>/dungeons/<dungeon-index>/npcs`.

## Precondition

At least one course is created. The tester is on the view of an area npcs list as described in the description above.

## Postcondition

The configuration of a selected npc was updated.

## Typical procedure

1. Click the edit button of a npc
2. A modal opens
3. Press the `Add Input` button
4. A new text field appears
5. Enter a little sentence a npc could say
6. Press the Ok button of the modal
7. The modal closes
8. A feedback toast message appears which contains that configuraiton was saved
9. Press the edit button from the npc again and make sure the configurations are the same as you saved it before.

## Alternative procedures

6.1: Press the Cancel button of the modal: \
    6.1.1 The modal closes \
    6.1.2 Press the edit button from the npc again and make sure the configurations that you changed before cancelling were not applied.


## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)
- [Show npcs of area (`u.lecturer-interface-14`)](u-lecturer-interface-14-show-npcs-of-area.md)