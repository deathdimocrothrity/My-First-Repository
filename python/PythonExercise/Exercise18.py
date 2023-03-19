#https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
import random
#写流程图
#while True
#想程序
#不要把变量倒来倒去

#generate answer
answerlist=[]
for i in range(0,4):
    answerlist.append(str(random.randint(0, 9)))
answer="".join(answerlist)
print(answer)#remove test code

#Loop until userinput matches answer
userinput=""
counter=0 #how many times used
while True:
    #get userinput
    userinput=input("Enter the number:")

    #if userinput=help, print answer and break the loop and print"
    if userinput=="help":
        print(answer)
        break

    #validate userinput,check if len=4; check if is number
    #if not, input again
    while True:
        if len(userinput)==4:
            user=userinput
            try:
                user=int(userinput)#0005 will have problem
            except:
                userinput=str(input("Enter a <number>:"))
            else:
                break
        else:
            userinput=input("Enter a <4-digits> number:")

    #counter+=1
    counter=counter+1

    #check if userinput matches answer
    if userinput==answer:
        #if Yes, print("You win! The answer is",answer,"!",counter,"times is used:") and get out of loop;
        print("You win! The answer is",answer,"!",counter,"times is used:")
        break
    else:
        #if not, check cow and bull
        cows=0
        bulls=0
        testNum=0
        answerlist1=answerlist
        while testNum<4:
            if userinput[testNum] in answerlist1:
                if userinput[testNum]==answerlist1[testNum]:
                    answerlist1[testNum]=answerlist1[testNum]+" checked"
                    cows+=1
            testNum+=1
        testNum=0
        while testNum<4:
            if userinput[testNum] in answerlist1:
                if userinput[testNum]==answerlist1[testNum]:
                    answerlist1[answerlist1.index(userinput[1])]=answerlist1[answerlist1.index(userinput[1])]+" checked"
                    bulls+=1
            testNum+=1
        print(cows,"cows",", ",bulls,"bulls  ",counter)

#print exit massage
print("game over")


"""import random
def CandB(userinput, answer,answerlist):
    #validate userinput,check if len=4; check if is number
    #if not, input again
    while True:
        if len(userinput)==4:
            #if userinput=help, print answer and break the loop and print"
            if userinput=="help":
                return answer
            else:
                try:
                    user=int(userinput)#0005 will have problem
                except:
                    userinput=str(input("Enter a 4-digits <number>:"))
                else:
                    break
        else:
            userinput=input("Enter a <4-digits> number:")

    if userinput!=answer:
        #if not, check cow and bull
        cows=0
        bulls=0
        testNum=0
        answerlist1=answerlist
        while testNum<4:
            if userinput[testNum] in answerlist1:
                if userinput[testNum]==answerlist1[testNum]:
                    answerlist1[testNum]=answerlist1[testNum]+" checked"
                    cows+=1
            testNum+=1
        testNum=0
        while testNum<4:
            if userinput[testNum] in answerlist1:
                if userinput[testNum]==answerlist1[testNum]:
                    answerlist1[answerlist1.index(userinput[1])]=answerlist1[answerlist1.index(userinput[1])]+" checked"
                    bulls+=1
            testNum+=1
        return cows, bulls




#generate answer
answerlist=[]
for i in range(0,4):
    answerlist.append(str(random.randint(0, 9)))
answer="".join(answerlist)
print(answer)#remove test code

#Loop until userinput matches answer
userinput=""
counter=0 #how many times used
while True:
    #get userinput
    userinput=input("Enter the number:")

    #check if userinput matches answer
    if userinput==answer:
        #if Yes, print("You win! The answer is",answer,"!",counter,"times is used:") and get out of loop;
        print("You win! The answer is",answer,"!",counter,"times is used:")
        break
    result=CandB(userinput, answer,answerlist)
    
    #counter+=1
    counter=counter+1

    if type(result)==str:
        print(result)
    else:
        print(result[0],"cows",", ",result[1],"bulls  ",counter)

#print exit massage
print("game over")"""