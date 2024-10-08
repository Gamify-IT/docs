# Towercrush

Towercrush is a minigame which is part of the Gamify-IT platform.

## About the Game

The goal of the game is to provide a simple game for students to practice their knowledge with single choice questions while competing against fellow students.

![main menu screenshot](assets/towercrush-game.webp)
When entering the game, the user is presented with a lobby search screen.
Once the user joined a lobby they can choose one of two teams to join and can ready up.
If every user in the lobby has chosen a team and readied up, the players can start the game by clicking the Start button.
The users can only go to the next question once every member of the team has voted for their preferred answer.
Teams get rewarded with points for every question they answered correctly, the aim of the game is to keep the tower of your team alive by getting as many points as possible.

Once a team has answered every question, or one of the team's towers reaches zero the game ends.

The winning team is the one whose tower is the last one standing, or whichever team has answered more questions correctly.

![game end screenshot](assets/towercrush-end-screen.webp)
When all questions are answered, you will be notified which team won.

## Sounds

In the overworld and each minigame, the player will hear different sounds. The player has an ability to control the volume of all sounds. You can read more about volume control here: [overworld volume control](../overworld/README.md#volume-control)

#### Background music

The player hears themed background music when entering the game.

#### Click sound

In the minigame, the player will find some interactive buttons, such as the option to start or exit the game. When the player clicks on a button, they will hear a click sound.

#### Sound when answer is pressed

When the player clicks on any answer, the answer selection sound will play.

#### Sound for end of minigame

At the end of the game, a screen will appear telling the player which team has won, accompanied by a game over sound.

## Configuration

The lecturer can configure the game with an arbitrary number of questions.

Each question has a single correct answer and an arbitrary number of wrong answers.

For more information how to configure minigames see the [lecturer interface manual](../lecturer-interface/README.md).

