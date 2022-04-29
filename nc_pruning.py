import math
from hand_of_the_king import getvalidmoves

def deepCopy(orig):
	copy = [[] for x in range(len(orig))]
	for row in range(len(orig)):
		for item in orig[row]:
			copy[row].append(item)
	return copy

def deepCopyBoard(orig):
	copy = []
	for item in orig:
		copy.append(item)
	return copy

def move(board, x, collection):
	# get the index of the purple card
	x1 = board.index(1)

	# color of the main card captured
	color = board[x]

	#1 card moves here
	board[x] = 1

	# Add main capture card color to list of captured cards
	collection[color - 2] += 1

	#move is left or right
	if abs(x -x1) < len(board):
		if x < x1:
			possible = range(x + 1, x1)
		else:
			possible = range(x1 + 1, x)
	else:
		if x < x1:
			possible = range(x+len(board), x1, len(board))
		else:
			possible = range(x1+len(board), x, len(board))
	

	for i in possible:
		if board[i] == color:
			board[i] = 0
			collection[color-2] += 1

	board[x1] = 0


def get_computer_move(board, cards, banners, turn):
	# deep copy board
	simBoard = deepCopyBoard(board)
	simCards = deepCopy(cards)
	simBanners = deepCopy(banners)

	
	

	# get valid moves
	moves = getvalidmoves(simBoard)

	# get best move
	best = moves[0]
	value = minVal(simBoard, simCards, simBanners, best, turn, -math.inf, math.inf)
	for action in moves[1:]:
		v = minVal(simBoard, simCards, simBanners, action, turn, -math.inf, math.inf)
		if v > value:
			best = action
			value = v
	return best



def minVal(board, cards, banners, action, turn, alpha, beta):
	# copy the stuff
	simBoard = deepCopyBoard(board)
	simCards = deepCopy(cards)
	simBanners = deepCopy(banners)


	# make move
	color = simBoard[action]
	move(simBoard, action, simCards[turn])


	# Check to see if current player should capture a banner
	if simCards[turn][color - 2] >= simCards[abs(turn - 1)][color - 2]:
		simBanners[turn][color - 2] = 1  # add the banner to the player's collection
		simBanners[abs(turn - 1)][color - 2] = 0
	
	# Switch turns
	turn = abs(turn - 1)

	
	#check if terminal state....is game over
	moves = getvalidmoves(simBoard)
	if(len(moves) == 0):
		#reached end of game check who was most banners
		if sum(simBanners[turn]) > sum(simBanners[abs(turn - 1)]):
			return -1
		elif sum(simBanners[abs(turn -1)]) > sum(simBanners[turn]):
			return 1
		else:
			return 0

	# set min to max value possible
	value = math.inf

	# loop over each possible action
	for action in moves:
		value = min(value, maxVal(simBoard, simCards, simBanners, action, turn, alpha, beta))
		if value <= alpha:
			return value
		beta = min(beta, value)
	return value


def maxVal(board, cards, banners, action, turn, alpha, beta):
	# copy the stuff
	simBoard = deepCopyBoard(board)
	simCards = deepCopy(cards)
	simBanners = deepCopy(banners)


	# make move
	color = simBoard[action]
	move(simBoard, action, simCards[turn])


	# Check to see if current player should capture a banner
	if simCards[turn][color - 2] >= simCards[abs(turn - 1)][color - 2]:
		simBanners[turn][color - 2] = 1  # add the banner to the player's collection
		simBanners[abs(turn - 1)][color - 2] = 0
	
	# Switch turns
	turn = abs(turn - 1)

	

	# check if terminal state....is game over
	moves = getvalidmoves(simBoard)
	if(len(moves) == 0):
		#reached end of game check who was most banners
		if sum(simBanners[turn]) > sum(simBanners[abs(turn - 1)]):
			return 1
		elif sum(simBanners[abs(turn -1)]) > sum(simBanners[turn]):
			return -1
		else:
			return 0


	# set max to min value possible
	value = -math.inf

	# loop over each possible action
	for action in moves:
		value = max(value, minVal(simBoard, simCards, simBanners, action, turn, alpha, beta))
		if value >= beta:
			return value
		alpha = max(alpha, value)
	return value