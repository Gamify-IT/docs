# Lecturer-Interface: Edit minigame description (`u.lecturer-interface-20`)


Version: V1.0, 29.08.2022 \
Author: Max Kästner

## Description

The description of a specific minigame can be changed on its view.

## Precondition

At least one course is created. The tester is located where the minigames of an area are listed.

## Postcondition

The description of the minigame was changed to the new entered description.

## Typical procedure

1. Click the edit description button of a minigame
2. A input field shows up
3. Change the minigame description to a new description in the input field
4. Hit the submit button
5. A feedback toast message appears which contains that the minigame description was updated
6. The new minigame description replaces the old minigame description in the view and the input field disappears

## Alternative procedures

4.1: Hit the cancel button: \
    4.1.1 A feedback toast message appears which contains that minigame description was not updated \
    4.1.2 The minigame description was not updated in the view and the input field disappears 

## Criticality

Low

## Linkages

- [Show minigames of area (`u.lecturer-interface-11`)](u-lecturer-interface-11-show-minigames-of-area.md)
