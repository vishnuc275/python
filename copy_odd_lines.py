f = open("drishyam.txt", "r")
list1 = []
for x in f:
    list1.append(x)
c = len(list1)
f1 = open("drishyam2.txt", "x")
for i in range(0,c,2):
    f1.write(list1[i])
f1.close()
