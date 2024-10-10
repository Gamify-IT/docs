# Regex Game: Validating valid quizzes works (`u.regex-game-4`)

Version: V1.1, 09.08.2022, Improve format and remove copy paste errors \
Author: Leon Layer, Leon Hofmeister

## Description

When a new quiz is added, it is validated before being displayed,
i.e. because the regexes don't compile or because there is no correct answer. \
A valid quiz doesn't produce errors.

## Precondition

-

## Postcondition

No error is logged, the game starts as intended.

## Typical procedure

1. the tester opens the file `data.ts` and inserts a new correct quiz
2. There is no error message in the browser console
3. The game works as intended

## Alternative procedures

-

## Criticality

Medium

## Linkages

- [Validating invalid quizzes works (`u.regex-game-5`)](u-regex-game-5-validating-invalid-quizzes-works.md)

