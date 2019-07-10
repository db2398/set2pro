self,help=map(int,input().split())
last=list(map(int,input().split()))
lin=[]
for i in range(0,help):
     x,y=map(int,input().split())
     lin.append([x,y])
for i in range(help):
     lower=lin[i][0]
     upper=lin[i][1]
     sta=us(last[lower-1:upper])
     print(sta)
