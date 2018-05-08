

class Peices:
    """
    Creation of abstract Peices class, for each individual peice to inherit
    the chessboard class, as well as their own respective findMoveSet method
    """

    def __init__(self, Board):
        self.chessboard = Board  # Store the instance of the board to the peice

    def findMoveSet(self, index):
        """
        This will be the abstract function that all peices has to evaluate what moves
        can be made by that respective peice
        """
        pass


class Rook(Peices):
    """
    Inherited peice class of the rook. This class includes all the methods
    used to evaluate all the moves that can be made by the rook
    """

    def testCastling(self, row, column, i, board_roamer):
        """
        Helper function to check if rook can perform the special castling move
        """
        castling = ""  # Initialize castle move (would return nothing if we can't perform)
        # If we are on the last row
        if row == 7:
            # If we are evaluate the rook's initial positions
            if column == 0 or column == 7:
                # If we can reach king with now peices in between
                if self.chessboard.boardArray[row][column+board_roamer*i] == "A":
                    previousPosition = self.chessboard.boardArray[row][column+board_roamer*i]  # define previousPosition as potential peice
                    self.chessboard.boardArray[row][column] = "A"  # Set current position of peice to blank
                    self.chessboard.boardArray[row][column+board_roamer*i] = "R"  # Set potential peice to promotion peice
                    # If move is a safe move, and no negative indexing is occuring
                    if self.chessboard.kingissafe() and (column+board_roamer*i) >= 0:
                        # Format: column rook, column king, Rook, king,C
                        # Compute move as it is valid
                        if column == 0:
                            castling += str(column)+str(column+board_roamer*i-1) + str(column+board_roamer*i)+"R"+"C"
                        elif column == 7:
                                castling += str(column)+ str(column+board_roamer*i+1) + str(column+board_roamer*i)+"R"+"C"
                    self.chessboard.boardArray[row][column] = "R"  # Set current peice back to Rook
                    self.chessboard.boardArray[row][column+board_roamer*i] = previousPosition

        return castling

    def testHorizontal(self, row, column, i, movelist):
        """
        Helper function to check if horizontal move is valid
        """
        board_roamer = 1  # set board_roamer back to start
        # Go through infinite loop to evaluate all horizontal moves
        try:
            # Keep looping until we reach a non blank space
            while(self.chessboard.boardArray[row][column+board_roamer*i] == " "):
                previousPosition = self.chessboard.boardArray[row][column+board_roamer*i]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row][column+board_roamer*i] = "R"  # Set potential peice to current peice
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and column+board_roamer*i >= 0:
                    movelist += str(row) + str(column) + str(row) +str(column + board_roamer*i) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current peice back to rook
                self.chessboard.boardArray[row][column+board_roamer*i] = previousPosition  # Set potential peice back to it's previousPosition
                board_roamer += 1  # Increment board roamer

            if self.chessboard.boardArray[row][column+board_roamer*i].islower():
                previousPosition = self.chessboard.boardArray[row][column+board_roamer*i]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row][column+board_roamer*i] = "R"  # Set potential peice to current peice
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and column+board_roamer*i >= 0:
                    movelist += str(row) + str(column) + str(row) +str(column + board_roamer*i)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current peice back to Rook
                self.chessboard.boardArray[row][column+board_roamer*i] = previousPosition  # Set potential peice back to it's previousPosition

            movelist += self.testCastling(row, column, i, board_roamer)

        except IndexError:
            pass

        return movelist

    def testVertical(self, row, column, i, movelist):
        """
        Helper function to check if vertical move is valid
        """
        board_roamer = 1  # set board_roamer back to start
        # We now have to do the same thing for vertical moves
        try:
            # Keep looping until we reach a non blank space
            while(self.chessboard.boardArray[row+board_roamer*i][column] == " "):
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row+board_roamer*i][column] = "R"  # Set potential peice to current peice
                # If move is a safe move
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0:
                    movelist += str(row) + str(column) + str(row+board_roamer*i) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current peice back to Rook
                self.chessboard.boardArray[row+board_roamer*i][column] = previousPosition  # Set potential peice back to it's previousPosition
                board_roamer += 1  # Increment board roamer

            if self.chessboard.boardArray[row+board_roamer*i][column].islower():
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row+board_roamer*i][column] = "R"  # Set potential peice to current peice
                # If move is a safe move
                if self.chessboard.kingissafe() and (row+board_roamer*i) >= 0:
                    movelist += str(row) + str(column) + str(row+board_roamer*i) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current peice back to
                self.chessboard.boardArray[row+board_roamer*i][column] = previousPosition  # Set potential peice back to it's previousPosition
        except IndexError:
            pass

        return movelist

    def findMoveSet(self, index):
        """
        Goes through the potential moves a rook can make and if it's a safe move
        (The king is not in check) and a legal move, then that move is a potential move.

        Args: index: Current position of the board we are evaluating

        Returns: Move set of all potential moves rook can make
        """
        movelist = ""  # declare a list that will store all potential moves.
        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8

        for i in range(-1, 2, 2):
            movelist = self.testVertical(row, column, i, movelist)
            movelist = self.testHorizontal(row, column, i, movelist)

        return movelist  # Return list of moves possible


