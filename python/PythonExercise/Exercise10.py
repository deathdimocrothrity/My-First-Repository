#https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
__author__ = 'DDM'
import random
print("The author is",__author__,"! (.^-^.)")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = random.sample(range(1,30), 12)
d = random.sample(range(1,30), 16)
list1 = print([i for i in a if i in b ])
print("c =",c)
print("d =",d)
list2 = print([i for i in c if i in d ])