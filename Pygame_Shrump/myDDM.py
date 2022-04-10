y = input("Enter your name:")
try:
    while y=="":
         print("Are you sure about that? try again(^_^)")
         y = input("Enter your name:")
finally:
    print("I got it! keep moving!")

a = input("Enter your age:")
b=int(a)
try:
    while b<0:
       print("Are you sure about that? try again(^_^)")
       a = input("Enter your age:")
finally:
    if 0<b<=10:
        print("oh,",y,", you are only",b,"!")
    if 10<b:
        print("hello,",y,", you are",b,". ")