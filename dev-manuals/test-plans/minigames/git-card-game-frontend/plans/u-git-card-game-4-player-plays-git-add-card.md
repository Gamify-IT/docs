# Git Card Game start (`u.git-card-game-2`)

Version: V1.1, 11.08.2022, Created test plan \
Author: Ilijaz Mehmedovic
Tester: -

## Description

The player plays a `git add` card.

## Precondition

It's the player's turn.
The player has a `git add` card in his stack.

## Postcondition

## Typical procedure

1. The player selects the `git add` card
2. The file with the name on the card gets staged.
3. The player's score will increase with 4.
4. The `git add` card gets add to the middle stack.
5. The `git add` card gets removed from the player's stack and the game continues

## Alternative procedures

2.1. There are no changes on the file with the file name on the card to stage \
2.2. The player's turn ends \
5.1. The player has no cards left on his stack \
5.2. The player's turn ends

## Criticality

High

## Linkages

- [Player plays touch card (`u.git-card-game-2`)](u-git-card-game-2-player-plays-touch-card.md)
- [Player plays rm card (`u.git-card-game-3`)](u-git-card-game-3-player-plays-rm-card.md)
- [Player plays git reset card (`u.git-card-game-5`)](u-git-card-game-5-player-plays-git-reset-card.md)
- [Player plays git add all card (`u.git-card-game-6`)](u-git-card-game-6-player-plays-git-add-all-card.md)
- [Player plays git commit card (`u.git-card-game-7`)](u-git-card-game-7-player-plays-git-commit-card.md)
- [Player plays git push card (`u.git-card-game-8`)](u-git-card-game-8-player-plays-git-push-card.md)
- [Player ends his turn (`u.git-card-game-9`)](u-git-card-game-9-player-ends-turn.md)
