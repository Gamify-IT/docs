# Set up the minimap and add minimap icons

## Overview

The minimap helps the player to orientate in areas, and highlights important things such as NPCs, dungeon entry points, or connections between worlds.

## How to set up the minimap

For the minimap to work correctly in an area, you need to set up the following parts:

1. The [minimap area name](#how-to-set-up-the-minimap-area-name)
2. The [minimap icons parent object](#how-to-set-up-the-minimap-icons-parent-object)
3. The [minimap icons](#how-to-add-minimap-icons)

## How to set up the minimap area name

1. Open the scene, for which you want to set up the minimap area name
2. Create a new `game object` on the hierarchy  
![Hierarchy view](assets/minimap-name-hierarchy-view.webp)
3. Add the `Minimap Area Name` script and a `Box Collider 2D` component to the created game object  
![Inspector view](assets/minimap-name-inspector-view.webp)
4. Adjust the trigger area of one `Box Collider 2D` component using the `Edit collider` button in such a way that it covers the entire area  
![Collider component](assets/minimap-name-collider-component.webp)  
![Example Image](assets/minimap-name-example-image.webp)
5. Set the `Is Trigger` flag at the `Box Collider 2D` component  
![Trigger flag](assets/minimap-name-trigger-flag.webp)
6. Set up the `Minimap Area Name` component by adding the name of the area as the `Area Name` attribute  
![Script component](assets/minimap-name-script-component.webp)

## How to set up the minimap icons parent object

1. Open the scene, for which you want to set up minimap icons
2. Create a new `game object` called `MinimapIcons` on the hierarchy
3. Set the `Tag` attribute in the `Inspector` to `MinimapIconsParent`  
![Inspector view](assets/minimap-icon-parent-inspector-view.webp)

If the area is a world, you also need to do the following:

1. Create a new `game object` as a child of the `MinimapIcons` game object on the hierarchy  
![Hierarchy view](assets/minimap-icon-unload-hierarchy-view.webp)
2. Add the `Minimap Icons Unloading` script and a `Box Collider 2D` component to the created game object  
![Inspector view](assets/minimap-icon-unload-inspector-view.webp)
3. Adjust the trigger area of one `Box Collider 2D` component using the `Edit collider` button in such a way that it covers the entire playable area area of the world  
![Collider component](assets/minimap-icon-unload-collider-component.webp)  
![Example Image](assets/minimap-icon-unload-example-image.webp)
4. Set the `Is Trigger` flag at the `Box Collider 2D` component  
![Trigger flag](assets/minimap-icon-unload-trigger-flag.webp)
5. Set up the `Minimap Icons Unloading` component by adding the area name as the `Name Of Current Scene` attribute  
![Script component](assets/minimap-icon-unload-script-component.webp)

## How to add minimap icons

You can add as many minimap icons as you want. Simply do the following:

1. Create a new `game object` as a child of the `MinimapIcons` game object on the hierarchy  
![Hierarchy view](assets/minimap-icon-hierarchy-view.webp)
2. Add the `Minimap Icons Unloading` script, a `Box Collider 2D` component and a `Sprite Renderer` component to the created game object
3. Set the `Tag` attribute in the `Inspector` to `MinimapIcon`
4. Set the `Layer` attribute in the `Inspector` to `Minimap`  
![Inspector view](assets/minimap-icon-inspector-view.webp)
5. Adjust the trigger area of one `Box Collider 2D` component using the `Edit collider` button to cover the area of the minimap icon  
![Collider component](assets/minimap-icon-collider-component.webp)
6. Set the `Is Trigger` flag at the `Box Collider 2D` component  
![Trigger flag](assets/minimap-icon-trigger-flag.webp)
7. Set up the `Minimap Icons Unloading` component by leaving the `Name Of Current Scene` attribute blanc  
![Script component](assets/minimap-icon-script-component.webp)

You also need to set up the `Sprite Renderer` component.

1. Select a sprite as the icon you want as the `Sprite` attribute.  
![Sprite renderer component](assets/minimap-icon-sprite-renderer-component.webp)  
2. Select in the `Sorting Layer` drop-down menu `MinimapIcons`
3. The `Order In Layer` attribute has to be `0`

If you don't want the minimap icon to be removed once you walked by it, for example because it shows the position of a NPC and therefor should always be active, you have to remove the `Box Collider 2D` component.
