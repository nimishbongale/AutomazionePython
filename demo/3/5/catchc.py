info = open("original_text.txt", "r+").readlines()
c=0
for i in range(len(info)):
    for j in info[i].split():
        for k in j:
            c=c+k.count('c')
print(c)