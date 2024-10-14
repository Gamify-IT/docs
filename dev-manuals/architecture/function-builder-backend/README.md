Backend Architecture
The backend is a Node.js application using Express and Socket.IO. It handles real-time synchronization between players, room creation, and game state management. Players can join rooms, and the backend ensures that turns are handled correctly for each player.

Key Responsibilities:
Real-time Communication: The backend uses Socket.IO to communicate real-time changes between players. It ensures that both players see the same game state at any given time.
Room Management: The backend creates rooms for multiplayer games and assigns players to them. Once both players are in a room, the game starts.
Game Logic: The backend maintains the logic for turn-based interaction in multiplayer mode, ensuring that players alternate turns in an orderly fashion.
Key Files:
server.js: The entry point of the backend that initializes the Express server and Socket.IO, manages rooms, and handles player connections.
routes/game.js: Handles game-specific routes for room creation and joining.
Game Flow and Logic
Single Player Mode
Player selects the desired game mode (Algebra, Lambda, or Strings).
The game presents an input value and a target output.
The player uses logic blocks to transform the input into the target output.
The game evaluates the player's solution, providing feedback in real-time.
Multiplayer Mode
Players create or join rooms using the room name or a randomly generated room ID.
Once both players are in the room, the game starts.
The game alternates between players, allowing each to take a turn in constructing their logic block chains.
Both players work towards the same target output, and the first to achieve the correct transformation wins the game.
Starting the Service
Backend:
To start the backend server:

Install the dependencies:
bash
Копиране на код
npm install
Start the server:
bash
Копиране на код
npm start
Frontend:
Install dependencies:
bash
Копиране на код
npm install
Start the frontend:
bash
Копиране на код
npm run serve
What to Look At
Key areas to focus on for understanding the game's architecture:

MainPage.vue and Game.vue (frontend) for user interaction and game state logic.
server.js (backend) for real-time synchronization and room management.
Known Design Flaws
Turn-based Sync: The current turn-based multiplayer mechanism may introduce slight delays, especially in high-latency environments. Optimizing the turn-sync mechanism could improve responsiveness.
Room Limits: Currently, rooms are limited to two players. Future iterations might want to consider expanding this to support multiple players or teams.
Known Bugs
An up-to-date list of open bugs can be found at Function Builder Issues.

Tests
In general, the following things are tested for Function Builder:

User interface elements and game logic are tested manually during development.
Socket.IO events are tested to ensure proper real-time synchronization between players in multiplayer mode.