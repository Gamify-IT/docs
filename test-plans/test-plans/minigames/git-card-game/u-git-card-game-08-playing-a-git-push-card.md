# Git Card Game: Playing a 'git push' card (`u.git-card-game-08`)

Version: V1.1, 12.08.2022, Improve format \
Author: Ilijaz Mehmedovic, Leon Hofmeister

## Description

The player plays a `git push` card.

## Precondition

It's the player's turn.
The player has a `git push` card in his stack.

## Postcondition

The `git push` card gets moved from the players stack to the middle stack.

## Typical procedure

1. The player selects the `git push` card
2. All commits are getting pushed
3. The player's score increases by 8 * the amount of commits
4. The `git push` card gets added to the middle stack
5. The `git push` card gets removed from the player's stack and the game continues

## Alternative procedures

5.1. The player has no cards left on his stack \
5.2. The player's turn ends

## Criticality

High

## Linkages

- [Playing a 'touch' card (`u.git-card-game-02`)](u-git-card-game-02-playing-a-touch-card.md)
- [Playing a 'rm' card (`u.git-card-game-03`)](u-git-card-game-03-playing-a-rm-card.md)
- [Playing a 'git add' card (`u.git-card-game-04`)](u-git-card-game-04-playing-a-git-add-card.md)
- [Playing a 'git reset' card (`u.git-card-game-05`)](u-git-card-game-05-playing-a-git-reset-card.md)
- [Playing a 'git add all' card (`u.git-card-game-06`)](u-git-card-game-06-playing-a-git-add-all-card.md)
- [Playing a 'git commit' card (`u.git-card-game-07`)](u-git-card-game-07-playing-a-git-commit-card.md)
- [Player ends his turn (`u.git-card-game-09`)](u-git-card-game-09-player-ends-turn.md)
