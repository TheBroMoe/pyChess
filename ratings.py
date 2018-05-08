from peices import*


class Ratings:
    """
    Class that contains function used to evaluate ratings made by the alphaBeta computer.
    Upon completion a rating will consider
        Attack: Are we in danger of being attacked by any peice or being put to check
        material: How many peices (material) are still in play
        Moveability: Evaluate If we are in checkmate or stalemate
    """

    def __init__(self, Board):
        self.rating = 0  # Set the overall rating to be zero
        self.material = 0  # Set the material to zero
        self.chessboard = Board  # Save board to class


    def evaluateRating(self, moveCount, depth):
        '''
        Evaluates the overall rating of a move based on the factors above.
        This is used for the alphaBeta computer to evaluate which move has the
        best rating based off it's own algorithm

        args:
            moveCount: the number of moves we can currently make. We want to know
            how  many moves (in essense how flexible) can we move?

            depth: How deep are we in our alphaBeta search

        returns:
            rating: The score and 'quality' of our current move
            to be compared with the rest of other move's ratings

        '''

        # Begin by evaluating how "good" our rating is
        self.material = self.rateMaterial()  # Evaluate the board's material
        self.rating += self.material  # Add rating by material
        self.rating += self.rateAttack()  # Evalue attack rating
        self.rating += self.rateMoveability(moveCount, depth, self.material)  # Evaluate moveability Rating

        # We now want to evaluate our opponents rating and subtract it from our own
        self.chessboard.changePerspective()  # Begin by changing to opponents perspective
        # Evaluate opponent's material
        self.material = self.rateMaterial()
        self.rating -= self.material

        self.rating -= self.rateAttack()  # Evaluate opponent's attack rating
        self.rating -= self.rateMoveability(moveCount, depth, self.material)  # Evaluate opponent's moveability

        self.chessboard.changePerspective()  # Return to our persepctive
        # Once material is evaluated return a negated version of our rating
        # (Works with algorithm) and add score based on how deep we currently are in the search tree
        return -(self.rating + depth*60)


    def rateMaterial(self):
        """
        Function adds up the material of all peices currently on the chessboard

        Returns: materialRating
        """
        materialRating = 0  # Counter for evaluating material
        bishopCounter = 0  # keep count of how many bishops are in board
        # Loop through all positions on the board to see how many peices we have
        for index in range(self.chessboard.TOTALPIECES):
            CaseTest = self.chessboard.boardArray[index//8][index % 8]
            # If we have a pawn
            if CaseTest == "P":
                materialRating += 100  # Increase Material
            # If we have a rook
            elif CaseTest == "R":
                materialRating += 600  # Increase Material
            # If we have a king
            elif CaseTest == "K":
                materialRating += 400  # Increase Material
            # If we have a bishop
            elif CaseTest == "B":
                bishopCounter += 1  # Increment bishop counter
            # If we have a queen
            elif CaseTest == "Q":
                materialRating += 1200  # Increase Material

        # Evaluate bishop material based on bishop counter
        # Bonus points if we have a pair of bishops
        if bishopCounter >= 2:
            materialRating += 200*bishopCounter  # Increase Material
        # Not as many points if we only have one bishop
        elif bishopCounter == 1:
            materialRating += 150  # Increase Material

        return materialRating  # Return material

    def rateAttack(self):
        """
        Function that evaluates attack rating: Are we in danger of being attacked by any peice
        or being put into checkmate

        Returns: attackRating
        """
        attackRating = 0

        temporyKingPosition = self.chessboard.kingPosition_White
        # Go through every peice in board
        for i in range(self.chessboard.TOTALPIECES):
            CaseTest = self.chessboard.boardArray[i//8][i%8]
            # Evalutate if current peice is a pawn
            if CaseTest == "P":
                self.kingPosition_White = i  # Move king to current position
                # If move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 30
            # Evalutate if current peice is a Rook
            elif CaseTest == "R":
                self.kingPosition_White = i  # Move king to current position
                # If move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 250
            # Evalutate if current peice is a Knight
            elif CaseTest == "K":
                self.kingPosition_White = i  # Move king to current position
                # If move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 150
            # Evalutate if current peice is a Bishop
            elif CaseTest == "B":
                self.kingPosition_White = i  # Move king to current position
                # If move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 150
            # Evalutate if current peice is a Queen
            elif CaseTest == "Q":
                self.kingPosition_White = i  # Move king to current position
                # If move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 450

        self.chessboard.kingPosition_White = temporyKingPosition
        # If we are currently not safe
        if (self.chessboard.kingissafe() is False):
            attackRating -= 500
        return attackRating

    def rateMoveability(self, moveCount, depth, material):
        """
        How flexible is our move system
        This will evaluate checkmates or stalemates, check are also usually restricted

        Args:
            moveCount: the number of moves we can currently make. We want to know
            how  many moves (in essense how flexible) can we move?

            depth: How deep are we in our alphaBeta search

            material: our material rating based on the value returned by rateMaterial
        """
        moveabilityRating = moveCount  # essentially adding points for how flexible our Moveability is


        # If we have no avaiable moves, it means we are either in checkmate or stalemate
        if moveCount == 0:
            # If king is not safe, it means we are in checkmate
            if self.chessboard.kingissafe() is False:
                moveabilityRating += -(150000*depth)  # Rating (for good reason) would be very very bad!

            # Otherwise if stalemate
            else:
                moveabilityRating += -(100000*depth)  # Still bad, but not as bad as checkmate


        return moveabilityRating
