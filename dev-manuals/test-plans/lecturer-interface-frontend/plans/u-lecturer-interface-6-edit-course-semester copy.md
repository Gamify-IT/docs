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

2.1 Nothing changes \
5.1 No toast message appears \
5.2 A toast message appears which contains that there was an error updating the semester \
6.1 The old course semester is displayed

## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-3-show-specific-course.md)