'''

another rhythm game
see readme for info (obviously)

'''

import random, time, json

class App:
	def __init__(self, maps, player):
		with json.load(open('assets/player.json', 'w')) as pf:
			self.player.name = pf[name]
			self.player.lvl = pf[lvl]
			