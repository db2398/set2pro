bhavi=input()
yaki=map(int,input().split())
sin=[]
for i in yaki:
    eat=bin(i)
    sin.append(eat)
fine=sorted(sin)
fine.reverse()
for j in fine:
    print(int(j,2))
