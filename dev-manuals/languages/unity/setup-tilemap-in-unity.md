# Setup Tilemap in Unity

## Get sprites from tilemap

Import your sprite into Unity. Then select it in the project explorer.

![select tileset](setup-unity-tilemap/select-tileset.png)

In the inspector set the following fields:

- Sprite Mode: `Multiple`
- Pixels Per Unity: the amount of pixels for each tile
- Filter Mode: `Point (no filter)`

Then select the sprite editor and apply.

![configure tileset](setup-unity-tilemap/configure-tileset.png)

In the sprite editor select `Slice` and set the type to `Grid by Cell Size`. Set the pixel size to the size of each tile and preview the tiling in the background. Finally press on `Slice` and in the sprite editor on `Apply`.

![tile in sprite editor](setup-unity-tilemap/tile-in-sprite-editor.png)

Now you can unfold the tilemap to preview all sprites.

![tiled sprites](setup-unity-tilemap/tiled-sprites.png)

## Create tilemap

### Install Tile Palette

Navigate to `Window`>`Package Manager`.

On the top right select `Packages: Unity Registry`

Now search for `Tilemap` and install `2D Tilemap Editor` and `2D Tilemap Extras`.

### Create Tile Palette

Navigate to `Window`>`2D`>`Tile Palette`.

You will have a new tileset window which you can move arround and dock to the unity editor.

There you need to press `Create new palette`. Give it a name, make sure you select a `Rectangle` grid and chose a target directory to store it.

![create new palette](setup-unity-tilemap/create-new-palette.png)

Next, select all sprites you want (e.g. all tiles sprites from a tilemap) and drag them over. Select a target directory where you want to store all tiles. This process can take a while. The result should look like this:

![tile palette](setup-unity-tilemap/tile-palette.png)

### Rotate or Flip sprites

On the Tile Palette toggle `Edit` and then use the cursor tool to select a tile. In the Inspector you can now rotate, move or split the tile by setting the scale to a negative value. Make sure to toggle the edit mode again when you finished.

## Draw unity scene

In the Hirarchy right click>`2D`>`Tilemap`>`Rectangular`.

Make sure the tilemap has to position `0,0,0` in the inspector. Create some more layers in the grid. By duplicating the just created `Tilemap` object.

Set the z position of the second layer to `-0.1`, the z position of the third layer to `-0.2`, etc.

![create layers](setup-unity-tilemap/create-layers.png)

Now you can select tiles from the tile palette and select the brush to draw. You also have a fill tool and a rectangle tool.

Make sure you draw your ground on the lowerst layer (layer 1). Go to the tile palette and set `Active Tilemap` to the first layer. Draw objects that should be drawn above layer 1 on layer 2. See results of using the layers:

![layers](setup-unity-tilemap/layers.png)

### Some tips

`Ctrl + Click or Drag` picks the current tile and you can now draw with that.
`Shift + Click` deletes the tile.
