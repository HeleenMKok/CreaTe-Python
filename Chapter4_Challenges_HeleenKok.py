__author__ = 'heleenkok'
#Student Number: S1183435
#Python_Programming Chapter 4
#The end assignment from chapter 4

# Challenges:

# 1. Write a program that counts for the user.Let the user enter the starting number, the ending number, and the amount by which to count.
# 2. Create a program that gets a message from the user and then prints it out backwards.
# 3. Improve “Word Jumble” so that each word is paired with a hint. The player should be able to see the hint if he or she is stuck. Add a scoring system that rewards players who solve a jumble without asking for the hint.
# 4. Create a game where the computer picks a random word and the player has to guess that word. The computer tells the player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The computer can only respond with “yes” or “no”. Then, the player must guess the word.

# 1. Counting program
# Welcome the user and explain the counting program
# let the user set the start_number and the end_number
# and the step_number
# print all the numbers by using an for loop and range
print("\tWelcome to the Counting program!")
print("\nThis program does all the work for you. You can choose a starting and ending number.")
print("You can even choose the amount by which to count!\n")

start_number=int(input("At which number do you want to start counting?"))
end_number=int(input("At which number do you want to end counting?"))
step_number=int(input("By which amount do you want to count?"))
print("We have counted for you and this are the results: ")

for i in range(start_number,end_number,step_number):
    print(i, end=" ")
print("\nRun this code again and see if it can count every amount that you want to know...\n\n")


# 2. Print Backwards program
# Explain to the user what this program does
# Let the user enter a message and store this in message
# Use a for loop let i count backwards and print each character of the message beginning at the end en going backwards.
print("\tSecret language!")
print("Do you want to send a message in a secret languages so only you understand what is says?")
print("This program helps you to spell you message backwards.")

message=input("What is your message?\n")

print("Your secret message is:")
for i in reversed(message):
    print(i, end=" ")
print("Hope you enjoyed this program!\n\n")


# 3. Improved Word Jumble Program
# import the Word Jumble Program
# correct the welcoming text
# print the options from which the user can guess
# make the score variable. Length of the word times 10
# make a count variable, which counts the times the user tried to guess
# get the random letter hint code within the while loop that checks the guess and the word
# include the score!=0 in the while loop so it stops when the user has lost
# if the score is 0 print the text You Lose to inform the user that he lost
# print the end score and the times the user guessed the number
# end the program


#import the random library:
import random

# start the game
print(
"""
           Welcome to Word Jumble!
   Unscramble the letters to make a word.
You start with a score of 10 times the length of the word, if you use a hint your score will be reduced with 10 points.
"""
)

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
print("These are the options from which you can guess: ",WORDS)
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
# create a jumbled version of the word
jumble =""
# create a count variable
count=1
# create a score variable
score=len(word)*10
# Let the user make their first guess
guess = input("\nYour guess: ")

while guess != correct and guess != "" and score!=0:
    print("Sorry, that's not it.")
    hint=int(input("Do you want a hint? Press: 1. If you don't want to use a hint Press: 0."))
    if hint==1 and count!=len(word):
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
        print(jumble)
        count+=1
        score-=10
    guess = input("Your guess: ")

if score==0:
    print("You Lose... It took you to long to guess the word.")

if guess == correct:
    print("That's it!  You guessed it!\n")
print("\nYour score is:", score, "and it took you:", count, "times.")

print("Thanks for playing.")


# 4. Improved Word Guessing Game
# Create a Word Jumble Game
# Tell the user how many letters are in the word
# Give the user 5 chances to guess ask if a letter is in the word, the computer answers with yes or no
# Then the user has to guess the word.



#import the random library:
import random

# start the game
print(
"""
           Welcome to Word Guess Game!
   The PC will think of a word and tell you how many letters are in that word.
   You can ask the PC for hints, you ask if a letter is in the word. The PC corresponds with yes or no.
   However you only have five chances to ask what letter is in the word, so chose wisely.
You start with a score of 10 times the length of the word, if you use a hint your score will be reduced with 10 points.
"""
)

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
print("These are the options from which you can guess: ",WORDS)
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
# create a jumbled version of the word
jumble =""
# create the stop_hint variable
stop_hint=""
# create a count variable
count=1
# create a score variable
score=len(word)*10
# Tell the user how many letters are in the word:
print("The word has", score/10, "letters")
# Let the user make their first guess
guess = input("\nYour guess: ")
if guess != correct:
       print("Sorry, that's not it.")

while guess != correct and guess != "" and count<=5 and stop_hint!=1:

    letter=input("You can now ask the PC if a letter is in the word")
    score-=10
    count+=1
    if letter.lower() not in correct:
        print("No")
    else:
        print("Yes")
    stop_hint =int(input("Do you want to guess already? Yes; press 1. If you want to another hint? Press 0."))

guess = input("Your guess: ")
# When the user guesses wrong, tell him he lost
if guess != correct:
    print("To bad, you lose")
    score=0
#When the user guessed right, congratulate him
if guess == correct:
    print("That's it!  You guessed it!\n")
# Let the user know what his score is
print("\nYour score is:", score,".")

print("Thanks for playing.")
#exit statement
input("\n\nPress the enter key to exit.")
