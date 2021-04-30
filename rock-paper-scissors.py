import random


def main():
	print("+--------------------------------------+",
	      "+------- ~ROCK PAPER SCISSORS~ --------+",
	      "+------- @Author: Dai Abdesslam -------+",
	      "+-------------  11/22/2018  -----------+",
	      "+--------------------------------------+",
	      sep='\n')
	print(">> Type 'quit' to quit the game.")
	print(">> Type 'status' to show scores.")
	print(">> Type 'rematch' to play again.")
	print(">> Type 'help' for help.")
	help_msg = "Game commands and options:\n" \
	           "-------------------------------\n" \
	           "rock/r/1\t\t\tChoose Rock as your weapon\n" \
	           "paper/p/2\t\t\tChoose Paper as your weapon\n" \
	           "scissors/s/3\t\tChoose Scissors as your weapon\n" \
	           "status\t\t\t\tShow games scores\n" \
	           "rematch\t\t\t\tRestart the game (reset scores)\n" \
	           "quit\t\t\t\tQuit the game\n" \
	           "help\t\t\t\tShow this message"
	user_wins = 0
	comp_wins = 0

	def who_won(a, b):
		print("Your score:", a, "\nVictoria's score:", b)
		if a > b:
			print("(You are the winner.)")
		elif b > a:
			print("(Victoria is the winner.)")
		else:
			print("(Draw)")

	choices = ["Rock", "Paper", "Scissors"]
	run = True
	print("1- Rock\n2- Paper\n3- Scissors")
	while run:
		choice = input(">> Choose your weapon [R/P/S] ").lower().strip()
		comp_weapon = random.choice(choices)
		if choice == "":
			print("Please choose your weapon.")
		elif choice == "r" or choice == "1" or choice == "rock":
			print("You choose Rock")
			print("Victoria chooses", comp_weapon)
			if comp_weapon == "Rock":
				print(" // Draw // ")
			elif comp_weapon == "Paper":
				print(" -- You Lose -- ")
				comp_wins += 1
			else:
				print(" ++ You Win ++ ")
				user_wins += 1
		elif choice == "p" or choice == "2" or choice == "paper":
			print("You choose Paper")
			print("Victoria chooses", comp_weapon)
			if comp_weapon == "Rock":
				print(" ++ You Win ++ ")
				user_wins += 1
			elif comp_weapon == "Paper":
				print(" // Draw // ")
			else:
				print(" -- You Lose -- ")
				comp_wins += 1
		elif choice == "s" or choice == "3" or choice == "scissors":
			print("You choose Scissors")
			print("Victoria chooses", comp_weapon)
			if comp_weapon == "Rock":
				print(" -- You Lose -- ")
				comp_wins += 1
			elif comp_weapon == "Paper":
				print(" ++ You Win ++ ")
				user_wins += 1
			else:
				print(" // Draw // ")
		elif choice == "status":
			print("Game Status:", "\nYour score:", user_wins, "\nVictoria's score:", comp_wins)
		elif choice == "rematch":
			who_won(user_wins, comp_wins)
			user_wins = 0
			comp_wins = 0
		elif choice == "quit":
			ask = input(">> Are you sure you want to quit the game? [Y/N] ").lower().strip()
			if ask == "y":
				run = False
				who_won(user_wins, comp_wins)
				print("Thanks for playing :)")
			elif ask == "n":
				print("Good")
			else:
				print("Please type 'y' for yes OR 'n' for no.")
		elif choice == "help":
			print(help_msg)
		else:
			print("Unknown command.")


main()
