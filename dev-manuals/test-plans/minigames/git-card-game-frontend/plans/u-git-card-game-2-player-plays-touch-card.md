# Git Card Game start (`u.git-card-game-2`)

Version: V1.1, 11.08.2022, Created test plan \
Author: Ilijaz Mehmedovic
Tester: -

## Description

The player plays a `touch` card.

A `nano` card is also considered a `touch` card.

## Precondition

It's the player's turn.
The player has a `touch` card in his stack.

## Postcondition

A new file got added with the name on the card.
The player's score will increase with 1.
The `touch` card gets moved from the players stack to the middle stack.

## Typical procedure

1. The player selects the `touch` card
2. A new file got added with the name of the card
3. The player's score will increase with 1.
4. The `touch` card gets add to the middle stack.
5. The `touch` card gets removed from the player's stack and the game continues

## Alternative procedures

5.1. The player has no cards left on his stack
5.2. The player's turn ends

## Criticality

High

## Linkages

- [Player plays rm card (`u.git-card-game-3`)](u-git-card-game-3-player-plays-rm-card.md)
- [Player plays git add card (`u.git-card-game-4`)](u-git-card-game-4-player-plays-git-add-card.md)
- [Player plays git reset card (`u.git-card-game-5`)](u-git-card-game-5-player-plays-git-reset-card.md)
- [Player plays git add all card (`u.git-card-game-6`)](u-git-card-game-6-player-plays-git-add-all-card.md)
- [Player plays git commit card (`u.git-card-game-7`)](u-git-card-game-7-player-plays-git-commit-card.md)
- [Player plays git push card (`u.git-card-game-8`)](u-git-card-game-8-player-plays-git-push-card.md)
- [Player ends his turn (`u.git-card-game-9`)](u-git-card-game-9-player-ends-turn.md)
