from decimal import Decimal, ROUND_HALF_UP
import math
File="MomSubtitleFile"#input("Enter File Name:")
f = open(File+".txt", "r")
finalf = open("SubtitleFinal.txt", "w")
finalf = open("SubtitleFinal.txt", "a")
for line in f:
    Flist=line.rsplit("\t")
    mytime=Flist[0]
    inttime=float(mytime)
    M=inttime//60
    S=inttime-M*60
    S=round(S,2)
    time=("%02d:%02d" % (M,S))
    time=str(time)
    Ssplit=math.modf(S)
    Sdecimalpart=str(Decimal(Ssplit[0]).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))
    Finaltime=time+Sdecimalpart[1:4]
    print(Finaltime)
    mysentence=Flist[2]
    oneline="[{}]{} \n\n"
    finalf.write(oneline.format(Finaltime,mysentence))
f.close()

