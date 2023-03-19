#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import maskpass
print("Rock,Paper,Scissors")
try:
    Player1 = int(maskpass.askpass(prompt="Player1(Rock is 1,Paper is 2,Scissors are 3, enter the number):", mask="*").lower())
    Player2 = int(maskpass.askpass(prompt="Player2(Rock is 1,Paper is 2,Scissors are 3, enter the number):", mask="*").lower())
    choice=[1,2,3]
    game=["Rock","Paper","Scissors"]
    if Player1 not in game or Player2 not in game:
        print("Try again")
    print("Player1:",game[Player1-1])
    print("Player2:",game[Player2-1])
    if Player1 == Player2:
        print("It's a tie!")
    elif Player1==1 & Player2==3 or Player1==2 & Player2==1 or Player1==3 & Player2==2:
        print("The winner is Player1! ")
    else:
        print("The winner is Player2! ")
except:
    print("Try again")
