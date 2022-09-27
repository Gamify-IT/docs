# Lecturer-Interface: Edit book configuration (`u.lecturer-interface-15`)


Version: V1.0, 24.09.2022 \
Author: Max Kästner

## Description

The configuration of an book can be edited.

## Precondition

At least one course is created. The tester is on the view where the books of an area are listed.

## Postcondition

The configuration of a selected book was updated.

## Typical procedure

1. Click the edit button of a book
2. A modal opens with a textarea
3. Enter a little text
4. Press the `Ok` button
5. The modal closes
6. A success message appears
7. Press the edit button from the book again and ensure that the configuration is what you saved above.

## Alternative procedures

4.1: Press the Cancel button of the modal: \
    4.1.1 The modal closes \
    4.1.2 Press the edit button from the book again and ensure that the configuration has not changed.


## Criticality

Medium

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)
- [Show books of area (`u.lecturer-interface-29`)](u-lecturer-interface-29-show-books-of-area.md)