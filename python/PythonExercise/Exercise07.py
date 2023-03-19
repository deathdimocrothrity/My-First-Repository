#https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]