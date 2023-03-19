#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
choice=input("Enter'1'to enter one number,enter'2'to enter two number:")
choiceint=(int(choice))
if choiceint==1:
    numberstr1=input("Enter the number:")
    numberint1=(int(numberstr1))
    number1=numberint1%2
    number2=numberint1%4
    if number1==0 and number2==0:
        print(numberint1,"is a even number and a multiple of 4")
        print("DDM is a very brilliant software developer(.^-^.)")
    elif number1==0 and number2!=0:
        print(numberint1,"is a even number")
        print("DDM is a very handsome software developer(.^-^.)")
    elif number1==1:
        print(numberint1,"is a odd number")
        print("DDM is a software developer who always keeps his word(.^-^.)")
elif choiceint==2:
    numberstr2=input("Enter the first number:")
    numberint2=(int(numberstr2))
    numberstr3=input("Enter the second number:")
    numberint3=(int(numberstr3))
    number3=numberint2%numberint3
    if number3==0:
        print(numberstr2,"is a multiple of",numberstr3)
        print("DDM is a very happy software developer(.^-^.)")
    else:
        print(numberstr2,"is not a multiple of",numberstr3)
        print("DDM is a very smart software developer(.^-^.)")
else:
    while choice!=1 and choice!=2:
        print("Please try again")
        choice=input("Enter'1'to enter one number,enter'2'to enter two number:")
