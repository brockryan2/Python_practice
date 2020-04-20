#trying_out_zip
from itertools import zip_longest

numbers = [1, 2, 3]
letters = ('a', 'b', 'c')

combined = zip(numbers, letters)

print(list(combined))

#passing zero arguments
a = zip()

print(list(a))

# next(a)  <-- raises StopIteration

#passing one argument
b = zip("this is an iterable")

print(b)
print(list(b))

#passing three arguments
c = zip([1,2,3], 'abc', [-9, -8, -7])

print(c)
print(list(c))

#passing arguments of unequal length
d = zip([1,2,3], 'abcd')

print(d)
print(list(d))

#passing arguments of unequal length using zip_longest
e = zip_longest([1,2,3], 'abcdef')

print(e)
print(list(e))

#traversing parallel lists

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

for i, n in zip(list1, list2):
  print("List 1 item: ", i)
  print("List 2 item: ", n)


#traversing multiple dictionaries in parallel

d1 = {1: 'red', 2: 'orange', 3: 'green'}
d2 = {'apples': 3, 'oranges': 5, 'pears': 2}

for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
  print("In basket", k1, ", there are ", v2, " ", v1, " ", k2, sep='')


