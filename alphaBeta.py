import random
from gamePlay import valid, doMove, printBoard, gameOver
from copy import deepcopy
import pprint


def getAllPossibleMovesFromState(kBoard, color):
	"""
	return array of moves (i,j)
	"""
	
	moves = []

	for i in range(8):
		for j in range(8):
			dupBoard = deepcopy(kBoard)
			if valid(dupBoard, color, (i, j)):
				moves.append((i, j))

	"""
	print "NEXT MOVE FOR COLOR ",color
	print "NEXT MOVE FOR BOARD"
	pprint.pprint(kBoard)
	print"are"
	pprint.pprint(moves)
	"""
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

	actions = getAllPossibleMovesFromState(kBoard, kColor)
	
	if kCurrentDepth == kMaxDepth or len(actions)==0:
		return value(kBoard), kMove
	else:
		for move in actions:
			orignalBoard = deepcopy(kBoard)
			changedBoard = resultOfAction(orignalBoard, kColor, move)
			
			
# 			if gameOver(changedBoard):
# 				break
			
			maxColor = "B" if kColor == "W" else "W"
			newValue, newMove = maxValue(changedBoard, kMaxDepth, kCurrentDepth + 1, maxColor,alpha,beta)
			
			
			
			if newValue <= alpha:
				#print "PRUNING"
				#raw_input()
				return newValue,move
			
			
			beta = newValue if ( newValue < beta) else beta
			
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
	values = []
	causes = []
	states = []
	
	values.append(kMaxValue)
	causes.append(kMove)
	states.append(kBoard)
	
	
	actions = getAllPossibleMovesFromState(kBoard, kColor)

	if kCurrentDepth == kMaxDepth or len(actions)==0:
		return value(kBoard), kMove
	else:
		for move in actions:
			orignalBoard = deepcopy(kBoard)
        	changedBoard = resultOfAction(orignalBoard, kColor, move)
        	
        	#check if gameover
#         	if gameOver(changedBoard):
#         		break;
        	
        	minColor = "B" if kColor == "W" else "W"
        	newValue, newMove = minValue(changedBoard, kMaxDepth, kCurrentDepth + 1, minColor,alpha,beta)
        	
        	
        	if newValue >= beta:
        		#print "PRUNING"
        		#raw_input()
         		return newValue,move
        	
        	
        	alpha = alpha if (alpha > newValue) else newValue
        	
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
    alpha = float("-inf")
    beta = float("inf")
    value, move = maxValue(board, 3, 0, color,alpha,beta) 
    print value, move
#     if value == float("inf") or value == float("-inf"):
#     	move = "pass"
    #raw_input()
    return move



