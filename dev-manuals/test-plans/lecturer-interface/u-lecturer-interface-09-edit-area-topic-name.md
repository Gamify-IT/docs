# Lecturer-Interface: Edit area topic name in world view (`u.lecturer-interface-09`)


Version: V1.0, 09.08.2022 \
Author: Max Kästner

## Description

The topic name of an area can be changed on the area view.

## Precondition

At least one course with a preconfigured area is created. The tester is on the view of that area.

## Postcondition

The topic name of an area was updated and is shown in the view.

## Typical procedure

1. Click on an edit topic name button of an area (select world/dungeon by static name)
2. An input field shows up
3. Change the topic name to a new topic name in the input field
4. Hit the submit button
5. A feedback toast message appears which contains that topic name was updated
6. The new topic name replaces the old topic name in the view and the input field disappears

## Alternative procedures

4.1: Hit the cancel button: \
    4.1.1 A feedback toast message appears which contains that topic name was not updated \
    4.1.2 The topic name did not update in the view and the input field disappears

## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)
