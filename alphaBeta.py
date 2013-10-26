# import random
# from gamePlay import valid, doMove, printBoard, gameOver
# from copy import deepcopy
# import pprint
# 
# 
# opponentColor = "W"
# playerColor = "B"
# 
# 
# def getAllPossibleMovesFromState(kBoard, color):
# 	"""
# 	return array of moves (i,j)
# 	"""
# 	
# 	moves = []
# 
# 	for i in range(8):
# 		for j in range(8):
# 			#dupBoard = deepcopy(kBoard)
# 			if valid(kBoard, color, (i, j)):
# 				moves.append((i, j))
# 
# 	"""
# 	print "NEXT MOVE FOR COLOR ",color
# 	print "NEXT MOVE FOR BOARD"
# 	pprint.pprint(kBoard)
# 	print"are"
# 	pprint.pprint(moves)
# 	"""
# 	return moves
# 
# """
# def value(board):
#     value = 0
#     for row in board:
# 	   for elem in row:
# 		  if elem == "W":
# 			 value = value + 0
# 		  elif elem == "B":
# 			 value = value + 1
#                   else:
#                          value = value+0.5
#     return value
# 
# 
# 
# def valueForColor(board, color):
#     value = 0
#     for row in board:
#         for elem in row:
#             if elem == color:
#                 value = value + 1
# 
#     return value
# """
# 
# 
# def evaluation(board):
#     value = 0
#     for i in range(8):
#         for j in range(8):
#             elem = board[i][j]
#             if elem == playerColor:
#                 value = value + 1
#                 if (j==0 and (i==0 or i==7)) or (j==7 and (i==0 or i==7)):
#                     value = value+7
#             elif elem == ".":
#                 value = value + 0.5
#             else:
#                 value = value + 0
# 
#     value = value + len(getAllPossibleMovesFromState(deepcopy(board), playerColor)) 
#     return value
# 
# 
# 
# 
# def resultOfAction(kBoard, kColor, kNextMove):
# 	"""
# 	return board after applying the action specified by move
# 	"""
# 	changedBoard = deepcopy(kBoard)
# 	doMove(changedBoard, kColor, kNextMove)
# 	
# 	return changedBoard
# 	
# 	
# 	
# def minValue(kBoard, kMaxDepth, kCurrentDepth, kColor,alpha,beta):
# 	"""
# 	return min value for board
# 	"""
# 	kMinValue = float("inf")
# 	kMove = "pass"
# 	
# 	
# 
# 	actions = getAllPossibleMovesFromState(kBoard, kColor)
# 	
# 	if kCurrentDepth == kMaxDepth or len(actions)==0:
# 		return evaluation(kBoard), kMove
# 	else:
# 		values = []
# 		causes = []
# 		states = []
# 		
# 		values.append(kMinValue)
# 		causes.append(kMove)
# 		states.append(kBoard)
# 		
# 		actions = getAllPossibleMovesFromState(kBoard, kColor)
# 		
# 		for move in actions:
# 			orignalBoard = deepcopy(kBoard)
# 			changedBoard = resultOfAction(orignalBoard, kColor, move)
# 			
# 			
# 			
# 			maxColor = "B" if kColor == "W" else "W"
# 			print "BEFORE MIN",kCurrentDepth,kMaxDepth,move
# 			newValue, newMove = maxValue(changedBoard, kMaxDepth, kCurrentDepth + 1, maxColor,alpha,beta)
# 			print "AFTER MIN",kCurrentDepth,kMaxDepth,move
# 			print ""
# 			
# 			#start
# 			values.append(newValue)
# 			causes.append(move)
# 			states.append(changedBoard)
# 
# 			#newValue = min(values)
# 			#end
# 			"""
# 			if newValue <= alpha and False:
# 				print "PRUNING minValue()"
# 				print "alpha :",alpha
# 				print "beta  :",beta
# 				pprint.pprint(values)
# 				#return newValue,move
# 			
# 			
# 			beta = MIN(beta,newValue)
# 			"""
# 		if len(values) > 0:
# 			kMinValue = min(values)
# 			index = values.index(kMinValue)
# 			kMove = causes[index]
# 	
# 		if kMinValue == float("inf"):
# 			kMove = "pass"
# 			return kMinValue, kMove
# 			
# 	
# 	
# 	 
# 	
# def maxValue(kBoard, kMaxDepth, kCurrentDepth, kColor,alpha,beta):
# 	"""
# 	get return max value for board
# 	"""
# 	kMaxValue = float("-inf")
# 	kMove = "pass"
# 	
# 	
# 	actions = getAllPossibleMovesFromState(kBoard, kColor)
# 
# 	if kCurrentDepth == kMaxDepth or len(actions)==0:
# 		return evaluation(kBoard), kMove
# 	else:
# 		values = []
# 		causes = []
# 		states = []
# 		values.append(kMaxValue)
# 		causes.append(kMove)
# 		states.append(kBoard)
# 
# 		actions = getAllPossibleMovesFromState(kBoard, kColor)
# 		for move in actions:
# 			
# 			
# 			
# 			orignalBoard = deepcopy(kBoard)
#         	changedBoard = resultOfAction(orignalBoard, kColor, move)
#         	
#         	
#         	minColor = "B" if kColor == "W" else "W"
#         	print " BEFORE MAX",kCurrentDepth,kMaxDepth,move
#         	newValue, newMove = minValue(changedBoard, kMaxDepth, kCurrentDepth + 1, minColor,alpha,beta)
#         	print " AFTER MAX",kCurrentDepth,kMaxDepth,move
#         	
#         	values.append(newValue)
#         	causes.append(move)
#         	states.append(changedBoard)
# 
#         	"""
#         	newValue = max(values)
#         	
#         	if newValue >= beta and False:
#         		print "PRUNING maxValue()"
#         		print "alpha :",alpha
#         		print "beta  :",beta
#         		pprint.pprint(values)
#          		#return newValue,move
#         	
#         	
#         	alpha = MAX(alpha, newValue)
#         	"""
# 		if len(values) > 0:
# 			kMaxValue = max(values)
# 			index = values.index(kMaxValue)
# 			kMove = causes[index]
# 		
# 		
# 		if kMaxValue == float("-inf"):
# 			kMove= "pass"	
# 			return kMaxValue, kMove
# 	
# 			
# 			
# 			
# 					
# 	
# 	
# 
# 
# def nextMove(board, color, time):
#     """
#     Get the move and the maximun value
#     """
#     global opponentColor
#     global playerColor
#     playerColor = color
#     opponentColor = "W" if (color == "B") else "B"
# 
#     
#     
#     alpha = float("-inf")
#     beta = float("inf")
#   
#     value, move = maxValue(board, 4, 0, color,alpha,beta)	
#     	 
#     print value, move
# 
#     return move
# 


