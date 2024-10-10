# Unlocking System

We need a system on how to decide, which area is unlocked next.

## Possible Solutions

1.  - additional attribute "configured" for areas, default: false

    - adding a minigame: configured = true
    - removing a minigame: if only minigame: configured = false

	- unlocking new areas:
	    - world completed:
		    - next dungeon configured = true: unlock dungeon
		    - next dungeon configured = false: unlock next world
            - no next world exists: game done
		
	    - dungeon completed:
		    - next dungeon configured = true: unlock dungeon
		    - next dungeon configured = false: unlock next world
		    - no next dungeon exists: unlock next world
            - no next world exists: game done
		
    - at the start of the game: check, which areas need to be unlocked

## Chosen Solution

1

## Pro Chosen Solution

flexible and works with course changes by the lecturer

## Contra Chosen Solution

N/A