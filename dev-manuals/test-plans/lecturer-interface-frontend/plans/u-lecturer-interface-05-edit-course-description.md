# Lecturer-Interface: Edit course description (`u.lecturer-interface-05`)


Version: V1.0, 09.08.2022 \
Author: Max Kästner

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

4.1: Hit the cancel button: \
    4.1.1 A feedback toast message appears which contains that course description was not updated \
    4.1.2 The course description was not updated in the view and the input field disappears 

## Criticality

Low

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
