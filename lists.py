mylists = ["banana", "cherry", "apple"]
print(mylists)

mylists2 = list()
print(mylists2)

mylists3 = [5, "apple", True, "apple"]
print(mylists3)

item = mylists3[-1]
print(item)

for i in mylists3:
    print(i)

if "banana" in mylists:
    print("yes")
else:
    print("no")

print(len(mylists3))

mylists3.append("lemon")
print(mylists3)

mylists3.insert(1, "blueberry")
print(mylists3)

item = mylists3.pop()
print(item)
print(mylists3)

mylists3.remove("apple")
print(mylists3)

mylists3.reverse()
print(mylists3)

mylists3.clear()
print(mylists3)

mylists4 = [-8, 1, 9, 6, -9 , 10 ,-16]
mylists4.sort() # new_list = sorted(mylist)
print(mylists4)

mylists5 = [0] * 5
print(mylists5)

combined_list = mylists5 + mylists4
print(combined_list)

sliced_list = combined_list[3:8] #combined_list[:8] -> staring from zero to 8, combined_list[3:] -> starting from 3 to last item, 
#combined_list[::2] -> stepping two
print(sliced_list)

list_org = ["banana", "cherry", "apple"]
list_copy = list_org # list_org[:], list_org.copy() and list(list_org) are shadow copy
list_copy.append("lemon")
print(list_copy)
print(list_org)

mylists6 = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylists6]
print(mylists6, b)