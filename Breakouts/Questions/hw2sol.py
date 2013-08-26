
import random
import numpy as np
## the key is the starting point, the value is the ending point
board = {1: 38, 5: 14, 9: 31, 16: 6, 21: 42, 28: 84, 36: 44, 48: 26, 49: 11,
         51: 67, 56: 53, 62: 19, 64: 60, 71: 91, 80: 100, 87: 24, 93: 73, 95: 75, 98: 78}

class Pawn(object):

	def __init__(self,run_at_start=False):
		## start off at the beginning
		self.loc = 0
		self.path = []
		self.n_throws = 0
		self.n_chutes = 0
		self.n_ladders = 0
		self.reached_end = False
		if run_at_start:
			self.play_till_end()

	def play_till_end(self):

		while not self.reached_end:
			## throw a spin
			throw = random.randint(1,6)
			self.n_throws += 1

			# if we're near the end then we have to get exactly 100
			if throw + self.loc > 100:
				## oops. Can't move.
				self.path.append(self.loc)
				continue

			self.loc += throw
			self.path.append(self.loc)

			if board.has_key(self.loc):
				## new location due to chute or ladder
				if self.loc > board[self.loc]:
					self.n_chutes += 1
				else:
					self.n_ladders += 1

				self.loc = board[self.loc]
				self.path.append(self.loc)

			if self.loc == 100:
				self.reached_end = True

	def __str__(self):
		s = """n_throws = %i ; n_ladders = %i  ; n_chutes = %i 
		       path = %s""" % (self.n_throws,self.n_ladders, self.n_chutes, str(self.path))
		return s      

class Game(object):

	def __init__(self,n_players=2):

		self.n_players = n_players
		self.run()

	def run(self):
		self.pawns = [Pawn(run_at_start=True) for i in range(self.n_players)]
		self.settle_winner()

	def settle_winner(self):
		throws = [x.n_throws for x in self.pawns]
		self.min_throws, self.max_throws  = min(throws), max(throws)

		## if it's the same number, then make sure the Pawn that went first wins
		self.winning_order = [x for x,y in sorted(enumerate(throws), key = lambda x: (x[1],x[0]))]

		self.throws = throws

		## what's the first throw value and how long did it take to get to 100?
		self.first_throw_length = [(x.path[0],x.n_throws) for x in self.pawns ]

class Simulate(object):

	def __init__(self,num_games = 1000, num_players = 4):
		self.num_games = num_games
		self.num_players = num_players

	def run(self):
		self.shortest_path = []
		self.longest_path  = []
		#self.winner_times  = dict( [(i,0) for i range(num_players)] )
		self.all_lengths = []
		self.first_throws = dict( [(i+1,[]) for i in range(6)])

		self.first_turn_wins = []

		for i in range(self.num_games):
			g = Game(n_players=self.num_players)

			# save the shortest and longest paths
			if self.shortest_path == [] or (g.min_throws < len(self.shortest_path)):
				self.shortest_path = g.pawns[g.winning_order[0]].path
			if self.longest_path == [] or (g.max_throws > len(self.longest_path)):
				self.longest_path = g.pawns[g.winning_order[-1]].path

			## save all the lengths
			self.all_lengths.extend(g.throws)

			# save the first moves
			for ft in g.first_throw_length:
				#print ft
				self.first_throws[ft[0]].append(ft[1])

			# save the winning orders:
			self.first_turn_wins.append(int(g.winning_order[0] == 0))

	def __str__(self):
		avg_throws = np.array(self.all_lengths).mean()
		s = "1. What is the average number of turns a player must take before she gets to 100?\n"
		s += "%.2f\n\n" % avg_throws

		s+= "2. What is the minimal number of turns in the simulation before getting to 100?\n"
		s+= str(len(self.shortest_path) ) + "\n"
		s+= "What was the sequence of values in the spin in each turn?\n"
		s+= str(self.shortest_path) +"\n"
		s+= "What was the longest number of turns?\n"
		s+= str(len(self.longest_path)) + "\n\n"
		s+= "3. What is the ordering of initial spins that gives, on average, the quickest path to 100?\n"
		tmp= [(np.array(self.first_throws[t]).mean(), t) for t in self.first_throws.keys()]
		tmp.sort()
		s+= str(tmp) + " \n"
		s+= "What about the median?\n"
		tmp= [(np.median(np.array(self.first_throws[t])), t) for t in self.first_throws.keys()]
		tmp.sort()
		s+= str(tmp) + " \n\n"

		s+= "4. What is the probability that someone who goes first will win in a 2 and 4 person game?\n"
		s+= str(float(np.array(self.first_turn_wins).sum())/len(self.first_turn_wins)) + "\n"
		s+= "  random expectation is %f\n" % (1.0/self.num_players)
		return s

s = Simulate(num_games =10000, num_players=4)
s.run()
print s
s = Simulate(num_games =10000, num_players=2)
s.run()
print s

def test_Pawn():
	p = Pawn()
	p.play_till_end()
	print p

def test_Game():
	g = Game(4)
	g.settle_winner()




