info = open("phonebook.txt", "r+").readlines()
ph = {}
for i in range(len(info)):
    word = info[i].split()
    ph[word[0]]=word[1]

for i in sorted(ph.keys()):
    print(i,ph[i])