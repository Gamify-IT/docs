# Lecturer-Interface: Edit NPC configuration (`u.lecturer-interface-15`)


Version: V1.0, 10.08.2022 \
Author: Max Kästner

## Description

The configuration of an NPC can be edited.

## Precondition

At least one course is created. The tester is on the view of an area NPCs list as described in the description above.

## Postcondition

The configuration of a selected NPC was updated.

## Typical procedure

1. Click the edit button of a NPC
2. A modal opens
3. Press the `Add Input` button
4. A new text field appears
5. Enter a little sentence a NPC could say
6. Press the Ok button of the modal
7. The modal closes
8. A feedback toast message appears which contains that configuraiton was saved
9. Press the edit button from the NPC again and ensure that the configuration is what you saved above.

## Alternative procedures

6.1: Press the Cancel button of the modal: \
    6.1.1 The modal closes \
    6.1.2 Press the edit button from the NPC again and ensure that the configuration has not changed.


## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)
- [Show npcs of area (`u.lecturer-interface-14`)](u-lecturer-interface-14-show-npcs-of-area.md)