#https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import random
def DDM_function():
    choose=str(input("would like to make a list by yourself? Enter Y or N: "))
    while choose!="Y"and choose!="N":
        print("Please try again")
        choose=str(input("would like to make a list by yourself? Enter Y or N: "))
    if choose=="Y":
        orinlist=("["+input("Write your list:")+"]")
        print(orinlist)
    elif choose=="N":
        orinlist=[random.randint(0,10)for i in range(1,20)]
        print(orinlist)
    resulist=[]
    for i in orinlist:
        if i not in resulist:
            resulist.append(i)
    print(resulist)
DDM_function()