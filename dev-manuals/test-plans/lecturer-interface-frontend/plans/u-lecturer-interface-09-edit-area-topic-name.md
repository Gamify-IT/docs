# Lecturer-Interface edit area topic name in world view (`u.lecturer-interface-9`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The topic name of a world or dungeon (which is linked to the world of a view) can be changed on the world view.

## Precondition

At least one course is created. The tester is on the view of a world of a course (`/courses/<course-id>/worlds/<world-index>`)

## Postcondition

The topic name of an area was updated and is shown in the view.

## Typical procedure

1. Click on an edit topic name button of an area (select world/dungeon by static name)
2. A input field shows up
3. Change the topic name to a new topic name in the input field
4. Hit the submit button
5. A feedback toast message appears which contains that topic name was updated
6. The new topic name replaces the old topic name in the view and the input field disappears

## Alternative procedures

2.1 Nothing changes \
5.1 No toast message appears \
5.2 A toast message appears which contains that there was an error updating the topic name \
6.1 The old topic name is displayed

## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)