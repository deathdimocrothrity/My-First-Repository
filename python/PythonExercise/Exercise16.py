#https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import random
list1=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
list2=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
list3=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ]
list4=["_", "[", "]", ";", "'", ",", ".", "/", "{", "}", "+", "-", "*", "/", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "|", ":", "<", ">", "?", ]
passwordlist=[]

L1number=random.randint(4,10)#在4-10之间取一个任意整数
for i in range(1,L1number):#在list1里取L1number个整数
    passwordlist.append(list1[random.randint(0,25)])#随机取数
L2number=random.randint(4,10)
for i in range(1,L2number):
    passwordlist.append(list2[random.randint(0,25)])
L3number=random.randint(4,10)
for i in range(1,L3number):
    passwordlist.append(list3[random.randint(0,9)])
L4number=random.randint(4,10)
for i in range(1,L4number):
    passwordlist.append(list4[random.randint(0,30)])
#print(passwordlist)
random.shuffle(passwordlist)
password="".join(passwordlist)
print(password)