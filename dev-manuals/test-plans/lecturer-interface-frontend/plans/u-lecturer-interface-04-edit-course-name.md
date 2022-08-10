# Lecturer-Interface: Edit course name (`u.lecturer-interface-4`)


Version: V1.0, 09.08.2022 \
Author: Max Kästner

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

4.1: Hit the cancel button: \
    4.1.1 A feedback toast message appears which contains that course name was not updated \
    4.1.2 The course name was not updated in the view and the input field disappears 
    
## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)