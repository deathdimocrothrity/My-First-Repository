File="MomSubtitleFile"#input("Enter File Name:")
f = open(File+".txt", "r")
finalf = open("SubtitleFinal.txt", "w")
finalf = open("SubtitleFinal.txt", "a")
for line in f:
    Flist=line.rsplit("\t")
    mytime=Flist[0]
    inttime=float(mytime)
    H=inttime//3600
    M=(inttime-H*3600)//60
    S=inttime-H*3600-M*60
    S=round(S,0)
    FinalTime=("%02d:%02d:%02d" % (H, M, S))
    mysentence=Flist[2]
    finalf.write("[")
    finalf.write(FinalTime)
    finalf.write("]")
    finalf.write(mysentence)
    finalf.write("\n")
    finalf.write("\n")
f.close()

