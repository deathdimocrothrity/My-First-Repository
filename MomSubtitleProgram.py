File="MomSubtitleFile"#input("Enter File Name:")
f = open(File+".txt", "r+")
for line in f:
    Flist=line.split("\t")
    mytime=Flist[0]
    inttime=float(mytime)
    H=inttime//3600
    M=(inttime-H*3600)//60
    S=inttime-H*3600-M*60
    S=round(S,0)
    FinalTime=("%02d:%02d:%02d" % (H, M, S))
    
    

