#https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
guesslow=0
guesshigh=100
guess=int((guesslow+guesshigh)/2)
print(guess)
user=str(input("too high or too low or yes:"))
while user!="Y":
    if user=="H":
        guesshigh=guess
    elif user=="L":
        guesslow=guess
    guess=int((guesslow+guesshigh)/2)
    print(guess)
    user=str(input("too high or too low or yes:"))
else:
    print("Yes! THe answer is",int((guesslow+guesshigh)/2))

"""#https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
guesslow=0
guesshigh=100
guess=int((guesslow+guesshigh)/2)
print(guess)
user=str(input("too high or too low or yes:"))
while user!="Y":
    if user=="H":
        guesshigh=guess
    elif user=="L":
        guesslow=guess
    if guesshigh-guesslow==2:
        user="Y"
    else:
        guess=int((guesslow+guesshigh)/2)
        print(guess)
        user=str(input("too high or too low or yes:"))
else:
    print("Yes! THe answer is",int((guesslow+guesshigh)/2))"""