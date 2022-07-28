 filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst1=list()
a=""
for line in fh:
    a=line.split()
    lst+=a
    for i in lst:
        if i not in lst1:
            lst1.append(i)
        else:
            continue
lst1.sort()
print(lst1)