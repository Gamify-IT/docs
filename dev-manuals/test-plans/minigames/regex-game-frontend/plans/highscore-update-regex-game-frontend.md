# Highscore update test 

Number: Unique and unambiguous identifier according to the following
pattern:
U.XX(service identifier).X (sequential number, start
at 1).  
Version: Version of the use case according to pattern.
Vx.x, date of creation, description of change  
Author: Author of the use case description  
Tester: Use case tester

## Description

Tests if the high score increases correctly when a higher score is reached.

## Precondition

The game is in a state where the maximum possible higscore has not yet been reached.

## Postcondition

by playing, the current higscore will be exceeded and the higscore will be updated in the menu. 

## Typical procedure

the player plays the game but does not yet reach the maximum higscoore. the player sees his previous higscore in the menu. by trying again, he surpasses his previous best performance, which should update his higscore in the meu.

## Alternative procedures

The game is started. The player sees his previous higscore in the menu (0). by attempting at least one correct answer, his higscore is updated in the meu.

## Criticality

Low

## Linkages

Relationships to other use cases.
References by use case number.
