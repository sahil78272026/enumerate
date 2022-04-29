list1 = [1,3,2,False,"Sahil",65,48,94.1]

""" index = 0
for items in list1:
    print(counter , items)
    index+=1 """

for num,items in enumerate(list1): # enumerate add a counter to the iterable
    print(num,items)