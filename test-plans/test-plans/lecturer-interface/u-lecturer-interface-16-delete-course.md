# Lecturer-Interface: Delete course (`u.lecturer-interface-16`)


Version: V1.0, 16.08.2022 \
Author: Max Kästner

## Description

A specific course can be deleted.

## Precondition

At least one course is created. The tester is on the view of the course (`/courses/<course-id>`).

## Postcondition

The course is deleted.

## Typical procedure

1. Press the delete course button
2. A confirmation modal opens
3. Hit the Ok button
4. A feedback toast message appears which contains that course was deleted
5. You get redirected to the courses list page

## Alternative procedures

3.1: Hit the cancel button: \
    3.1.1 The modal closes

## Criticality

Medium

## Linkages

- [Show courses (`u.lecturer-interface-1`)](u-lecturer-interface-01-show-courses.md)
- [Create course (`u.lecturer-interface-2`)](u-lecturer-interface-02-create-course.md)
- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)