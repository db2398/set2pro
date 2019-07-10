sbhav,psen = input().split()
psen = int(sen)
fake = False
ben = list(map(int,input().split()))
for i in range(len(ben)):
    for j in range(len(ben)):
        if ben[i]+ben[j] == psen:
            fake = True
print("yes" if fake else "no")
