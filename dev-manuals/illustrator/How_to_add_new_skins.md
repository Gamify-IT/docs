# Adding new outfits
The outfits are divided into skins and accessories. The categories are chosen in this way to differentiate between the characters themselves (or their clothing if you want to say so), and anything that is wearable on their head (glasses, hats, hair). In the following, the terms `head` and `body` will also be used to name these categories while `outfit` will be used as a general term that describes any change in appearance.

## Making a new outfit
To make any new outfit you first need to create a new sprite sheet. You can copy one of the existing sheets and use it as a template. Then you can use any image editor of your preference to change the sheet to your liking.
We advise to draw hats/glasses on a separate layer then the body giving you easy reference of the character while being able to only export the layer of the hat/glasses when finished.
This will be necessary, since head accessories need to be in their own sprite sheet without a character model underneath.

After you finished pixeling, you can add your sprite sheet to `Assets/Sprites/outfits/` and copy the settings of the existing sprite sheets. It is important that you slice your sprite sheet with a 16x32 grid, since it determines the size of the sprite.

## Creating animations for the outfit
To create animations you need to create a walking animation for each direction (4 frames) and a idle animation per direction (1 frame). You then need to create a `AnimatorController` under `Assets/Animations/Player/` you can copy a existing controller and change out the animations for your new ones. It is important to turn `loop time` on and set the frames to 5. When finished copy the Controller over to `Assets/Resources/AnimatorControllers` to make them available in the script.

## Adding the animation to the script
Open the `PlayerAnimation.cs` Script. Here you need to add a few values:
- in the `start()` method you need to add the positioning of your accessory to the dictionary present (only for accessories).
- below the `SetOutfitAnimator()` method is a list in which you need to add the name of your animator controller.
- if you need to scale your accessory you need to set this in the method itself, by extending the present if statement with your case.

## Making the outfit available in the character selection
