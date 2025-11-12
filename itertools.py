from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
import operator

a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))

c = [1,2,3]
perm = permutations(c)
print(list(perm))

comb = combinations(c,2)
print(list(comb))
comb = combinations_with_replacement(c,2)
print(list(comb))

acc = accumulate(c)
print(list(acc))

acc = accumulate(c, func=operator.mul)
print(list(acc))

def smaller_than_3(x):
    return x < 3

groupby_obj = groupby(c, key = smaller_than_3)
for key, value in groupby_obj:
    print(key, list(value))

for i in count(10):
    print(i)
    if i == 15:
        break

for i in repeat(1, 7):
    print(i)