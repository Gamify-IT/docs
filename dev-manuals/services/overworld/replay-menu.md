# Replay Menu Developer Guide

## Scripts
You will find the relevant C#-scripts under the following directory in the overworld folder `\Assets\Scripts\HUD\Minigame Replay UI`.
The structure should look like this:
```
<Minigame Replay UI>
|_ ReplayItemManager       # Handles the logic for the minigame items (prefabs) in the list
|_ ReplayMenu              # Most improtantly, it is responsible for the population of the list
|_ ReplaySpotInteraction   # Handles the interaction between the player and the arcade game machine
```
## Objects
You will find the replay item prefab under the following directory in the overworld folder `\Assets\Prefabs\Minigame Replay Menu`. 
Unity uses this prefab to create a minigame item for a completed game, that will be added to the minigames list in the Replay Menu.

The used sprites for the designs can be found under the following directory in the overworld folder `\Assets\Sprites\ReplayMenu`.

## Unity Editor
Inside the unity project editor you can find the relevant objects in the hierarchy of the World 1 scene(`\Assets\Scenes\Worlds\World 1`).
The two objects in question are the sprite, "Arcade Game Machine", and the UI canvas "Replay Menu", which has the "Menu Window" as a child.

