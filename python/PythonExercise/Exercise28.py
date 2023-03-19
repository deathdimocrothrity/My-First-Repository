#https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
N1=int(input("Enter the first number:"))
N2=int(input("Enter the second number:"))
N3=int(input("Enter the third number:"))
print("The numbers are:",N1,N2,N3)
#第一次尝逝
"""if N1>N2:
    if N1>N3:
        max=N1
    else:
        max=N3
elif N1==N2:
    if N1>N3:
        max=N1
    else:
        max=N3
elif N1<N2:
    if N2>N3:
        max=N2
    else:
        max=N3
print(max)"""
#第二次尝逝
list=[N2,N3]
biggest=N1
for i in list:
    if biggest>i:
        pass
    elif biggest<i:
        biggest=i
print("The biggest is",biggest)