import random
randomNumber=random.randint(1, 267751)
print(randomNumber)
f=open("C:\\Users\MarkL\OneDrive\Documents\GitHub\My-First-Repository\python\PythonExercise\sowpods.txt")
a=2
i=f.readline()
while a<randomNumber:
    a+=1
    i=f.readline()
print(f.readline())