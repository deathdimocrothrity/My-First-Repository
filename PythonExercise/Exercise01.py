#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html 
__author__ = 'DDM'
name = input("Enter your name:")

try:
    while name=="":
         print("Are you sure about that? try again(^_^)")
         name = input("Enter your name:")
finally:
    print("I got it! keep moving!")

agestr = input("Enter your age:")
ageint=int(agestr)
try:
    while ageint<0:
       print("Are you sure about that? try again(^_^)")
       agestr = input("Enter your age:")
       ageint=int(agestr)
finally:
    if 0<ageint<=10:
        print("oh,",name,", you are only",ageint,"!")
    if 10<ageint:
        print("hello,",name,", you are",ageint,". ")