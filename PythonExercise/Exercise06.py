#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import math
a=0
My_string=input("Enter the string:")
stringlen=math.ceil(len(My_string)/2)

while a < stringlen and My_string[a] == My_string[-a-1]:
    #print(My_string[a],My_string[-a-1])
    if My_string[a] != My_string[-a-1]:
        break
    a+=1
if a >= stringlen:
    print("This is a palindrome(.^-^.)")
elif a < stringlen:
    print("This is not a palindrome(.>_<.)")
