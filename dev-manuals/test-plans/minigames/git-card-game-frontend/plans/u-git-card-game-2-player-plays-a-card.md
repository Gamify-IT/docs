# Git Card Game start (`u.git-card-game-2`)

Version: V1.1, 11.08.2022, Created test plan \
Author: Ilijaz Mehmedovic
Tester: -

## Description

The player plays a card.

## Precondition

It's the players turn.

## Postcondition

The playe's score will change and the player's cards get removed by one.

## Typical procedure

1. The player selects a valid card and plays it
2. The card gets removed from the stack
3. The player receives the correct score to the card
4. The card gets add to the middle stack

## Alternative procedures

1.1. The played card is invalid
1.2. The player's turn ends
2.1. The stack is empty now
2.2. The player's turn ends

## Criticality

High

## Linkages

- [Player ends his turn (`u.git-card-game-3`)](u-git-card-game-3-player-ends-turn.md)
