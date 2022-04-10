#https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
__author__ = 'DDM'
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
resultlist1=[]
for i in a:
   if i in b:
       resultlist1.append(i)

#extra 1
import random
twin1=[random.randint(0,50)for i in range(1,20)]
twin2=[random.randint(0,50)for i in range(1,20)]
print("twin1=",twin1)
print("twin2=",twin2)
resultlist2=[]
if len(twin1)>len(twin2):
    for i in twin2:
        if i in twin1:
            resultlist2.append(i)
else:
    for i in twin1:
        if i in twin2:
            resultlist2.append(i)
print(resultlist2)

#extra 2

print( [i for i in b if i in a] )
