

from gamePlay import valid, doMove
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


def evaluation(board):
    value = 0
    for i in range(8):
        for j in range(8):
            elem = board[i][j]
            if elem == playerColor:
                value = value + 1
                if (j==0 and (i==0 or i==7)) or (j==7 and (i==0 or i==7)):
                    value = value+8
#                 elif (j==0 and (i in range(8))) or (j==7 and (i in range(8))):
#                     value = value+4
#                 elif ((i==0 or i==7) and (j in range(8))):
#                     value = value+4
            elif elem == ".":
                value = value + 0.5
            else:
                value = value + 0

    value = value + len(getAllPossibleMovesFromState(deepcopy(board), playerColor)) - len(getAllPossibleMovesFromState(deepcopy(board), opponentColor)) 
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
    kBoard = deepcopy(board)
    actions = getAllPossibleMovesFromState(kBoard, color)
    p = len(actions)
    l=3
    if time < 10.0:
        l = 2
    elif time >30.0 and p>10:
        l = 4
    else:
        l = 3;
    #raw_input();
    
    value, move = maxValue(board, l, 0, color,alpha,beta)    
    #print value, move
    return move







# def nextMove(board, color, time):
#     """
#     Get the move and the maximun value
#     """
#     nextMove.limit = time if nextMove.limit == 0.0 else nextMove.limit
#     nextMove.timediff = nextMove.oldTime - time
#     nextMove.oldTime = time
#     nextMove.counter = nextMove.counter + 1
#     global opponentColor
#     global playerColor
#     playerColor = color
#     opponentColor = "W" if (color == "B") else "B"
#     alpha = float("-inf")
#     beta = float("inf")
#     kBoard = deepcopy(board)
#     actions = getAllPossibleMovesFromState(kBoard, color)
#     p = len(actions)
# #    print "Counter: ",nextMove.counter,"LIMIT :",nextMove.limit,"OLD :",nextMove.oldTime,"CURR :",time,"DIFF :",nextMove.timediff," P :",p
#     l=3
#     if time < 10.0:
#         l = 2
#     elif time >30.0 and p>10:
#         l = 4
#     else:
#         l = 3;
#     #raw_input();
#     
#     value, move = maxValue(board, l, 0, color,alpha,beta)	
#     #print value, move
#     return move
# 
# 
# 
# #nextMoveWithTime
# 
# 
# nextMove.oldTime = 0.0
# nextMove.counter = 0
# nextMove.timediff = 0.0
# nextMove.limit = 0.0

