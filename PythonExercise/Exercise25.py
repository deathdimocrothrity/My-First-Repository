#https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
"""NUMBER=str(input("enter your number:"))
number=False
while number==False:
    try:
        NUMBER=int(NUMBER)
    except:
        NUMBER=str(input("enter a int:"))
    else:
        if NUMBER>100 or NUMBER<0:
            NUMBER=str(input("enter a number between 0 and 100:"))
        else:
            number=True"""
guesslow=0
guesshigh=100
guess=int((guesslow+guesshigh)/2)
print(guess)
user=str(input("too high or too low or yes:"))
while user!="yes":
    if user=="1":
        guesshigh=guess
    elif user=="2":
        guesslow=guess
    guess=int((guesslow+guesshigh)/2)
    print(guess)
    user=str(input("too high or too low or yes:"))
else:
    print("Yes! THe answer is",(guesslow+guesshigh)/2)