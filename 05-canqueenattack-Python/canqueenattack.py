# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and
# diagonally.

def canqueenattack(qX, qY, oX, oY):
    # Your code goes here
    if(qX == oX):
        return True
    if(qY == oY):
        return True
    if(abs(qX-oX) == abs(qY-oY)):
        return True
    return False
