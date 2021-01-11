print("program for merging two dictionaries")
dict1={"type":"animal" , "color":"red"}
print("dict one before merging", dict1)
dict2={"species":"lion" , "area":"forest"}
dict1.update(dict2)
print(dict1)