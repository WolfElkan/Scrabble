import random
import const
import Player1, Player2

class Game(object):
	"""Scrabble Game Board object"""
	def __init__(self, *players):

		tilebag = ''.join([ letter * const.letters[letter]['freq'] for letter in const.letters ])
		tilebag = list(tilebag)
		# random.shuffle(tilebag)
		tilebag.sort()
		self.tilebag = tilebag

		# Deal letters
		for player in players:
			pass
			
	def dispense_letters(self, nLetters=7):
		nLetters = min(nLetters, len(self.tilebag))
		dispensed = self.letters[:nLetters]
		del self.letters[:nLetters]
		return dispensed