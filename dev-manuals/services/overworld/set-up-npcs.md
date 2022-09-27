# Add and set up NPCs

## Overview

NPCs are used to impart knowledge to the player.  
The lecturer can set dialogues and texts to help the player to complete minigames.  
A player can talk to an NPC as often as he likes to.

## How to add a NPC

To add a new NPC to an area, do the following:

1. Open the scene, in which the NPC should be
2. Create a new `game object` as a child of the `NPCs` game object on the hierarchy  
![Hierarchy view](assets/npc-hierarchy-view.webp)
3. Add the `NPC` script, a `Box Collider 2D` component, a `Sprite Renderer` component and a `Capsule Collider 2D` component to the created game object
![Inspector view](assets/npc-inspector-view.webp)
4. Place the object where the NPC should be (via the `x` and `y` coordinates)
5. Adjust the trigger area of the `Box Collider 2D` component using the `Edit Collider` button (this sets the area the player can talk to the NPC)
6. Adjust the trigger area of the `Capsule Collider 2D` component using the `Edit Collider` button (this sets the collider of the NPC)  
![Collider component](assets/npc-collider-component.webp)
7. Set the `Is Trigger` flag at the `Box Collider 2D` component  
![Trigger flag](assets/npc-trigger-flag.webp)

## How to set up a NPC

Provide the required data for the NPC at the `NPC` component  
![Script component](assets/npc-script-component.webp)

1. `World`: The index of the world the NPC is in  
2. `Dungeon`: The index of the dungeon the NPC is in, `0` if it is in a world
3. `Number`: The index of the NPC in its area (a consecutive number starting from `1`)
4. `Image Of NPC`: The image shown in the dialogue box
5. `Name Of NPC`: The name of the NPC

You also need to set up the `Sprite Renderer` component.

1. Select a sprite as the visible appearance of NPC as the `Sprite` attribute.  
![Animator component](assets/npc-sprite-renderer-component.webp)  
![Animator selection](assets/npc-sprite-renderer-selection.webp)  
2. Select in the `Sorting Layer` drop-down menu `BackGround`
3. The `Order In Layer` attribute has to be `4`

## Prefab

You can also speed up that process by using the provided prefab, located at `Assets/Prefabs/Interactable`.  
![Prefab](assets/npc-prefab.webp)  
Simply drag an drop the `NPC` object into the scene hierarchy as a child of the `NPCs` game object.
You can then skip steps `2`, `3`, `5`, `6` and `7`.

### Lecturer Interface

Once you have added all NPCs you want to add, do not forget to update the maps for the lecturer interface by pushing a new commit changing the specific image in <https://github.com/Gamify-IT/docs/tree/main/user-manuals/maps>.  
You should also update the line `mapCommitHash: …` in the [lecturer interface config file](https://github.com/Gamify-IT/lecturer-interface/blob/main/src/config.ts) with the new SHA.

## Disclaimer

You can only add NPCs to an area when you have less than `maxNPCs` (script `GameSettings` located at `Assets/Scripts/GameManager`) in this area.  
![Prefabs](assets/npc-game-settings.webp)
Everything above will not be configurable from the backend.
