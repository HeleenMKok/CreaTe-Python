__author__ = 'heleenkok'
#Student Number: S1183435
#Python_Programming Chapter 5
#The end assignment from chapter 5

# Challenges:
# 1. Create a program that prints a list of words in random order. The program should print all the words and not repeat any.
# 2. Write a Character Creator program for a role-playing game. The player should be given a pool of 30 points to spend on four attributes: Strength, Health, Wisdom, and Dexterity. The player should be able to spend points from the pool on any attribute and should also be able to take points from an attribute and put them back into the pool.
# 3. Write a Who’s Your Daddy? program that lets the user enter the name of a male and produces the name of his father. (You can use celebrities, fictional characters, or even historical figures for fun.) Allow the user to add, replace, and delete son- father pairs.


# 1. Random words from a list. Only print the words once
# first import random
# make a list called words
# pick a random word from the list
# make a loop to check if the word is printed already
# is the word is not printed print the word, els pick another word

# start
print(
"""
           Welcome to Random Word Order!
   This program will print the following list:
   "Tree", "Bag", "Happy", "Flame", "Pen"
                in a random order.
            Only printing the words once!
"""
)
import random
words = ["Tree", "Bag", "Happy", "Flame", "Pen"]
used = []

while words:
    pick = random.randint(0, len(words)-1) #get a random index number for words.
    used.append(words[pick]) #store the word in used
    del words[pick] #delete the word from words.

for word in used:
    print (word) # print the words in used.

print("This was the random word order program.")


#2 Role Playing game
# Player gets 30 points to spend on four objects
# objects: Strength, Health, Wisdom, and Dexterity
# player spends points or subtracts them from any object.
#

player_name=input("\nWhat is the name of your Hero?")
attributes = {'health': 0, 'strength': 0, 'wisdom': 0, 'dexterity': 0 }
chosen=None
points=30
while chosen != "0":
    print("You have", points)
    print(
            """
            What can you do with these points?
            0 Exit
            1 Spend points on an attribute
            2 Take points from an attribute
            3 See how many points each attribute has
            """
        )
    chosen=input("What do you want to do?")

    if chosen == "1":
        item_1 = input("\nOn which attribute do you want to spend points? ")
        if item_1 in attributes:
            give = int(input("How much points do you want to spend?\n"))
            if give < points:
                attributes[item_1]+=give
                points-=give
            else:
                print("\nYour hero does not have that amount of points \n")
        else:
            print("\nYour hero does not have that attribute.\n")

    elif chosen == "2":
        item_2 = input("\nFrom which attribute do you want to take points? ")
        if item_2 in attributes:
            take = int(input("How much points do you want to take?\n"))
            if take < attributes[item_2]:
                attributes[item_2]-=take
                points+=take
            else:
                print("\nThat attribute does not have that amount of points.\n")

    elif chosen == "3":
        print("\nYour hero has these attributes: ", attributes)
    elif chosen >= "4":
        print("\nInvalid, number.\n")

if chosen == "0":
    print("Good-bye.")
    #exit statement
    input("\n\nPress the enter key to exit.\n\n")
else:
    print("\n\nInvalid choice\n\n")


# 3 Who's Your daddy.
# make a library of {'sons':'fathers'}
# print the sons
# Let the user decide from which son the user wants to know the father.
# print the father.
# allow the user to add, replace and delete pairs.

print(""" \n\n\t Welcome to Who's Your Daddy!
In this game you can chose out of 4 sons and get to know who their father is.
Later on you can even edit the fathers and sons. \n\n
""")
men={'Mick':'George', 'Jan':'Hans', 'Richard':'Paul', 'Kees':'Dirk'}
# print(men)
sons=men.keys()
fathers=men.values()
choice=None
print(sons)
pick=input("\n\nFrom which son do you want to know his father?")
pickCap=pick.title()
print("The father of ", pickCap, "is", men.get(pickCap))

while choice !="0":
    print(
            """
            Now you can edit the fathers and sons.
            These are your options:
            0 Exit
            1 Get a to know a new father
            2 Add a new father and sons to the dictionary
            3 Give sons a different father
            4 Delete fathers and sons
            """
        )
    choice=input("Choice: ")


    if choice == "1":
        print(sons)
        pick=input("\nFrom which son do you want to know his father?")
        pickCap=pick.title()
        if pickCap in sons:
            print("The father of ", pickCap, "is", men.get(pickCap))
        else:
            print("\nI don't know this son but you can add him in the dictionary\n")

    elif choice == "2":
        new_son=input("\nWhat is the name of the son?")
        new_sonCap=new_son.title()
        if new_sonCap not in sons:
            new_father=input("What is the name of the father?")
            new_fatherCap=new_father.title()
            men[new_sonCap]=new_fatherCap
            print("\n", new_sonCap, "has been added.\n")
        else:
            print("\n That son already exists, but you can replace him.\n")

    elif choice == "3":
        new_son=input("\nWhat is the name of the son that you want to replace?")
        new_sonCap=new_son.title()
        if new_sonCap in sons:
                new_father=input("What is the name of the new father of this son?")
                new_fatherCap=new_father.title()
                men[new_sonCap]=new_fatherCap
                print("\n", new_son, "has a new father.\n")
        else:
                print("\nThat son does not exist! Try adding him.\n")

    elif choice == "4":
        new_son=input("\nWhich son do you want to delete?")
        new_sonCap=new_son.title()
        if new_sonCap in sons:
            del men[new_sonCap]
            print("Oke, he is removed from our dictionary.\n")
        else:
            print("\nI can't delete him, because he does not exist in the dictionary.\n")
    elif choice >= "5":
        print("\n\nInvalid choice.\n\n")

if choice == "0":
    print("Good-bye.")
    #exit statement
    input("\n\nPress the enter key to exit.\n\n")
else:
 print("\n\nInvalid choice.\n\n")