class Knight(Peices):
    """
    Inherited peice class of the knight. This class includes all the methods
    used to evaluate all the moves that can be made by the knight
    """
    def findMoveSet(self, index):
        """
        Goes through the potential moves a knight can make and if it's a safe move
        (The king is not in check) and a legal move, then that move is a potential move.

        Args: index: Current position of the board we are evaluating

        Returns: Move set of all potential moves knight can make
        """
        movelist = ""  # declare a list that will store all potential moves.

        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8
        # For loop to cover particular moves a knight can make
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                # Covers moves where knight moves two columns and one row
                try:
                    if self.chessboard.boardArray[row+i][column+j*2] == " " or self.chessboard.boardArray[row+i][column+j*2].islower():
                        previousPosition = self.chessboard.boardArray[row+i][column+j*2]  # define previousPosition as potential peice
                        self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                        self.chessboard.boardArray[row+i][column+j*2] = "K"  # Set potential peice to current peice
                        # If move is a safe move, and no negative indexing is occuring
                        if self.chessboard.kingissafe()and row+i >= 0 and column+j*2 >= 0:
                            movelist += str(row)+str(column) + str(row+i) + str(column+j*2) + str(previousPosition)  # Add tested move to our movelist
                        self.chessboard.boardArray[row][column] = "K"  # Set current peice back to knight
                        self.chessboard.boardArray[row+i][column+j*2] = previousPosition  # Set potential peice back to it's previousPosition
                except IndexError:
                    pass
                # Covers moves where knight moves two rows and one column
                try:
                    if self.chessboard.boardArray[row+i*2][column+j] == " " or self.chessboard.boardArray[row+i*2][column+j].islower():
                        previousPosition =self.chessboard.boardArray[row+i*2][column+j]  # define previousPosition as potential peice
                        self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                        self.chessboard.boardArray[row+i*2][column+j] = "K"  # Set potential peice to current peice
                        # If move is a safe move, and no negative indexing is occuring
                        if self.chessboard.kingissafe() and row+i*2 >= 0 and column+j >=0:
                            movelist += str(row)+str(column) + str(row+i*2) + str(column+j) + str(previousPosition)  # Add tested move to our movelist
                        self.chessboard.boardArray[row][column] = "K"  # Set current peice back to knight
                        self.chessboard.boardArray[row+i*2][column+j] = previousPosition  # Set potential peice back to it's previousPosition
                except IndexError:
                    pass

        return movelist  # Return list of moves possible


class Bishop(Peices):
    """
    Inherited peice class of the Bishop. This class includes all the methods
    used to evaluate all the moves that can be made by the Bishop
    """
    def checkDiagonal(self, movelist, row, column, i, j):
        """
        Helper function to check if diagonal move is valid
        """
        board_roamer = 1  # temporary variable to increment through board
        try:
            while(self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] == " "):
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "B"  # Set potential peice to current peice
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "B"  # Set current peice back to Bishop
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential peice back to it's previousPosition
                board_roamer +=1  # Increment board_roamer
            if self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j].islower() :
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "B"  # Set potential peice to current peice
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "B"  # Set current peice back to
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential peice back to it's previousPosition
        except IndexError:
            pass
        return movelist


    def findMoveSet(self, index):
        """
        Goes through the potential moves a bishop can make and if it's a safe move
        (The king is not in check) and a legal move, then that move is a potential move.

        Args: index: Current position of the board we are evaluating

        Returns: Move set of all potential moves bishop can make
        """
        movelist = ""  # declare a list that will store all potential moves.
        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8
        # For loop that covers all diagonal moves
        for i in range(-1, 2, 2):
            for j in range(-1, 2,2):
                movelist = self.checkDiagonal(movelist, row, column, i, j) # Check if bishop can move


        return movelist  # Return list of moves possible


