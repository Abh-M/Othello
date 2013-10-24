import random
from gamePlay import valid, doMove, printBoard
from copy import deepcopy



def getAllPossibleMovesFromState(kBoard, color):
	"""
	return array of moves (i,j)
	"""
	moves = []

	for i in range(8):
		for j in range(8):
			if valid(kBoard, color, (i, j)):
				moves.append((i, j))

	return moves


def value(board):
    value = 0
    for row in board:
	   for elem in row:
		  if elem == "W":
			 value = value + 0
		  elif elem == "B":
			 value = value + 1
    return value



def valueForColor(board, color):
    value = 0
    for row in board:
        for elem in row:
            if elem == color:
                value = value + 1

    return value


def resultOfAction(kBoard, kColor, kNextMove):
	"""
	return board after applying the action specified by move
	"""
	changedBoard = deepcopy(kBoard)
	doMove(changedBoard, kColor, kNextMove)
	
	return changedBoard
	
	
	
def minValue(kBoard, kMaxDepth, kCurrentDepth, kColor,alpha,beta):
	"""
	return min value for board
	"""
	kMinValue = float("inf")
	kMove = "pass"
	values = []
	causes = []
	states = []
	
	values.append(kMinValue)
	causes.append(kMove)
	states.append(kBoard)

	
	
	if kCurrentDepth == kMaxDepth:
		return value(kBoard), None
	else:
		actions = getAllPossibleMovesFromState(kBoard, kColor)
        
        for move in actions:
			orignalBoard = deepcopy(kBoard)
			changedBoard = resultOfAction(orignalBoard, kColor, move)
			maxColor = "B" if kColor == "W" else "W"
			newValue, newMove = maxValue(changedBoard, kMaxDepth, kCurrentDepth + 1, maxColor)
			values.append(newValue)
			causes.append(move)
			states.append(changedBoard)
		
	if len(values) > 0:
		kMinValue = min(values)
		index = values.index(kMinValue)
		kMove = causes[index]
	
	if kMinValue == float("inf"):
		kMove = "pass"
	return kMinValue, kMove
			
	
	
	
	
def maxValue(kBoard, kMaxDepth, kCurrentDepth, kColor,alpha,beta):
	"""
	get return max value for board
	"""
	kMaxValue = float("-inf")
	kMove = "pass"

	if kCurrentDepth == kMaxDepth:
		return value(kBoard), None
	else:
		
		values = []
		causes = []
		states = []

        values.append(kMaxValue)
        causes.append(kMove)
        states.append(kBoard)


        actions = getAllPossibleMovesFromState(kBoard, kColor)
        for move in actions:
        	orignalBoard = deepcopy(kBoard)
        	changedBoard = resultOfAction(orignalBoard, kColor, move)
        	minColor = "B" if kColor == "W" else "W"
        	newValue, newMove = minValue(changedBoard, kMaxDepth, kCurrentDepth + 1, minColor)
        	values.append(newValue)
        	causes.append(move)
        	states.append(changedBoard)
			
	if len(values) > 0:
		kMaxValue = max(values)
		index = values.index(kMaxValue)
		kMove = causes[index]
		
		
	if kMaxValue == float("-inf"):
		kMove= "pass"	
	return kMaxValue, kMove
	
			
			
			
					
	
	


def nextMove(board, color, time):
    """
    Get the move and the maximun value
    """

	alpa = float("-inf")
	beta = float("inf")
    value, move = maxValue(board, 2, 0, color,alpha,beta) 
    print value, move
#     if value == float("inf") or value == float("-inf"):
#     	move = "pass"
    #raw_input()
    return move



