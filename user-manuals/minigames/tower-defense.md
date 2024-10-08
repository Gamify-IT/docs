# Tower Defense

Tower Defense is a minigame which is part of the Gamify-IT platform.

## About the Game

The intention with this game is to make answering single choice questions fun.

When entering the game, the user is presented with the main menu.

After pressing the start button the enemies start spawning. The player then can place towers along the road to kill the enemies. Everytime the player wants to place a tower he must answer a question correctly to do so.

The player also can upgrade the towers to make them stronger, for each upgrade he also must answer a question correctly.


Once too many enemies reach the base the game ends. The longer the player survives the more points he can earn. 

## User Interface

![Start menu](assets/tower-defense-start-menu.webp)

The game will open with the start menu. There, you can choose to either start or exit the game.

![Game UI](assets/tower-defense-ui.webp)

When you start the game, the game map with the UI elements will be loaded. In the top right-hand corner you have a pause button and a speed up button. You can switch between standard pace and double pace. On the other side to the buttons, there is a life bar representing your current amount of health points.

At the beginning of the game, the shop menu is expanded allowing you to choose between towers with different attack styles. In the top left-hand corner of the shop menu you can see the current amount of currency available to you. After left-clicking on a tower you can move the cursor to the preferred position on the map and place the tower by left-clicking again. You can collapse the shop menu by clicking on the shop icon at the right-hand side.

## Game Mechanics

In Tower Defense, there are two conditions to finish the game:

1. When your life is empty, the game ends and you will be directed to the game over screen, where you can return back to the overworld.

2. If you answered all questions, the game also ends and you have the opportunity to see your results. 

## Sounds

In the overworld and each minigame, the player will hear different sounds. The player has an ability to control the volume of all sounds. You can read more about volume control here: [overworld volume control](../overworld/README.md#volume-control)

#### Background music

Upon entering the game, the player will immediately hear themed background music that will accompany them throughout the game.

#### Click sound

In the minigame, the player will find some interactive buttons, such as the option to start or exit the game. When the player clicks on a button, they will hear a click sound.

#### Tower shot

When enemies move, tower will attack them. In addition to the visual effects, there is also an audio effect that symbolises the sound of a shot.

#### Kill enemy
When the enemy is killed, the corresponding sound is played to inform the player of the enemy's death.

#### Tower update 
If the player answers the question correctly, they will have the opportunity to upgrade the tower. The correct answer and the opportunity to upgrade the tower will be accompanied by a sound symbolising the level up and the correct answer.

#### Triumph sound for end screen 
At the end of the game, the player will see the final screen accompanied by a sound symbolising the end of the game.

## Configuration

The lecturer can configure the game with an arbitrary number of questions.

Each question has a single correct answer and an arbitrary number of wrong answers.
The lecturer can also configure the time limit for the game.

For more information how to configure minigames see the [lecturer interface manual](../lecturer-interface/README.md).
