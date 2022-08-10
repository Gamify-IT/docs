# Lecturer-Interface: Edit minigame configuration of chickenshock (`u.lecturer-interface-13`)


Version: V1.0, 09.08.2022 \
Author: Max Kästner

## Description

A `chickenshock` configuration can be customized to display custom questions and answers.

## Precondition

At least one course is created. The tester is on the view of an area minigames list as described in the description above.

## Postcondition

A configuration of the a chickenshock minigame was changed.

## Typical procedure

1. Click on a dropwdown of a minigame to change the game
2. Select `CHICKENSHOCK`
3. A feedback toast message appears which contains that game was updated
4. The game is now displayed in the dropdown
5. Click the edit button where the game was updated
6. A modal opens
7. Press add question button
8. The modal changes
9. Fill out the form:
    - Enter a question
    - Enter a correct answer
    - Enter a wrong answer
        - click add
    - Enter another answer
        - click add
10. Press the Ok button of the modal
11. The modal changes back
12. The entered question with correct answer and wrong answers is displayed in the modal
13. Press the Ok button of the modal
14. The modal closes
15. A success message appears

## Alternative procedures


## Criticality

High

## Linkages

- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
- [Switch to world view (`u.lecturer-interface-8`)](u-lecturer-interface-08-switch-to-world-view.md)
- [Show minigames of area (`u.lecturer-interface-11`)](u-lecturer-interface-11-show-minigames-of-area.md)