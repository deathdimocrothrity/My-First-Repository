#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
__author__ = 'DDM'
dividend=input("Enter the number:")
int_dividend=int(dividend)
listofdivisor=[]
divisor=1
while divisor<=int_dividend:
    if int_dividend % divisor==0:
        listofdivisor.append(divisor)
    divisor+=1
print(listofdivisor)