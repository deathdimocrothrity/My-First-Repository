#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
__author__ = 'DDM'
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in b:
    if i< 5: 
        print(i)
#extra 1
newlist=[]
for i in b: 
    if i< 5: newlist.append(i)
    
print(newlist)

#extra 2
temp=[ x for x in b if x<5 ]
print(type(temp))
print( [ x for x in b if x<5 ] )
#extra 3
y=input("enter the number:")
inty=int(y)
newlist2=[]
for i in b: 
    if i< inty: newlist2.append(i)
    
print(newlist2)