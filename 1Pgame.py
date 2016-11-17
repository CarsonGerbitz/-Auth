def PrisonerGame():
	'''Starts the prisoner's dilema game.'''
	print("Welcome to the local precinct.")
	print("I'm going to make this real simple for you.")
	print("We don't actaully have enough evidance to book you and your partner in crime.")
	print("So, we want you to confess to us. And in return we'll let you off easy.")
	print("Now, you don't have to confess. But if your parnter confesses and you don't.")
	print("Well then your just in for a world of pain.")
	print("So, what will it be?")
	def TheChoice():
                from sys import exit
		import random
		PartnerAnswer = random.randint(0, 1)
		answer = raw_input("Confess or Deny? ")
		if answer == 'deny' and PartnerAnswer == 0:
			print("Congrats you both walk clean.")
			exit()
		if answer == 'deny' and PartnerAnswer == 1:
			print("Looks like your partner wasn't as quiet as you.")
			print("You're going away for a long time.")
			exit()
		if answer == 'confess' and PartnerAnswer == 0:
			print("Congrats, i'm sure your partner will be glad to know his friend was a snitch.")
			exit()
		if answer == 'confess' and PartnerAnswer == 1:
			print("Looks like we got ourselve a pair of snitches here.")
			exit()
		else:
			print("What was that? You have to speak up.")
			TheChoice()
	TheChoice()
PrisonerGame()
