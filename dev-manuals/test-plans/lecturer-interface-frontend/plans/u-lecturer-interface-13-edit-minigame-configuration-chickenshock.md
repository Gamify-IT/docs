# Lecturer-Interface: Edit minigame configuration of chickenshock (`u.lecturer-interface-13`)


Version: V1.0, 09.08.2022 \
Author: Max Kästner

## Description

A `chickenshock` configuration can be customized to display custom questions and answers.

## Precondition

At least one course with a `CHICKENSHOCK` minigame is created. The tester is located where the `chickenshock` instance can be configured.

## Postcondition

The configuration of the `chickenshock` instance was changed.

## Typical procedure

1. Click the edit button of a `chickenshock` minigame
2. A modal opens
3. Press add question button
4. The modal changes
5. Fill out the form, including the question, the correct answer, and two wrong answers
6. Press the Ok button of the modal
7. The modal changes back
8. The entered question with correct answer and wrong answers is displayed in the modal
9. Press the Ok button of the modal
10. The modal closes
11. A success message appears

## Alternative procedures

6.1: Hit the cancel button of the modal: \
    6.1.1 The modal changes back \
    6.1.2 No new question was added
    6.1.3 Continue with step `9`

9.1: Hit the cancel button of the modal: \
    9.1.1 The modal closes \
    9.1.2 The changes to the configuration does not get saved

## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)
- [Show minigames of area (`u.lecturer-interface-11`)](u-lecturer-interface-11-show-minigames-of-area.md)