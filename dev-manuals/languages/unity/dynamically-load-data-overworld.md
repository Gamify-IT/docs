# dynamically load data for overworld

here it is documented how data can be dynamically loaded into the overworld.

## changing dialogue options dynamically

idea 1:  

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

## minigame spawn location

## additional knowledge in books

- could be managed similar to [changing dialogue options dynamically](#changing-dialogue-options-dynamically)
- maybe different way to display book pages
  - more info could be displayed maybe almost fullscreen

## change color of npc that was talked to

## area unlocking
