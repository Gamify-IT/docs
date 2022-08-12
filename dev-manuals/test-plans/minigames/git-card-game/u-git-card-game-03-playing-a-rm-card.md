# Git Card Game: Playing a 'rm' card (`u.git-card-game-03`)

Version: V1.1, 12.08.2022, Improve format \
Author: Ilijaz Mehmedovic, Leon Hofmeister

## Description

The player plays a `rm` card.

## Precondition

It's the player's turn.
The player has a `rm` card in his stack.

## Postcondition

## Typical procedure

1. The player selects the `rm` card
2. a new file got added with the name of the card
3. The player's score increases by 1
4. The `rm` card gets added to the middle stack
5. The `rm` card gets removed from the player's stack and the game continues

## Alternative procedures

2.1. There is no file with the same name as the filename on the card \
2.2. The player's turn ends \
5.1. The player has no cards left on his stack \
5.2. The player's turn ends

## Criticality

High

## Linkages

- [Playing a 'touch' card (`u.git-card-game-02`)](u-git-card-game-02-playing-a-touch-card.md)
- [Playing a 'git add' card (`u.git-card-game-04`)](u-git-card-game-04-playing-a-git-add-card.md)
- [Playing a 'git reset' card (`u.git-card-game-05`)](u-git-card-game-05-playing-a-git-reset-card.md)
- [Playing a 'git add all' card (`u.git-card-game-06`)](u-git-card-game-06-playing-a-git-add-all-card.md)
- [Playing a 'git commit' card (`u.git-card-game-07`)](u-git-card-game-07-playing-a-git-commit-card.md)
- [Playing a 'git push' card (`u.git-card-game-08`)](u-git-card-game-08-playing-a-git-push-card.md)
- [Player ends his turn (`u.git-card-game-09`)](u-git-card-game-09-player-ends-turn.md)
