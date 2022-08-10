# Lecturer-Interface edit course semester (`u.lecturer-interface-6`)


Version: V1.0, 09.08.2022
Author: Max Kästner
Tester: -

## Description

The semester of a specific course can be changed on its view.

## Precondition

At least one course is created. The tester is on the view of the course (`/courses/<course-id>`)

## Postcondition

The semester of the course was changed to the new entered semester.

## Typical procedure

1. Click the edit semester button
2. A input field shows up
3. Change the semester to a new semester in the input field (format `WS-20` or `SS-20`)
4. Hit the submit button
5. A feedback toast message appears which contains that semester was updated
6. The new semester replaces the old semester in the view and the input field disappears

## Alternative procedures

3.1: The semester is not in the right format: \
    3.1.1 Hit the submit button
    3.1.2 A feedback toast message appears which contains that semester was not updated \
    3.1.3 The semester did not change in the view and the input field disappears

4.1: Hit the cancel button: \
    5.1.1 A feedback toast message appears which contains that course description was not updated \
    4.1.2 The course description was not updated in the view and the input field disappears 

## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)