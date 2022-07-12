# Scene handling

Here it is documented how we currently handle multiple scenes in Unity.

## Requirements

To use our unity scenes with script code we need to add them to the Build Settings.  
![build settings](build-settings-scenes.png)  
Simply just drag and drop the required Scenes into the `Scenes in Build` area.
Every Scene that needs to be in the Final Version, has to be there.

## First Scene

We need to have a starting Scene from which every other Scene is accessible in some way. Currently we have a dummy scene called `FirstScene` which has a Script attached to it. If you load the `FirstScene` it executes a Script `LoadFirstScene.cs` that is attached to it. This Script loads the configured Scenes.

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class LoadFirstScene : MonoBehaviour
{
    public VectorValue startingPosition;
    // Start is called before the first frame update
    void Start()
    {
        //Here you can specify the starting World/Scene
        SceneManager.LoadScene("Area 1");
        //Add HUD over it
        SceneManager.LoadScene("Player HUD", LoadSceneMode.Additive);
        // Set the desired starting position
        startingPosition.initialValue = new Vector2(-15f, 41f);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}


```

In this example, the Scene `Area 1` is loaded, and the HUD Scene is also loaded additively.  
There is also a line that specifies the starting point of the Player in the loaded Scene.  
The Script should be adapted to load whatever Scene should be the starting Scene for our Game (World Selection Hub for example).
