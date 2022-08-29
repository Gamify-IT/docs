# Lecturer-Interface: Edit NPC description (`u.lecturer-interface-21`)


Version: V1.0, 29.08.2022 \
Author: Max Kästner

## Description

The description of a specific npc can be changed on its view.

## Precondition

At least one course is created. The tester is located where the NPCs of an area are listed.

## Postcondition

The description of the NPC was changed to the new entered description.

## Typical procedure

1. Click the edit description button of a NPC
2. A input field shows up
3. Change the NPC description to a new description in the input field
4. Hit the submit button
5. A feedback toast message appears which contains that the NPC description was updated
6. The new NPC description replaces the old NPC description in the view and the input field disappears

## Alternative procedures

4.1: Hit the cancel button: \
    4.1.1 A feedback toast message appears which contains that NPC description was not updated \
    4.1.2 The NPC description was not updated in the view and the input field disappears 

## Criticality

Low

## Linkages

- [Show NPCs of area (`u.lecturer-interface-14`)](u-lecturer-interface-14-show-npcs-of-area.md)
