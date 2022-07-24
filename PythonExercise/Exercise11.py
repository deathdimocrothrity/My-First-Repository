#https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import math
from typing import Final
inputnumber=int(input("Enter the number:"))
number=math.ceil(math.sqrt(inputnumber))
devidor=2
list=[]
finallist=[]
while number-devidor>=0:
    if inputnumber % devidor!=0:
        devidor+=1
    elif inputnumber % devidor==0:
        list.append(devidor)
        list.append(int(inputnumber/devidor))
        devidor+=1
for i in list:
    if i not in finallist:
        finallist.append(i)
if inputnumber==2:
    print(inputnumber,"is a prime number")
elif inputnumber==1:
    print(inputnumber,"is not a prime number")
elif len(finallist)!=0:
    print(inputnumber,"is not a prime number")
    print(finallist)
else:
    print(inputnumber,"is a prime number")