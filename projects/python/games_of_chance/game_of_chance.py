import random

money = 100


#coin flip function
def coin_flip(guess,bet):
	result = random.randint(1,2)
	global money
	if guess == "Heads" or guess == "Tails":
		print("Let's play a game of heads and tails!")
	else:
		print('Sorry, your guess can only be either "Heads" or "Tails". Please try to guess again with the proper input!'):
		return 0
	if bet > money:
		print("Sorry, your bet amount exceeds the money you currently have!")
		return 0
		print("You chose " + guess + "!")
	if result == 1:
		print("The coin flip resulted in Heads!")
	elif result == 2:
		print("The coin flip resulted in Tails!")		
	if (guess == "Heads" and result == 1) or (guess == "Tails" and result == 2):
		money += bet
		print("You have won $" + str(bet) + "!" )
		print("Your total money pool is now $" + str(money) + " to use on more bets!")
	else:
		money -= bet
		print("You have lost $" + str(bet) + "!" )
		print("Your total money pool is down $" + str(money) + " to use on more bets!")

#coin flip callouts
coin_flip("Heads", 10)
coin_flip("Tails", 20)
coin_flip("side", 20)


#cho han function
def cho_han(guess, bet):
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	dice_result = dice1 + dice2
	global money
	if guess == "Odd" or guess == "Even":
		print("Let's play a game of Cho Han!")
	else:
		print('Sorry, your guess can only be either "Odd" or "Even". Please try to guess again with the proper input!')
		return 0
	if bet <= 0:
		print("Sorry, your bet must be more than $1 dollar")
		return 0
	if bet > money:
		print("Sorry, your bet amount exceeds the money you currently have")
		return 0
		print("Let's play Cho Han!")
		print("You guessed " + guess + "!")
	if dice_result % 2 == 1:
		print("The dice rolls resulted as " + str(dice_result) + "!" + " An Odd Number!")
	elif dice_result % 2 == 0:
		print("The dice rolls resulted as " + str(dice_result) + "!" + " An Even Number!")
	if (guess == "Odd" and dice_result % 2 == 1) or (guess == "Even" and dice_result % 2 == 0):
		money += bet
		print("You have won $" + str(bet) + "!" )
		print("Your total money pool is now $" + str(money) + " to use on more bets!")
	else:
		money -= bet
		print("You have lost $" + str(bet) + "!" )
		print("Your total money pool is down $" + str(money) + " to use on more bets!")

#cho han callouts
cho_han("Odd", 200)
cho_han("Even", 20)


#deck of cards function

def deck_of_cards(guess, bet):










