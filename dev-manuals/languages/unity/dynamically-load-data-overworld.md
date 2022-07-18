# dynamically load data for overworld

here it is documented how data can be dynamically loaded into the overworld.
a lot of this depends on the database we create for the overworld.

## changing dialogue options dynamically

### idea 1

- we have a working demo dialogue with an npc (Assets/Scenes/Prototypes/Npc Dialogue/Npc Dialogue.unity)
  - a dialogue array of strings exists
  - the text needs to be added to the array
- To now change what the npc says dynamically we could use a text file that is created by the lecturer interface.
  - the lecturer inputs hints/lecture content into a text input from
  - this is saved with correct filename, which is specified by the system
- The text file could be separated in a way (for example using linebreaks) so every section is a new part of the dialogue (which you can click through)
- This text file can be read by a script in unity and added to an npc.
- There could be many text files that are named through a naming convention (something like "World1_Npc3.txt")
- npc need to have a number or id for this so the script can assign the correct text to the correct npc
- the lecturer interface will create a configuration file in some way anyways
  - the text files could be derived from that configuration file, or could be created separately automatically

### idea 2

- if we dont want to create extra text files out of the configuration
- we can get the data out of the configuration files
  - script to get the data might be a little bit more complex
  - should be still doable if we choose a good configuration file structure
- rest same as in idea 1  

## minigame spawn location

### current state

- currently only one minigame is set by hand to load when the player gets to the specific spot
- 12 minigame spots per world and 12 minigame spots per dungeon are available
  - marked with a specific texture on the floor

### goal

- a configuration file can set the minigame that spawns at which minigame point
  - content of the minigame (questions, answers, etc.) is also set with the config file
- a script then reads the config file and links minigame spot with the correct minigame  

## additional knowledge in books

- could be managed similar to [changing dialogue options dynamically](#changing-dialogue-options-dynamically)
- maybe different way to display book pages
  - more info could be displayed maybe almost fullscreen

## change color of npc that was talked to

there is already an issue for that: <https://github.com/Gamify-IT/issues/issues/116>

- once a npc is talked to, change the config file of the Npc
  - only a small change like a boolean is needed for this
- a script checks the boolean and changes the appearence of the npc according to it
  - npc could be in gray tones or have a checkmark above his head  

## area unlocking

### current state areas

- the current idea on progression is, that the player that successfully finishes a minigame gains knowledge
  - this knowledge level should be displayed on the HUD
- when he has mastered enough minigames (gained enough knowledge) the next World should unlock
- the Worlds have paths between each other that are blocked with an object that hinders the player from using the paths
  - if the needed knowledge level is achieved, the path unlocks
- it needs to be specified how many minigames need to be successfully finished to unlock the next area
  - all minigames? a major part?
- an idea was that the player gains an item once he reaches the needed knowledge level so he knows that he can advance to another world

### possibilities to solve problem

- every time the player finishes a minigame a file that stores user information is updated
  - the file holds information on how many (and which) minigames the player has successfully finished
- a script checks this file and calculates the knowledge level
  - this can update the HUD information
  - unlocking areas when set amount of knowledge achieved
