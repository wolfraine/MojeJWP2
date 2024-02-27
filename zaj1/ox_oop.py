ALL_SPACES = list('123456789')
X, O, BLANK - 'X', 'O', ' '

class TTTBoard:
	def __init__(self, usePrettyBoard=False, useLogging=False):
		self._spaces = {}
		for space in ALL_SPACES:
			self._spaces[space] = BLANK 