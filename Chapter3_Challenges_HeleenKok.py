__author__ = 'heleenkok'
#Student Number: S1183435
#Python_Programming Chapter 3
#The end assignment from chapter 3

# Challenges:
# 1. Write a program that simulates a fortune cookie. The program should display one of five unique fortunes, at random, each time it’s run.
# 2. Write a program that flips a coin 100 times and then tells you the number of heads and tails.
# 3. Modify the Guess My Number game so that the player has a limited number of guesses. If the player fails to guess in time, the program should display an appropriately chastising message.
# 4. Here’s a bigger challenge. Write the pseudocode for a program where the player and the computer trade places in the number guessing game. That is, the player picks a random number between 1 and 100 that the computer has to guess. Before you start, think about how you guess.If all goes well, try coding the game.


# 1. Fortune cookie program
# Welcome the user
# Pick a random number between 1 and 5
# Pick a fortune, out of five fortunes relating the random number
# Print the fortune

import random
fortune_1="Your shoes will make you happy today."
fortune_2="A dream you have will come true."
fortune_3="The greatest risk is not taking one."
fortune_4="Now is the time to try something new."
fortune_5="You are very talented in many ways."

print("\tWelcome to the Fortune Cookie program!")
print("\nYour fortune cookie says: \n")
fort_numb=random.randint(1,5)
if fort_numb==1:
    print(fortune_1)
elif fort_numb==2:
    print(fortune_2)
elif fort_numb==3:
    print(fortune_3)
elif fort_numb==4:
    print(fortune_4)
else:
    print(fortune_5)



# 2. Flip a coin program
# Explain the game
# Set the count number to 1
# Set the heads_value to 0
# Set the tails_value to 0
# while count<=100
# Randomly choose 1 or 2
# If 1 the coin value is heads, add 1 to the heads_value
# Elif 2 the coin value is tails, add 1 to the tails_value
# Else the coin has a secret value print congratulations your coins is invalid
# Add 1 to count.
# When count is 100 print: After flipping the coin 100 times we counted (print value heads_value) times heads and (print value tails_value) times tails.

print("\n\n\tWelcome to the Flip a Coin Program\n")
print("The program will flip a coin 100 time")
print("It will count the times it landed on heads and on tails")
print("Then it will tell you the exact amounts.\n")
count_number=1
heads_value=0
tails_value=0
while count_number<=100:
    coin_value=random.randint(1,2)
    count_number+=1
    if coin_value==1:
        heads_value+=1
    elif coin_value==2:
        tails_value+=1
    else:
        print("The coin was so special that it had no head and no tail.")
print("After flipping 100 times we counted",heads_value,"times heads and",tails_value,"times tails.\n\n")


# 3. Modification to Guess My Number, by giving the user the user 10 times to guess the number
# welcome the player to the game and explain it
# pick a random number between 1 and 100
# ask the player for a guess
# set the number of guesses to 1
# while the number of guesses is smaller then 10
# while the player’s guess does not equal the number
# if the guess is greater than the number: tell the player to guess lower
# otherwise tell the player to guess higher
# get a new guess from the player
# increase the number of guesses by 1
# congratulate the player on guessing the number
# let the player know how many guesses it took

print("\tWelcome to the modified 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in less then 10 attempts.\n")

# set the initial values
the_number = random.randint(1, 100)
# print(the_number) # I used this line to check if it worked
guess = int(input("Take a guess: "))
tries = 1

    # guessing loop
while guess != the_number:
    tries+=1
    if tries>10: # When the user has guessed more then 10 times, print Game Over and break the while loop
        print("Game Over! It took you more then 10 attempts.\n")
        break
    elif guess > the_number: #if the guessed number is bigger, print Lower...
        print("Lower...")
    else: #if the guessed number is lower, print higher
        print("Higher...")
    guess = int(input("Take a guess: ")) #let the user guess again

if guess == the_number: #if the guessed number is correct print the following lines:
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")
    print("End of the Guess My Number game, I hope you enjoyed it!\n\n")


#4 PC Guess my number
# Welcome the player and explain
# Let the player give the input for the user_number
# Let the PC pick a random_number between 1 and 100
# Set the number of guesses to 1
# While the random_number is not equal to the user_number
# Increase the number of guesses by 1
# Set the random_number to a new random number between 1 and 100
# Congratulate the player and let the player know how many guesses it took
# Quit the game

print("\tWelcome to the NEW 'Guess My Number'!")
print("\nThis time we will switch seats! You may pick a number between 1 and 10.")
print("And the PC will try to guess it in less then 10 attempts.\n")

# Set the initial values
user_number = int(input("Pick a number between 1 and 10: "))
times = 1
pc_guess = random.randint(1, 10)

# The while loop is used to compare the user_number to the pc_guess
while pc_guess != user_number: # when the numbers are not the same run the while loop
    times+=1 # add 1 to the attempts of the PC
    if times>10: # When the PC has guessed more then 10 times, congratulate the user and break the while loop
        print("You win!! It took the PC more then 10 attempts to guess your number!!\n")
        break
    pc_guess = random.randint(1, 10) # give a new value to pc_guess
    print("Is it", pc_guess,"?")
    print("No.")

if pc_guess == user_number: #if the guessed number is correct print the following lines:
    print("The PC guessed it! The number was", user_number)
    print("It took", times, "tries!\n")
    print("End of the NEW Guess My Number game, I hope you enjoyed it!\n\n")

#exit statement
input("\n\nPress the enter key to exit.")
