info1 = open("file2.txt","w+").writelines(sorted(open("file1.txt", "r+").readlines()))