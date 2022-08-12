# Git Card Game: Playing a 'git reset' card (`u.git-card-game-05`)

Version: V1.1, 12.08.2022, Improve format \
Author: Ilijaz Mehmedovic, Leon Hofmeister

## Description

The player plays a `git reset` card.

## Precondition

It's the player's turn.
The player has a `git reset` card in his stack.

## Postcondition

## Typical procedure

1. The player selects the `git reset` card
2. The staged file with the name on the card gets unstaged
3. The player's score increases by 4
4. The `git reset` card gets added to the middle stack
5. The `git reset` card gets removed from the player's stack and the game continues

## Alternative procedures

2.1. The file with the file name on the card is not staged \
2.2. The player's turn ends \
5.1. The player has no cards left on his stack \
5.2. The player's turn ends

## Criticality

High

## Linkages

- [Playing a 'touch' card (`u.git-card-game-02`)](u-git-card-game-02-playing-a-touch-card.md)
- [Playing a 'rm' card (`u.git-card-game-03`)](u-git-card-game-03-playing-a-rm-card.md)
- [Playing a 'git add' card (`u.git-card-game-04`)](u-git-card-game-04-playing-a-git-add-card.md)
- [Playing a 'git add all' card (`u.git-card-game-06`)](u-git-card-game-06-playing-a-git-add-all-card.md)
- [Playing a 'git commit' card (`u.git-card-game-07`)](u-git-card-game-07-playing-a-git-commit-card.md)
- [Playing a 'git push' card (`u.git-card-game-08`)](u-git-card-game-08-playing-a-git-push-card.md)
- [Player ends his turn (`u.git-card-game-09`)](u-git-card-game-09-player-ends-turn.md)
