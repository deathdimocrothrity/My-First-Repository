import random
Entercode=1
while Entercode==1:
    try:
        len_packets=int(input("Enter the number of packets:"))
    except:
        print("Please Enter a number")
        Entercode=1
    else:
        if len_packets>500000:
            print("Enter a number less than 500000")
            Entercode=1
        else:
            Entercode=0
while Entercode==0:
    try:
        len_channels=int(input("Enter the number of channels:"))
    except:
        print("Please input a number")
        Entercode=0
    else:
        if len_channels>len_packets:
            print("Enter a number less than the number of packets")
            Entercode=0
        else:
            Entercode=1
packets=random.sample(range(1, 1000000000), len_packets)
def sort():
    x=packets[0]
    for i in packets:
        if x >i:
            packets.insert(1, i)
            packets.remove(i)
        elif x<i:
            x=packets[i]
print("you got",len_packets,"packets,they are",packets,". And you got",len_channels,"channels. ")
single_p_quality=0
mult_p=len_packets-len_channels
for i in packets[mult_p:]:
    single_p_quality+=i
if mult_p%2==1:
    quality=single_p_quality+packets[int(mult_p-1/2)]
elif mult_p%2==0:
    quality=single_p_quality+(packets[int(mult_p/2)]+packets[int(mult_p/2-1)])/2
print(quality)