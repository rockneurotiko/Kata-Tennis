global PUNTOS
PUNTOS = [0,15,30,40]


class Game:

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2

		player1.setContrincant(player2)
		player2.setContrincant(player1)

	def resumeGame(self):
		pl1Ad = pl2Ad = ""
		if(self.player1.advance):
			pl1Ad = "A"
		elif(self.player2.advance):
			pl2Ad="A"
			
		print("---------------------------")
		print("%s : %d   %s|  %d" %(self.player1.name, self.player1.points, pl1Ad, self.player1.gamesWins))
		print("%s : %d   %s|  %d" %(self.player2.name, self.player2.points, pl2Ad, self.player2.gamesWins))
		print("---------------------------")

	def winPoints(self, player):
		if(self.testNotWinner()):
			player.winPoints()

	def testNotWinner(self):
		if(self.player1.winner or self.player2.winner):
			print "Ya hay un ganador"
			return False
		return True


class Player:

	def __init__(self, name): #, game):
		self.name = name
		self.points = 0
		self.pointsIndex = 0
		self.advance = False
		self.gamesWins = 0
		self.winner = False


	def setContrincant(self, contrincant):
		self.contrincant = contrincant

	def testContrincant(self):
		return(self.contrincant != None)

	def increasePoints(self):
		self.pointsIndex += 1
		self.points = PUNTOS[self.pointsIndex]
		
	def startMatch(self):
		self.points=0
		self.pointsIndex=0
		self.advance = False

	def winMatch(self):
		self.startMatch()
		self.contrincant.startMatch()
		self.gamesWins += 1
		if (self.gamesWins>= 6):
			self.winner = True

	def deuce(self):
		if(self.contrincant.advance):
			self.contrincant.advance = False
		else:
			self.advance = True

	def winPoints(self):
		if(self.testContrincant()):
			if(self.pointsIndex<3):
				self.increasePoints()
			elif(self.contrincant.pointsIndex < 3):
				self.winMatch()
			elif(self.advance):
				self.winMatch()
			else:
				self.deuce()
