list=["apple","bannana","cherries","papaya"]
print(list)
x=type(list)
print(x)
print(list[1])
print(list[2])
list[0]="jackfruit"
print(list)
for x in list:
    print(x)

list.insert(2,"peach")
print(list)
list.pop(3)
print(list)
list.remove("jackfruit")
print(list)
