#https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
__author__ = 'DDM'
print("The author is",__author__,"! (.^-^.)")
test = "this has a lot of spaces and tabs"
indextest1=0
indextest2=0
resultlist=[]
for i in test:
    indextest1+=1
    if i == " ":
        resultlist.append(test[indextest2:indextest1-1])
        indextest2=indextest1
print(resultlist)
resultlist.append(test[indextest2:])
result=""
testindex=0
while testindex>-len(resultlist):
    testindex-=1
    result+=resultlist[testindex]+" "
print(result)