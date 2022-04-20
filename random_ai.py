import random
from hand_of_the_king import getvalidmoves

def get_computer_move(board, cards, banners):
	"""
	Returns a random valid move.
	"""
	valid_moves = getvalidmoves(board)
	return random.choice(valid_moves)