# Configuring the Chickenshock minigame

Game specific properties can be configured in the file `Assets/Scripts/Properties/Chickenshock.properties` in the `chickenshock` repository.  
The file follows the format of [Java properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html).  
Currently, the following things can be configured:
  - `ingame.playtime` (in seconds, default `50`): Duration for which the user can play the game
  - `REST.saveRound` (default `minigames/chickenshock/api/v1/results`): backend path where to save data of one round
  - `REST.getQuestions` (default `minigames/chickenshock/api/v1/configurations/{id}/questions`): backend path for retrieving all questions for a run
