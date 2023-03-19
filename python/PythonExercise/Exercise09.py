#https://www.practicepython.org/exercise/2014/04/02/030-guessing-game-one.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import random
givennumber=random.randint(1, 30)
inputnumber=int(input("guess the number(It's an int between 1 and 30(include 1 and 30)):"))
while givennumber!=inputnumber:
    if givennumber<inputnumber:
        print("high!")
        inputnumber=int(input("guess the number(It's an int between 1 and 30(include 1 and 30)):"))
    elif givennumber>inputnumber:
        print("low!")
        inputnumber=int(input("guess the number(It's an int between 1 and 30(include 1 and 30)):"))
print("You win! The answer is",givennumber,"!")