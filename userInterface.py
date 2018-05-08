import pygame
from peices import *
from ratings import Ratings
import time

class UserInterface:
    '''
    User interface class contains all Graphical User Interface components
    of program through pygame. This includes a function that Draws
    all elements including the board and peices. Class takes pygame surface
    and class of type board to be initialized with game

    '''
    def __init__(self, surface, Board):
        self.surface = surface  # Holds the surface variable defined for pygame
        self.inPlay = True  # Inplay variable to check if we are still playing the game
        self.squareSize = 75  # Size of square; used as a scale for peices and board squares (Re adjust this variable if you want to change size of game)
        self.peices = 64
        # mouseInitial Stores the inital X and y coordinates user makes when clicking mouse on board
        self.mouseInitialX = 0
        self.mouseInitialY = 0

        # mouseFinal Stores the finale X and y coordinates user makes when releasing mouse on board
        self.mouseFinalX = 0
        self.mouseFinalY = 0

        self.chessboard = Board  # Initialize given board onto interface
        self.playerMove = ""  # stores players move they make
        self.computerMove = "" # Stores computers move they make
        self.playerColor = "" # Color of player
        self.computerColor = "" # Color of computer




    def drawComponent(self):
        '''
        Draw component draws elements including the game board, chess chessPieces
        and text cues and indications
        '''
        # Creates visual representation of board by Making Checkered square pattern
        for i in range(0, self.peices, 2):
            pygame.draw.rect(self.surface, (120, 60, 30), [(i % 8+(i//8) % 2)*self.squareSize, (i//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws brown squares
            pygame.draw.rect(self.surface, (245, 245, 220), [((i+1) % 8-((i+1)//8) % 2)*self.squareSize, ((i+1)//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws beige squares
        #  Loop through every peice
        for index in range(self.peices):
            currentPosition = self.chessboard.boardArray[index//8][index % 8]  # looking at current peice in board
            # If we are looking at a white pawn
            if currentPosition == "P":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_pl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_pd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black pawn
            elif currentPosition == "p":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_pd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_pl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white knight
            elif currentPosition == "K":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_nl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_nd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black knight
            elif currentPosition == "k":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_nd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_nl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white bishop
            elif currentPosition == "B":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_bl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_bd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black bishop
            elif currentPosition == "b":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_bd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_bl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white rook
            elif currentPosition == "R":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_rl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_rd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black rook
            elif currentPosition == "r":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_rd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_rl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white queen
            elif currentPosition == "Q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_ql.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_qd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a black queen
            elif currentPosition == "q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_qd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_ql.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If we are looking at a white king
            elif currentPosition == "A":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_kl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto boardArray
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_kd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
            # If we are looking at a black king
            elif currentPosition == "a":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_kd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_kl.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize Peice image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto boardArray

        pygame.display.update()  # Update the display board when complete


    def eventHandler(self):
        '''
        Function for handling mouse events and reacting to them such as
        conducting moves
        '''
        # Read pygame events
        for event in pygame.event.get():
            # If user hits exit
            if event.type == pygame.QUIT:
                self.inPlay = False  # Set exit variable to false and exit loop
                break

            # If we press the mouse down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If we are currently inside the board
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseInitialX = pygame.mouse.get_pos()[0]  # Store clicked x position to mouseInitialX
                    self.mouseInitialY = pygame.mouse.get_pos()[1]  # Store clicked y position to mouseInitialY

            # If we release the mouse
            if event.type == pygame.MOUSEBUTTONUP:
                # If we are currently inside the board
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseFinalX = pygame.mouse.get_pos()[0]  # Store released x position to mouseFinalX
                    self.mouseFinalY = pygame.mouse.get_pos()[1]  # Store released y position to mouseFinalY
                    self.computeMove()  # Compute the move player has made

    def computeMove(self):
        """
        Computes move player makes onto the game board
        """
        # We now have to translate the coordinates in a way the board will understand
        # If we have a pawn promotion
        rowInitial = self.mouseInitialY//self.squareSize
        columnInitial = self.mouseInitialX//self.squareSize
        rowFinal = self.mouseFinalY//self.squareSize
        columnFinal = self.mouseFinalX//self.squareSize

        # IF player is performing a promotion move
        if rowFinal == 0 and rowInitial == 1 and self.chessboard.boardArray[rowInitial][columnInitial] == "P":
            # Allow player to choose which peice to promote
            promotionPeice = input("Promotion! Select promotion peice [Q,R,B,K]: ")
            # Send move to promote peice
            self.playerMove += str(columnInitial) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][columnFinal])+ promotionPeice + "P"

        # IF player is performing a castling move
        elif rowFinal == 7 and (columnInitial == 0 or columnInitial == 7) and self.chessboard.boardArray[rowInitial][columnInitial] == "R" and self.chessboard.boardArray[rowFinal][columnFinal] == "A":
            # Set current move as the current move player has made

            if columnInitial == 0:
                self.playerMove += str(columnInitial) + str(columnFinal-1) + str(columnFinal) + "R" + "C"
            elif columnInitial == 7:
                self.playerMove += str(columnInitial) + str(columnFinal+1) + str(columnFinal) + "R" + "C"

        # Otherwise we have a regular Move
        else:
            # Set current move as the current move player has made
            self.playerMove += str(rowInitial) + str(columnInitial) + str(rowFinal) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][(columnFinal)])

        # If the move we make is a valid move
        if self.playerMove in self.chessboard.generateMoveList():
            self.chessboard.computeMove(self.playerMove)  # Make the move on the board
            self.drawComponent()  # Visually update board
            # It's now the computer's turn to make a move. Call computerMoves
            self.computerMoves()
        else:
            print("Move Invalid or Unsafe")
        # Set current move back to empty to generate next move
        self.playerMove = ""
        self.computerMove = ""

    def computerMoves(self):
        '''
        Function for computer to conduct it's move using the alphaBeta function
        '''
        # Display that it is the computers turn
        if self.computerColor == "W":
            print("White's Turn")
        else:
            print("Black's Turn")

        self.chessboard.changePerspective()  # change to the computer's perspective
        self.computerMove = self.chessboard.alphaBeta(self.chessboard.MAXDEPTH, float("inf"), -float("inf"), "", 0)
        # If computer cannot make a move
        # Player wins
        if self.computerMove is None:
            print("CHECKMATE!")
            time.sleep(15)
            self.inPlay = False
        # Otherwise compute move
        else:
            self.chessboard.computeMove(self.computerMove)  # Allow computer to make move using alphaBeta

        self.chessboard.changePerspective()  # Change back to the player's persepctive
        self.drawComponent()  # Visually update board

        # If we have hit a checkmate or a stalemate
        # If checkmate
        if len(self.chessboard.generateMoveList()) == 0:
            if self.chessboard.kingissafe() is False:
                print("CHECKMATE!")
                time.sleep(15)  # 15 Second delay (usually to verify if checkmate is legitimate)
                self.inPlay = False
            # Otherwise if stalemate
            else:
                print("STALEMATE!")
                time.sleep(15)  # 15 Second delay (usually to verify if checkmate is legitimate)
                self.inPlay = False

        # Print check message if player is in check
        if self.chessboard.kingissafe() is False:
            print("Check!")

        # Display that it is the players turn
        if self.playerColor == "W":
            print("White's Turn")
        else:
            print("Black's Turn")


    def playGame(self):
        '''
        PlayGame function will run the gamn until he game ends, a reset is
        performed, or user exits the program
        '''
        self.surface.fill((0, 0, 0))  # initially Fill screen with black
        # Prompt user to select what colour they want to play as
        while(self.playerColor != "W" and self.playerColor != "B"):
            self.playerColor = input("Select Color (W/B): ")

        self.drawComponent()  # Call drawComponent to initially draw the board

        # Set computerColor based on color user selects
        if self.playerColor == "W":
            self.computerColor = "B"
        else:
            self.computerColor = "W"

        # If player is white, prompt player to go first
        if self.playerColor == "W":
            print("White's Turn")

        else:
            # Otherwise it is computers turn
            print("White's Turn")
            self.computerMoves() # Computer makes first move
            print("Black's Turn")
        # Call the event handler until user chooses to exit game
        while self.inPlay:
            self.eventHandler()  # Call eventHandler for players input
