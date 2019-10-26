info = open("count.txt", "r+").readlines()
c={}
for i in range(len(info)):
    for j in info[i].split():
        for k in j:
            c[k]=c.get(k,0)+1

print(c)