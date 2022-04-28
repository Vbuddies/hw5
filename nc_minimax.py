import math
import random
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

def get_computer_move(board, cards, banners, turn):
	# deep copy board
	simBoard = deepCopyBoard(board)
	simCards = deepCopy(cards)
	simBanners = deepCopy(banners)

	
	

	# get valid moves
	moves = getvalidmoves(simBoard)

	# call minimax
	# return best action
	# get all actions
	# value = min(board, best)
	# for action in actions[1:]:
		# 	v = min(board, action)
		# 	if v > value:
		# 		best = action
		# 		value = v
	# return best

	return random.choice(moves)



def minVal():
	pass
	# check if terminal state....is game over

	# set min to max value possible
	value = math.inf
	# loop over each possible action
		# value = min(value, maxVal(board, action)))	
	# return value


def maxVal():
	pass
	# check if terminal state....is game over

	# set max to min value possible
	value = -math.inf
	# loop over each possible action
		# value = max(value, minVal(board, action)))
	# return value

