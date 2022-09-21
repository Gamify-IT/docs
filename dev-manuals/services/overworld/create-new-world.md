# How to create a new World

This tutorial is for people interested in creating their own World/Dungeon the way we created one. This tutorial will be about creating a new world, but creating a dungeon works equally.

## Tileset

Before starting to paint a world you need to think about in which theme the world should be. We used the [Zelda-like Tileset](https://opengameart.org/content/zelda-like-tilesets-and-sprites) for all our Worlds and made some modifications to it according to our own needs (Including a few custom sprites). See [new tilesets](https://github.com/Gamify-IT/overworld/blob/main/new-tilesets/README.md) for some info about how to change the look of the Tileset. This tutorial works with the standard Zelda-like Tileset since it is already available in the project. If you need another tileset you can refer to [setup tilemap in unity](https://github.com/Gamify-IT/docs/blob/main/dev-manuals/languages/unity/setup-tilemap-in-unity.md).

## Copying the Boilerplate Scene

Worlds are created in separate scenes. There is an empty Boilerplate scene which can be used to draw new worlds. It already has the grid and needed layers.

1. Copy the Boilerplate scene that is located in the folder `Assets/Scenes/Boilerplate`
![Folder Structure](assets/boilerplate.webp)
2. Create a new Folder in the `Assets/Scenes/Worlds` Folder and name it for example `World 5`.
3. Paste the copied boilerplate scene into the newly created folder and rename the scene to for example `World 5`

## Layer Information

When painting a World there are multiple layers that can be painted on. It is necessary to paint on the correct layer for everything to work correctly.  
![Layers](assets/layers.webp)

## Start painting the World
