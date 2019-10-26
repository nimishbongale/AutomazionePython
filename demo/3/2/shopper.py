info = open("shopper_list.txt", "r+").readlines()
sh=[]
for i in range(len(info)):
    temp=[]
    for j in info[i].split():
        temp.append(j)
    sh.append(temp)

print(sh)