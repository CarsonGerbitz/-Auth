def PrisonerGame2P():
	'''Launches the 2 player prisoner game'''
	choice1 = 0
	choice2 = 0
	name1 = 0
	name2 = 0
	def player1name():
		print("Hello player 1.")
		global name1
		name1 = input("What is your name? ")
	player1name()
	def player2name():
		print("Hello player 2.")
		global name2
		name2 = input("What is your name? ")
	player2name()
	def player1Choice():
		global choice1
		global name1
		global name2
		print("Listen, " + name1 + " We don't have enough evidence on you and your partner " + name2 + ". So, we want you to confess to us and in exchange we'll let you off easy.")
		print("Will you confess?")
		choice1 = input("Y/N")
	player1Choice()
	def player2choice():
		global choice2
		global name1
		global name2
		print("Listen, " + name2 + " We don't have enough evidence on you and your partner " + name1 + ". So, we want you to confess to us and in exchange we'll let you off easy.")
		print("Will you confess?")
		choice2 = input("Y/N")
	player2choice()
	def ending():
		global choice1
		global choice2
		global name1
		global name2
		if choice1 == 'y' and choice2 == 'y':
			print("Well then, " + name1 + " " + name2 + " It looks like you were not the people we were looking for. You two can go now.")
		if choice1 == 'n' and choice2 == 'n':
			print("Well then, " + name1 + + " " + name2 + " It seems there really is no loyalty between theives.")
		if choice1 == 'y' and choice2 == 'n':
			print("Well then, it looks like " + name2 + " had more faith in their partner than " + name1 + " did.")
		if choice1 == 'n' and choice2 == 'y':
			print("Well then, it looks like " + name1 + " had more faith in their partner than " + name2 + " did.")
	ending()
PrisonerGame2P()
