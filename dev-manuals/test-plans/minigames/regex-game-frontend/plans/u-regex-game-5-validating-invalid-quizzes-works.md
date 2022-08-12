# Regex Game: Validating invalid quizzes works (`u.regex-game-5`)

Version: V1.1, 09.08.2022, Improve format and remove copy paste errors \
Author: Leon Layer, Leon Hofmeister

## Description

When a new quiz is added, it is validated before being displayed,
i.e. because the regexes don't compile or because there is no correct answer. \
An invalid quiz logs an error on the browser console.

## Precondition

-

## Postcondition

An error is logged in the console.

## Typical procedure

1. Open the file `data.ts` and insert a new incorrect quiz whose regex doesn't compile as well as one quiz that has no correct answer
2. Start the game
3. There is at least one error message in the browser console
4. The game works as intended

## Alternative procedures

4.1. The game redirects to the end screen \
4.2. The game notifies the user that the quizzes are invalid \
4.3. Unparseable quizzes are skipped

## Criticality

Medium

## Linkages

- [Validating valid quizzes works (`u.regex-game-4`)](u-regex-game-4-validating-valid-quizzes-works.md)

