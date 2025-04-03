# Umlgame

Umlgame is a minigame which is part of the Gamify-IT platform.

## About the Game

The game is built as a storyteller, with decision elements and tasks for the player.
These tasks are mainly uml related tasks, e.g. completing an uml diagram to fit the description, 
constructing a diagram from given code or text or vice versa.

## Room for expansion

The game currently includes the "completion" task type. This task asks the player to complete a given UML-diagram
based on the information given through its description.

The design of the game leaves room for more task types. Some that quickly come to mind would be error hunting,
creating a UML-diagram from given code or text and creating (pseudo-) code from a given diagram. These other tasks 
can be achieved in a similar way the completion task is implemented. Furthermore, the lecturer-interface is 
designed to make this easily possible.

#### What to add in the lecturer-interface
- In the `EditUmlGameConfigurationModal.vue` add the name of the new task type to the `selectionOptions` list
- In the `umlgame-models.ts` add the task type to the enum
  - depending on the task type, you might need to add another kind of configuration class (if your task type needs more than what is there already)
  - you might also need to check out the umlgame-rest-client.ts as well as the corresponding backend methods
- You can then add your edit modal at the bottom of the `EditUmlGameConfigurationModal.vue`
  - You also need to add the handler for your modal, similar to `handleCompletionTaskOk()`
  - Add your task type to the switch case in the `onEditClick()` method
Since the backend is mainly used to transfer and persist the data, no big changes should be necessary here.
The additions in the frontend can vary between the types, but you can still use the existing code as a guide.