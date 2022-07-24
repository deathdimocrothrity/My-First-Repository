#https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
__author__ = 'DDM'
#M1
print("The author is",  __author__,"! (.^-^.)")
length=int(input("how many Fibonnaci numbers to generate(>2):"))
Fseqence=[1,1,]
Lnumber=2
while Lnumber<length:
    Fseqence.append(Fseqence[Lnumber-1]+Fseqence[Lnumber-2])
    Lnumber+=1
print(Fseqence)
#M2
length=int(input("how many Fibonnaci numbers to generate(>2):"))
a=1
b=1
Lnumber=2
print(a, end=', ')
print(b, end=', ')
while Lnumber<length:
    c=a+b
    print(c, end=', ')
    a=b
    b=c
    Lnumber+=1
