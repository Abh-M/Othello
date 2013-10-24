import random
from gamePlay import valid, doMove, printBoard
from copy import deepcopy



def getAllPossibleMovesFromState(kBoard,color):
	"""
	return array of moves (i,j)
	"""
	moves = []

	for i in range(8):
		for j in range(8):
			if valid(kBoard, color, (i,j)):
				moves.append((i,j))

	return moves


def value(board):
    value = 0
    for row in board:
	   for elem in row:
		  if elem == "W":
			 value = value + 1
		  elif elem == "B":
			 value = value - 1
    return value



def resultOfAction(kBoard,kColor,kNextMove):
	"""
	return board after applying the action specified by move
	"""
	changedBoard = deepcopy(kBoard)
	doMove(changedBoard,kColor,kNextMove)
	
	return changedBoard
	
	
	
def minValue(kBoard,kMaxDepth,kCurrentDepth,kColor):
	"""
	return min value for board
	"""
	
	if kCurrentDepth == kMaxDepth:
		""" stop further exploration and return value for this state"""
		return value(kBoard)
	else:
		
		"""
		get all possible actions from this board state
		
		"""
		
		values = []
		causes = []
		states = []
		
		actions = getAllPossibleMovesFromState(kBoard,kColor)
		
		for move in actions:
			
			"""
			get board state after applying this move
			"""
			
			orignalBoard = deepcopy(kBoard)
			
			changedBoard = resultOfAction(orignalBoard, kColor, move)
			
			
			newValue = maxValue(changedBoard, kMaxDepth, kCurrentDepth+1, kColor)
			"""
			store the 
			1. Values as a result of each action
			2. Resulting state of the board
			3. The move causing the result
			"""
			
			values.append(newValue)
			causes.append(move)
			states.append(changedBoard)
			
		
		"""
		get the index of min value
		and return the min value
		"""
		
		if len(values) > 0:
			kMinVal = min(values)
			if kMinVal != None:
				index = values.index(kMinVal)
				return kMinVal
		

		return float("inf")
			
	
	
	
	
def maxValue(kBoard,kMaxDepth,kCurrentDepth,kColor):
	"""
	get return max value for board
	"""
	
	if kCurrentDepth == kMaxDepth:
		""" stop further exploration and return value for this state"""
		return value(kBoard)
	else:
		
		"""
		get all possible actions from this board state
		
		"""
		
		values = []
		causes = []
		states = []
		
		actions = getAllPossibleMovesFromState(kBoard,kColor)
		
		for move in actions:
			
			"""
			get board state after applying this move
			"""
			
			orignalBoard = deepcopy(kBoard)
			
			changedBoard = resultOfAction(orignalBoard, kColor, move)
			
			newValue = minValue(orignalBoard, kMaxDepth, kCurrentDepth+1, kColor)
			
			"""
			store the 
			1. Values as a result of each action
			2. Resulting state of the board
			3. The move causing the result
			"""
			
			values.append(newValue)
			causes.append(move)
			states.append(changedBoard)
			
		
		"""
		get the index of max value
		and return the max value
		"""
		if len(values) > 0:
			kMaxVal = max(values)
			if kMaxVal != None:
				index = values.index(kMaxVal)
				return kMaxVal
		
		return float("-inf")
	
			
			
			
					
	
	


def nextMove(board, color, time):
	moves = []
	allPossibleState = []
	for i in range(8):
		for j in range(8):
			if valid(board, color, (i,j)):
				moves.append((i,j))
	if len(moves) == 0:
		return "pass"
	else:
		
		actions = []
		resulting_states = []
		min_values = []
		
		maximumdepth = 2
		
		for move in moves:
			#print "-----Next move is---- ",move
			boardCopy = deepcopy(board)
			#print "----Before Move----"
#			printBoard(boardCopy)
			
			
			changedBoard = resultOfAction(boardCopy, color, move)
			
			#print "---Afer move----"
#			printBoard(boardCopy)
			
			
			#printBoard(newState)
			#print value(newState)
			
			min = minValue(changedBoard, maximumdepth, 0, color)
			
			actions.append(move)
			resulting_states.append(changedBoard)
			min_values.append(min)
			allPossibleState.append(boardCopy)
		
		
		if len(min_values) > 0:
			maximum = max(min_values)
			if maximum is not None:
				idx = min_values.index(maximum)
				bestMove = actions[idx]
				return bestMove
		
			
	#bestMove = moves[random.randint(0,len(moves) - 1)]
	return "pass"



