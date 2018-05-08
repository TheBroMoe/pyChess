###### Mohammad Kebbi
###### Sheetal Gour

## References:
* Program Uses pygame: http://www.pygame.org/

  * Chess tile graphics were used from Wikimedia Commons: http://commons.wikimedia.org/wiki/File:Chess_tile_pd.png

  * alphaBeta Function was created based on the pseudocode Provided by wikipedia: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning


  * Used 'Fruit' values for rating material and similar values for other ratings from chessprogramming wikispace : https://chessprogramming.wikispaces.com/Point%20Value

  * Generating Move lists for each piece class was inspired by chessprogramming wikispace on move lists: https://chessprogramming.wikispaces.com/Move%20List

  * Board representation 'boardArray' is based off the 8x8 board array method: https://chessprogramming.wikispaces.com/8x8%20Board

  * Chess.com for descriptions of basic and special moves pieces can make:
  https://www.chess.com/learn-how-to-play-chess

## Description:
Pychess is a Player-Vs-AI chess engine implemented within pygame where a player is able to play chess against a computer that makes its own moves.
The game’s chess board and pieces was built using varying class based structures and polymorphism.
The Computer Ai is based on the alphabeta pruning search algorithm for evaluating potential moves it can make.

### The development of this project consisted of the following major milestones:

* Creation of a board class that contains all pieces and functions used to make moves on board, evaluate if player or computer is in check, etc.

* Creation of individual piece classes that have their own move sets based on the piece. Each piece class inherits an abstract ‘piece’ class with it’s own variables and methods. This process is called polymorphism. Each piece has methods that constructs its move set that it is allowed to make (a list of moves).
  #### The following move sets are included in the game
 * All basic moves a piece is allowed to make
 * Promotions: When player moves to the opposite side of a board with a pawn, it may exchange its current piece with either a rook, a queen, a bishop, or a knight
 * Castling:  On a player's turn he may move his king two squares over to one side and then move the rook from that side's corner right next to the king on the opposite side. -

 * En Passant:  If a pawn moves out two squares on its first move, and by doing so lands to the side of an opponent's pawn (effectively jumping past the other pawn's ability to capture it),
   that other pawn has the option of capturing the first pawn as it passes by. This special move must be done immediately after the first pawn has moved past,
   otherwise the option to capture it is no longer available.
  NOTE ABOUT EN PASSANT IMPLEMENTATION: we were able to get the move to work with our games logic (I.E En passant was possible within our movelist and making the move was successful).
   However the game kept running into problems with our user interface and due to time crunches were never resolved. As a result this version does not have En Passant implemented

* Creation of computer Ai that evaluates each individual move and decides which move to make based on the alpha beta pruning search algorithm

 #### Alpha Beta Pruning Summary: 
The algorithm maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively. Initially alpha is negative infinity and beta is positive infinity, i.e. both players start with their worst possible score. Whenever the maximum score that the minimizing player(beta) is assured of becomes less than the minimum score that the maximizing player(alpha) is assured of (i.e. beta <= alpha), the maximizing player need not consider the descendants of this node as they will never be reached in actual play. (ref: Wikipedia)

  IMPORTANT NOTE: The current maximum depth evaluates up to 3 plys. The algorithm supports
  running up to for plys however for the sake of running time and time it takes computers
  to make move it is 1 lower. You can set self.MAXDEPTH = 4 in the board initalizer method,
  if you want to see computer compute 'deeper' moves at the cost of how long method
  takes to return move

  Refer to link for more information on algorithm: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

* Creation of rating class that the computer uses to evaluate how ‘good’ a move is based on different factors.

* Creating  a graphical user interface using pygame that draws the board and chess pieces and allows user to play the game and make moves with the mouse and prompts or certain tasks are displayed on the terminal while game is running.

The contents in the file include:
* assets folder: Contains all the chess piece sprites used for game’s graphics.
* chess.py : Main program used to run interface and game. Run this program when starting the game
* board.py: Contains board class and it’s methods. Also contains the alphabeta method that the computer uses to make moves
* peices.py: Contains the master class ‘Peices’ as well as all individual piece classes that inheret the main class.
* ratings.py : Contains the ratings class with methods that evaluate the rating of a move.
* userInterface.py: Contains the userInterface class that is used to play the game and display the game using pygame.


## Setup Instructions:
  * Ensure that python 3 is installed 
  * Ensure all listed files are within the main directory 
  * Install pygame and run chess.py:
  
  ### For Windows
    
    # Python and pip must be in your path for this to work
    
    pip install --user pygame
    python chess.py
 
 ### For Ubuntu
  ```
  sudo apt install python3-pip
  pip3 -m install --user pygame
  python3 chess.py
  ```
  * After running the main program, user will be prompted to select their color in the terminal
   enter “W” for white or “B” for black
  * Whoever plays as white makes the first move
  * In case of promotion, Terminal asks to pick one of “Q” - queen, “R”- rook, “B”- bishop, and “K” - knight.
  * if king is not safe, terminal displays “Check!
  * if in checkmate, terminal displays “CHECKMATE!”
