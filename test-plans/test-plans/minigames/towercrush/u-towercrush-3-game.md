
# Towercrush: play the game (`u-towercrush-3`)

Version: V1.0, 2023.01.11 \
Author: Martin Lautenschlager, Levi Otterbach

## Description

This use case verifies that the game works as intendet.

## Precondition

Make sure a game configuration is set in the DB with postman.
Enter the configuration UUID at the end of the URL in your browser for all 3 Players.
3 Players have connected in the same lobby, 1 and 2 joined team a, 3 joined team b.

## Postcondition

- 

## Typical procedure

1. Player 1 pressed on any of possible answeres.
2. PLayer 1 and 2 see the name of player one below the answer he entered.
3. Player 3 does NOT see the name of player 1.
4. Player 1 presses `Next Question`.
5. PLayer 1 and 2 see the next question displayed.
6. Player 3 does NOT see the next question displayed.

## Alternative procedures

X.1 Press `leave lobby` at any time to return to the start screen.

## Criticality

High

## Linkages

-
