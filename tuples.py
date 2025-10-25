import sys
import timeit

mytuples = ("Max", 28, "Boston")
print(mytuples)

mytuples2 = ('a','p','p','l','e')
print(len(mytuples2))
print(mytuples2.count('p'))
print(mytuples2.index('l'))

mylist = list(mytuples)
print(mylist)

mytuples3=tuple(mylist)
print(mytuples3)

name, age, city = mytuples
print(name, age, city)

mytuples4 = (0,1,2,3,4,5)
i1, *i2, i3 = mytuples4
print(i1)
print(i2)
print(i3)

my_list = [0,1,2, "hello", True]
my_tuple=(0,1,2,"hello",True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=100000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=100000))