# Regex Game: Only update highscore when `score > highscore` (`u.regex-game-3`)

Version: V1.1, 09.08.2022, Improve format, merge with `score <= highscore does not update highscore` test \
Author: Leon Layer, Leon Hofmeister

## Description

Tests that the highscore doesn't change when `score <= highscore`.

## Precondition

The highscore is `>= 2`. The game has at least three regexes. The current score is `0`.

## Postcondition

The highscore has value `3`.

## Typical procedure

1. Select a correct answer
2. The current score changes to `1`
3. The high score does not change
4. Select a correct answer
5. The current score changes to `2`
6. The high score does not change
7. Select a correct answer
8. The current score changes to `3`
9. The high score changes to `3`
10. Answer all further questions incorrectly
11. The backend (if present) gets updated with the game results including all correctly answered regexes, all incorrectly answered regexes, and the current score as well as the high score

## Alternative procedures

2.1. We don't increase by factor `1` - multiply all numbers in this test by this factor \
10.1. Wrong answers give a penalty instead of no reward - answer the questions correctly, and update the highscore accordingly \
11.1. No backend present - No-op

## Criticality

Low

## Linkages

