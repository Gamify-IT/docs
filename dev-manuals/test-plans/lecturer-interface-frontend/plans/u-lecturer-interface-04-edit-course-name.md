# Lecturer-Interface edit course name (`u.lecturer-interface-4`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The name of a specific course can be changed on its view.

## Precondition

At least one course is created. The tester is on the view of the course (`/courses/<course-id>`)

## Postcondition

The name of the course was changed to the new entered name.

## Typical procedure

1. Click the edit name button
2. A input field shows up
3. Change the course name to a new name in the input field
4. Hit the submit button
5. A feedback toast message appears which contains that course name was updated
6. The new course name replaces the old course name in the view and the input field disappears

## Alternative procedures

2.1 Nothing changes \
5.1 No toast message appears \
5.2 A toast message appears which contains that there was an error updating the name \
6.1 The old course name is displayed

## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)