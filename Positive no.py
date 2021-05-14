list1=[12,-7,5,64,-14]
pos_nos =list(filter(lambda x: (x>=0) , list1))
print("list1=[12,-7,5,64,-14]")
print(" ",  *pos_nos)
list2=[12,14,-95,3]
pos_nos =list(filter(lambda y: (y>=0) , list2))
print("list2=[12,14,-95,3]")
print(" ",  *pos_nos)
