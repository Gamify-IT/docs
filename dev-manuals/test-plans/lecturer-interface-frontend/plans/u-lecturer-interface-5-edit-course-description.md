# Lecturer-Interface edit course description (`u.lecturer-interface-5`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The description of a specific course can be changed on its view.

## Precondition

At least one course is created. The tester is on the view of the course (`/courses/<course-id>`)

## Postcondition

The description of the course was changed to the new entered description.

## Typical procedure

1. Click the edit description button
2. A input field shows up
3. Change the course description to a new description in the input field
4. Hit the submit button
5. A feedback toast message appears which contains that course description was updated
6. The new course description replaces the old course description in the view and the input field disappears

## Alternative procedures

2.1 Nothing changes \
5.1 No toast message appears \
5.2 A toast message appears which contains that there was an error updating the description \
6.1 The old course description is displayed

## Criticality

Low

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-3-show-specific-course.md)