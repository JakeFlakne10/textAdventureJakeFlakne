#importing
import time
from time import *
import os
from os import *

#define clear command
def clear():
    os.system('cls')

def Question1():
    #Rules
    print("Input sensitive, Capitilization is important")
    clear()

    #Story
    print("Your name is jake and life is mid.\n")

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
    print("You start skating and hate life a slight bit less.\n")

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
    print("Gaming is fun again! life still sucks tho.\n")

    #Question 3
    a3 = input("Do you try to learn the bcs intro on your brothers guitar?\n\Y\nN\n")

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
    #Story
    clear()
    print("You keep playing guitar, you really like it, it quites the voices.\n")

    #Question 3
    a4 = input("Do you get a grip on your diet, and start eating healthy and drinking a lot of water?")

    #input Y
    if a4 == "Y":
        Question5()

    #input N
    elif a4 == "N":
        print("You keep eating like crap, hate your body, and stay self concious")

    #invalid input
    else:
        print("INVALID INPUT")
        clear()
        start()

def Question5():
    #Story
    clear()
    print("Your get on track with your diet, you start to feel good about yourself.\n")

    #Question 3
    a5 = input("You used to work out, but couldnt stay on track, should you pick up the weights again?")

    #input Y
    if a5 == "Y":
        Question6()

    #input N
    elif a5 == "N":
        print("You are not proud of your body image.")

    #invalid input
    else:
        print("INVALID INPUT")
        clear()
        start()

def Question6():
   #Story
   clear()
   print("You pick up working out, you make sure to keep is as a hobby that benefits your health and not let it take over your life.\n")
 
   #Question 3
   a6 = input("Do you point out the issues in your life, so you can improve yourself?")
 
   #input Y
   if a6 == "Y":
       Question7()
 
   #input N
   elif a6 == "N":
       print("You arent as sad but you arent a great person on the inside.")
 
   #invalid input
   else:
       print("INVALID INPUT")
       clear()
       start()

def Question7():
    print("q7")

print(Question1())