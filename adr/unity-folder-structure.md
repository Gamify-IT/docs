# Unity Folder Structure and Filenames

Currently, the File and Folder structure in our unity projects is inconsistent.
There are Scripts in Scenes Folders, Scenes in no folder at all,... Additionally, the Filenames do not follow a common naming scheme.

## Possible Solutions

- Change nothing
- Only put files in the correct folders, which are correctly named.
  - for example put all World Scenes into the worlds folder
  - Scripts only in the scripts folder, with subfolders which are named to display where the script belongs to
    - also applies to all other stuff like prefabs, scenes, sprites, tiles, animations, ...
  - no longer needed scenes/scripts/etc. should be moved to "old" folder in the respective parent Folder.
    - or deleted?

### Proposed folder structure:  

- Assets
  - Animations
    - Foldername
      - animation files
  - Prefabs
    - Foldername
      - prefab files
  - Resources
    - Foldername
      - resource files (render textures, masks, everything that doesnt fit in the other folders)
  - Scenes
    - Dungeons
      - Dungeon 1
        - Dungeon 1 scenes
      - Dungeon 2
        - Dungeon 2 scenes
      - ...
    - Worlds
      - World 1
        - World 1 scenes
      - World 2
        - World 2 scenes
      - ...
    - Foldername
      - scenes
    - ...
  - Scripts
    - Foldername
      - script files
    - ...  
  - Sprites
    - Foldername
      - sprite files
    - ...
  - Tiles (Folder for every different Tileset, if new tileset created -> create new folder)
    - Cave
      - Cave tilesets and tilemaps (and all assets that generate out of it)
    - Overworld
      - animated
        - fountain
          - animated tiles
        - ...  
      - Overworld tilesets and tilemaps (and all assets that generate out of it)
    - ...

## Pro changing nothing

- no extra work at the moment

## Pro consistent structure

- much more straightforward
- easier to find files

## Chosen Solution

## Pro Chosen Solution

## Contra Chosen Solution