class Queen(Peices):
    """
    Inherited peice class of the Queen. This class includes all the methods
    used to evaluate all the moves that can be made by the Queen
    """
    def testMovement(self, row, column, i, j, movelist):
        board_roamer = 1  # temporary variable to increment through board
        try:
            while(self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] == " "):
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "Q"  # Set potential peice to current peice
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "Q"  # Set current peice back to queen
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential peice back to it's previousPosition
                board_roamer += 1  # increment board_roamer
            # If we can capture a peice
            if self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j].islower():
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "Q"  # Set potential peice to current peice
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "Q"  # Set current peice back to queen
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential peice back to it's previousPosition
        except IndexError:
            pass
        return movelist

    def findMoveSet(self, index):
        """
        Goes through the potential moves a Queen can make and if it's a safe move
        (The king is not in check) and a legal move, then that move is a potential move.

        Args: index: Current position of the board we are evaluating

        Returns: Move set of all potential moves Queen can make
        """
        movelist = ""  # declare a list that will store all potential moves.
        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8
        # For loop that covers all possible moves Queen can make
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    movelist = self.testMovement(row, column, i, j, movelist)


        return movelist  # Return list of moves possible


class King(Peices):
    """
    Inherited peice class of the king. This class includes all the methods
    used to evaluate all the moves that can be made by the king
    """
    def testMove(self, index, row, column, i, movelist):
        try:
            # If potential position is blank or has an enemy peice
            if self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3].islower() or self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3] == " ":
                previousPosition = self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3] = "A"  # Set potential peice to current peice
                kingTemp = self.chessboard.kingPosition_White  # Store current kingPosition_in temporary variable
                self.chessboard.kingPosition_White = index+(i//3)*8 +i%3-9  # Set new potential king position

                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and row-1+i//3 >=0 and column-1+ i%3>=0:
                        movelist += str(row)+str(column)+str(row-1+i//3)+str(column-1+i%3)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "A"  # Set current peice back to king
                self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3] = previousPosition  # Set potential peice back to it's previousPosition
                self.chessboard.kingPosition_White = kingTemp  # Set king position back to current
        except IndexError:
            pass
        return movelist

    def findMoveSet(self, index):
        """
        Goes through the potential moves a king can make and if it's a safe move
        (The king is not in check) and a legal move, then that move is a potential move.

        Args: index: Current position of the board we are evaluating

        Returns: Move set of all potential moves king can make
        """
        movelist = ""  # declare a list that will store all potential moves.
        # define row and column variables with respect to index

        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8

        for i in range(9):
            # if king makes a move (essentially index 4 is the kings current position and we do not want to check that spot)
            if i != 4:
                movelist = self.testMove(index, row, column, i, movelist)

        return movelist  # Return list of moves possible


class Pawn(Peices):
    """
    Inherited peice class of the pawn. This class includes all the methods
    used to evaluate all the moves that can be made by the pawn
    """
    def testMovement(self, row, column, index, movelist):
        # Can pawn move one up
        try:
            # If potential space is blank and index is below promotion level
            if self.chessboard.boardArray[row-1][column] == " " and index >= 16:
                previousPosition = self.chessboard.boardArray[row-1][column]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row-1][column] = "P"  # Set potential peice to current peice
                # If move is a safe move
                if self.chessboard.kingissafe() and (row-1) >= 0:
                    movelist += str(row) + str(column) + str(row-1) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "P"  # Set current peice back to pawn
                self.chessboard.boardArray[row-1][column] = previousPosition  # Set potential peice back to it's previousPosition
        except IndexError:
            pass

        # Can pawn move two up
        try:
            # If potential space is blank and index is below promotion level
            if self.chessboard.boardArray[row-1][column] == " " and self.chessboard.boardArray[row-2][column] == " " and index >= 48:
                previousPosition = self.chessboard.boardArray[row-2][column]  # define previousPosition as potential peice
                self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                self.chessboard.boardArray[row-2][column] = "P"  # Set potential peice to current peice
                # If move is a safe move,
                if self.chessboard.kingissafe() and row-2 >=0:
                    movelist += str(row) + str(column) + str(row-2) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "P"  # Set current peice back to pawn
                self.chessboard.boardArray[row-2][column] = previousPosition  # Set potential peice back to it's previousPosition

        except IndexError:
            pass

        # If pawn able to perform Promotion without capturing
        try:
            # If potential space is blank and index is above promotion level
            if self.chessboard.boardArray[row-1][column] == " " and index < 16:
                promotionList = ["Q", "R", "B", "K"]  # Define a list of peices pawn can be Promoted to

                # loop through promotion peices in promotionList to generate potential move sets
                for promPiece in promotionList:
                    previousPosition = self.chessboard.boardArray[row-1][column]  # define previousPosition as potential peice
                    self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                    self.chessboard.boardArray[row-1][column] = promPiece  # Set potential peice to current peice
                    # If move is a safe move
                    if self.chessboard.kingissafe():
                        # Format: column 1, column 2, captured-piece, new-piece, P
                        movelist += str(column) + str(column) + str(previousPosition) + str(promPiece) + "P"  # Add tested move to our movelist
                    self.chessboard.boardArray[row][column] = "P"  # Set current peice back to pawn
                    self.chessboard.boardArray[row-1][column] = previousPosition  # Set potential peice back to it's previousPosition
        except IndexError:
            pass

        return movelist

    def testCapture(self, index, row, column, movelist):
        for i in range(-1, 2, 2):
            try:
                # Check if we encounter a peice
                if self.chessboard.boardArray[row-1][column+i].islower():
                    if index < 16:
                        promotionList = ["Q", "R", "B", "K"]  # Define a list of peices pawn can be Promoted to
                        # Loop through promotionList peices to evaluate different potential moves with different peices
                        for promPiece in promotionList:
                            previousPosition = self.chessboard.boardArray[row-1][column+i]  # define previousPosition as potential peice
                            self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                            self.chessboard.boardArray[row-1][column+i] = promPiece  # Set potential peice to promotion peice

                            # If move is a safe move, and no negative indexing is occuring
                            if self.chessboard.kingissafe() and (column+i) >= 0:
                                # Format: column 1, column 2, captured-piece, new-piece,P
                                movelist += str(column) + str(column+i)+str(previousPosition)+str(promPiece)+"P"
                            self.chessboard.boardArray[row][column] = "P"  # Set current peice back to pawn
                            self.chessboard.boardArray[row-1][column+i] = previousPosition  # Set potential peice back to it's previousPosition

                    # If we have a promotion and capture case
                    else:
                        previousPosition = self.chessboard.boardArray[row-1][column+i]  # define previousPosition as potential peice
                        self.chessboard.boardArray[row][column] = " "  # Set current position of peice to blank
                        self.chessboard.boardArray[row-1][column+i] = "P"  # Set potential peice to current peice
                        # If move is a safe move, and no negative indexing is occuring
                        if self.chessboard.kingissafe() and (row-1) >= 0 and (column+i) >= 0:
                            movelist += str(row) + str(column) + str(row-1)+str(column+i) + str(previousPosition)  # Add tested move to our movelist
                        self.chessboard.boardArray[row][column] = "P"  # Set current peice back to pawn
                        self.chessboard.boardArray[row-1][column+i] = previousPosition  # Set potential peice back to it's previousPosition

            except IndexError:
                pass

        return movelist

    def findMoveSet(self, index):
        """
        Goes through the potential moves a pawn can make and if it's a safe move
        (The king is not in check) and a legal move, then that move is a potential move.

        Args: index: Current position of the board we are evaluating

        Returns: Move set of all potential moves pawn can make
        """
        movelist = ""  # declare a list that will store all potential moves.

        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8

        # Loop through potential moves pawn can make for capturing

        movelist = self.testCapture(index, row, column, movelist)

        movelist = self.testMovement(row, column, index, movelist)


        return movelist  # Return list of moves possible
