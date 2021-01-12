dict={"aron":"25" , "zeo":"20" , "raul" : "12" , "abhi" : "123" , "calb" : "34"}
list1=list(dict.items())
list1.sort()
print(list1)
list2=list(dict.items())
list2.sort(reverse=True)
print(list2)