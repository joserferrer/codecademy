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
		print("The dice rolls resulted as " + str(dice_result) + "!" + " An Odd number!")
	elif dice_result % 2 == 0:
		print("The dice rolls resulted as " + str(dice_result) + "!" + " An Even number!")
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


#higher card function

def higher_card(bet):
	player = random.randint(1,10)
	computer = random.randint(1,10)
	global money
	if bet <= 0:
		print("Sorry, your bet must be more than $1 dollar")
		return 0
	if bet > money:
		print("Sorry, your bet amount exceeds the money you currently have")
		return 0
		print("Let's draw a card!")
	if player == computer:
		print("You and the computer selected the same number " + str(player) + "! It's a tie!")
		return 0
	if player >= computer:
		money += bet
		print("You have drawn card #" + str(player) + " while the computer has draw card #" + str(computer) + "! Player wins $" + str(bet) + "! Your total money pool is now $" + str(money) + " to use on more bets.")
	elif computer >= player:
		money -= bet
		print("The computer has drawn card #" + str(computer) + " while you have drawn #" + str(player) + "! Computer wins! You have lost $" + str(bet) + "! Your total money pool is now $" + str(money) + " to use on more bets.")

#higher card callouts
higher_card(20)
higher_card(10)


#roulette function

def roulette(guess, bet):
	result = random.randint(0, 37)
	global money
	if isinstance(guess, str) and (guess == "Odd" or guess == "Even"):
		print("Let's play roulette! You placed your bet on " + str(guess) + "!")
	elif isinstance(guess, int) and (bet >= 0 and bet <= 36):
		print("Let's play roulette! You placed your bet on " + str(guess) + "!")
	else:
		print('Please make sure your bets are either on "Even", "Odd" or on Numbers 0 - 36!')
		return 0
	if bet <= 0:
		print("Sorry, your bet must be more than $1 dollar")
		return 0
	if bet > money:
		print("Sorry, your bet amount exceeds the money you currently have")
		return 0
	if result == 37:
		money -= bet
		print("The dice landed on 00!")
		print("You have lost $" + str(bet) + "!" )
		print("Your total money pool is down $" + str(money) + " to use on more bets!")
		return 0
	if (guess == "Even" and result % 2 == 0 and result != 0):
		money += bet
		print("The dice landed on " + str(result) + "! An Even number!")
		print("You have won $" + str(bet) + "! Your total money pool is now $" + str(money) + " to use on more bets!")
	elif (guess == "Odd" and result % 2 == 1 and result != 0):
		money += bet
		print("The dice landed on " + str(result) + "! An Odd number!")
		print("You have won $" + str(bet) + "! Your total money pool is now $" + str(money) + " to use on more bets!")
	elif guess == result:
		money += (bet * 35)
		print("The dice landed on " + str(result) + "! This matches your guess of " + str(guess) + "!")
		print("You have won $" + str(bet) + "! Your total money pool is now $" + str(money) + " to use on more bets!")
	else:
		money -= bet
		print("You've put a bet on the dice landing on " + str(guess) + " but it landed on " + str(result) + "!")
		print("You have lost $" + str(bet) + "!" )
		print("Your total money pool is down $" + str(money) + " to use on more bets!")



#roulette callouts
roulette("Odd", 20)
roulette(36, 20)
roulette(37, 20)

#roulette guess function checker experiment using lists
#def test(bet):
#	allowed_bets = set(["Odd", "Even"] + list(range(11)))
#		if bet in allowed_bets:
#			print("Let's Play")
#		else:
#			print("Must be Odd, Even or between 0 - 10")
#			return 0