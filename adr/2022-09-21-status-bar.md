# Status Bar

We need to decide what to display in the status bar.

## Possible Solutions

1.  - The `level` part displays the furthest area the player has unlocked
		- e.g.: only world `1` unlocked: displays `1`
		- e.g.: unlocks world `1` dungeon `1`: displays `1-1`
		- e.g.: unlocks world `2`: displays `2`
	- The `progress bar` displays the progress to unlocking the next area
		- e.g.: `0/12` minigames completed: `0`% filled
		- e.g.: `6/12` minigames completed: `50`% filled

1.  - The `level` part displays the furthest area the player has unlocked
		- e.g.: only world `1` unlocked: displays `1`
		- e.g.: unlocks world `1` dungeon `1`: displays `2`
		- e.g.: unlocks world `2`(only one dungeon and world 1): displays `3`
	- The `progress bar` displays the progress to unlocking the next area
		- e.g.: `0/12` minigames completed: `0`% filled
		- e.g.: `6/12` minigames completed: `50`% filled

## Chosen Solution

1.

## Pro Chosen Solution

Easier for the user to understand what got unlocked.
