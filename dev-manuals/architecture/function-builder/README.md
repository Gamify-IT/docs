Architecture of Function Builder
Purpose
Function Builder is an interactive, logic-based game designed to teach programming and problem-solving skills. The game allows users to use various logic blocks to transform inputs into desired outputs. Players can enjoy both single-player and multiplayer modes, making it a versatile educational tool.

Table of Contents
<!-- TOC -->
Architecture of Function Builder
Purpose
Table of Contents
Links
General Code Structure
Frontend Architecture
Backend Architecture
Game Flow and Logic
Starting the Service
What to Look At
Known Design Flaws
Known Bugs
Tests
<!-- TOC -->
Links
The user manual explains how to play the game.
The program code is available here.
The overview of the architecture can be found here.
The backend architecture is described here.
General Code Structure
The codebase for Function Builder is organized into frontend and backend components. The frontend is built with Vue.js and manages the user interface and game logic, while the backend is built with Express.js and Socket.IO, handling real-time communication between players in multiplayer mode.

Frontend Architecture
The frontend of Function Builder is implemented using the Vue.js framework. It manages user interactions, rendering game states, and the game's logic blocks. Key components include:

MainPage.vue: The central interface where players enter their name, create or join rooms, and select game modes.
Game.vue: The core game interface where players can drag and drop logic blocks, execute their logic chains, and see real-time feedback.
Logic Blocks: Different game modes (Algebra, Lambda, Strings) each have their set of logic blocks, which players can use to manipulate inputs and achieve target outputs.
Multiplayer Interaction: The frontend communicates with the backend using Socket.IO for real-time multiplayer synchronization.
Key Files:
MainPage.vue: Handles room creation, joining, and game mode selection.
Game.vue: Manages the game state, player fields, and logic block execution.
router/index.js: Defines routes for different parts of the game (e.g., single-player, multiplayer).