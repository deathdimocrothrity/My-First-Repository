#https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import random
number=int(input("input a number:"))
list=[2, 4, 6, 8, 10]
#list=[random.randint(1,100)for i in range(random.randint(1,15))]
list.sort()
list1=list
print(list)
#element search
def element_search(list1,Number):
    for i in list1:
        if i==Number:
            return True
    return False
print(element_search(list1,number))

#binary search
listlen=0
def binary_search(listlen,list1,Number):
    while list1!=[]:
        listlen=0
        for i in list:
            listlen+=1
        midian=int(listlen/2)
        if listlen==1:
            if number==list1[midian]:
                return True
            else:
                return False
        if list1[midian]==Number:
            return True
        elif list1[midian]>Number:
            for i in range(1,1+listlen-midian):
                list1.pop(midian)
                print(list1)
        elif list1[midian]<Number:
            while midian>0:
                list1.pop(midian)
                midian-=1
                print(list1)
    return False
print(binary_search(listlen,list1,number))