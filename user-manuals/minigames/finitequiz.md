# Finitequiz

Finitequiz is a minigame which is part of the Gamify-IT platform.

## About the Game

The goal of the game is to provide a simple game for students to practice their knowledge with single choice questions.

![main menu screenshot](assets/finitequiz-game.webp)
When entering the game, the user is directly presented with the first question.
The score is displayed in the format `current score / max score`, meaning that the right number counts the total number of question that the player has answered.
The left number is only incremented when the player answers a question correctly.
When the user answers a question, they are presented with the next question.

![game screenshot](assets/finitequiz-end-screen.webp)
When all questions are answered, the end screen is presented.

At any point in the game, the player may choose to restart the game or to close the it, using the buttons in the top right corner.

## Configuration

The lecturer can configure the game with an arbitrary number of questions.

Each question has a single correct answer and an arbitrary number of wrong answers.
The lecturer can also configure the time limit for the game.

For more information how to configure minigames see the [lecturer interface manual](../lecturer-interface/README.md).

