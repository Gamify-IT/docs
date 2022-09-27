# Add and set up minigames

## Overview

Minigame spots are used to start a minigame. If the player enters the specified area, the spot activates and displays information about the minigame, the players previous success as a highscore and allows the player to start a minigame play round.

## How to add a minigame

To add a new minigame to an area, do the following:

1. Open the scene, in which the minigame should be
2. Create a new `game object` as a child of the `Minigames` game object on the hierarchy  
![Hierarchy view](assets/minigame-hierarchy-view.webp)
3. Add the `Minigame` script, a `Box Collider 2D` component, a `Sprite Renderer` component and a `Animator` component to the created game object
![Inspector view](assets/minigame-inspector-view.webp)
4. Place the object where the minigame should be (via the `x` and `y` coordinates)
5. Adjust the trigger area of the `Box Collider 2D` component using the `Edit collider` button (default width and height is `1.5`)  
![Collider component](assets/minigame-collider-component.webp)
6. Set the `Is Trigger` flag at the `Box Collider 2D` component  
![Trigger flag](assets/minigame-trigger-flag.webp)

## How to set up a minigame

Provide the required data for the minigame at the `Minigame` component  
![Script component](assets/minigame-script-component.webp)

1. `World`: The index of the world the minigame is in  
2. `Dungeon`: The index of the dungeon the minigame is in, `0` if it is in a world
3. `Number`: The index of the minigame in its area (a consecutive number starting from `1`)

You also need to set up the `Animator` component. To do that, select the `Minigame` controller located at `Assets/Animations/MinigameSpot` as the `Controller` attribute.  
![Animator component](assets/minigame-animator-component.webp)  
![Animator selection](assets/minigame-animator-selection.webp)

## Prefab

You can also speed up that process by using the provided prefab, located at `Assets/Prefabs/Minigames`.  
![Prefab](assets/minigame-prefab.webp)  
Simply drag an drop the `Minigame` object into the scene hierarchy as a child of the `Minigames` game object.
You can then skip steps `2`, `3`, `5` and `6` as well as setting up the `Animator` component.

## Lecturer Interface

Once you have added all minigames you want to add, do not forget to update the maps for the lecturer interface by pushing a new commit changing the specific image in <https://github.com/Gamify-IT/docs/tree/main/user-manuals/maps>.  
You should also update the line `mapCommitHash: …` in the [lecturer interface config file](https://github.com/Gamify-IT/lecturer-interface/blob/main/src/config.ts) with the new SHA.

## Disclaimer

You can only add minigames to an area when you have less than `maxMinigames` (script `GameSettings` located at `Assets/Scripts/GameManager`) in this area.  
![Prefabs](assets/minigame-game-settings.webp)
Everything above will not be configurable from the backend.
