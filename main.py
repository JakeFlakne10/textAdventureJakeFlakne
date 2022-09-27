import time
from time import *

def clear():
    os.system('cls')

def Question1():
    #Rules
    print("Input sensitive, Y/N only")
    clear()

    #Story
    print("Your name is jake and life is mid.\n\n")

    #Question 1
    a1 = input("Do you start skating?\nY\nN\n")

    #input Y
    if a1 == "Y":
        Question2()

    #input N
    elif a1 == "N":
        print("You dont start your hobbies, life stays miserable, you fail at life.")

    #invalid input
    else:
        print("INVALID INPUT")
        clear()
        start()

def Question2():
    #Story
    clear()
    print("You start skating and hate life a slight bit less.")

    #Question 2
    a2 = input("Do you refind your interest in gaming?\nY\N\n")

    #input Y
    if a2 == "Y":
        Question3()

    #input N
    elif a2 == "N":
        print("you keep skating until you die at the ripe age of 25, life was still miserable but at least you were a pretty rad skater?")

    #invalid input
    else:
        print("INVALID INPUT")
        clear()
        start()

def Question3():
    #Story
    clear()
    print("Gaming is fun again! life still sucks tho.")

    #Question 3
    a3 = input("Do you try to learn bcs intro on your brothers guitar?\n\Y\nN\n")

    #input Y
    if a3 == "Y":
        Question4()

    #input N
    elif a3 == "N":
        print("You lose interest in your hobbies, become mentally ill agian, and fail at life.")

    #invalid input
    else:
        print("INVALID INPUT")
        clear()
        start()

def Question4():
    print("The enevitable happens, there are no more endings, you create your own")