import random
from gamePlay import valid, doMove, printBoard
from copy import deepcopy
import pprint


opponentColor = "W"
playerColor = "B"

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

"""
def converted(oldBoard,newBoard):
    
    val = 0;
    return 0;
    for i in range(8):
        for j in range(8):
            if oldBoard[i][j] == opponentColor and newBoard[i][j] == playerColor:
                val = val + 1
            elif oldBoard[i][j] == "." and newBoard[i][j] == playerColor:
                val = val + 1
        
    return val

def value(board):

    value = 0
    for row in board:
        for elem in row:
            if elem == "W":
                value = value + 0
            elif elem == "B":
                value = value + 1
            else:
                value = value + 0.5
    
    


    return value

"""

def evaluation(board):
    value = 0
    for i in range(8):
        for j in range(8):
            elem = board[i][j]
            if elem == playerColor:
                value = value + 1
                if (j==0 and (i==0 or i==7)) or (j==7 and (i==0 or i==7)):
                    value = value+8
            elif elem == ".":
                value = value + 0.5
            else:
                value = value + 0

    value = value + len(getAllPossibleMovesFromState(deepcopy(board), playerColor)) 
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
        return evaluation(kBoard), kMove
    else:
        actions = getAllPossibleMovesFromState(kBoard, kColor)

        for move in actions:
            orignalBoard = deepcopy(kBoard)
            changedBoard = resultOfAction(orignalBoard, kColor, move)
            maxColor = "B" if kColor == "W" else "W"
            newValue, newMove = maxValue(changedBoard, kMaxDepth, kCurrentDepth + 1, maxColor,alpha,beta)
            
            values.append(newValue)
            causes.append(move)
            states.append(changedBoard)
            
            if newValue <= alpha:
            	#print "PRUNING minValue()"
            	#print "alpha :",alpha
            	#print "beta  :",beta
            	#pprint.pprint(values)
            	return newValue,move
            
            
            beta = beta if (beta < newValue) else newValue # MIN(beta,newValue)
			




        if len(values) > 0:
            #pprint.pprint(values)
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

    if kCurrentDepth == kMaxDepth or len(actions) == 0:
        return evaluation(kBoard), kMove
    else:



        actions = getAllPossibleMovesFromState(kBoard, kColor)
        for move in actions:
            orignalBoard = deepcopy(kBoard)
            changedBoard = resultOfAction(orignalBoard, kColor, move)
            minColor = "B" if kColor == "W" else "W"
            newValue, newMove = minValue(changedBoard, kMaxDepth, kCurrentDepth + 1, minColor,alpha,beta)
            values.append(newValue)
            causes.append(move)
            states.append(changedBoard)
            
            #newValue = max(values)
            if newValue >= beta:
            	#print "PRUNING maxValue()"
            	#print "alpha :",alpha
            	#print "beta  :",beta
            	#pprint.pprint(values)
            	return newValue,move
            
            alpha = alpha if (alpha > newValue) else newValue # MAX(alpha, newValue)
        	
            
            
            

        if len(values) > 0:
            #pprint.pprint(values)
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
    global opponentColor
    global playerColor
    playerColor = color
    opponentColor = "W" if (color == "B") else "B"
    alpha = float("-inf")
    beta = float("inf")
    value, move = maxValue(board, 3, 0, color,alpha,beta)	
    print value, move
    return move



