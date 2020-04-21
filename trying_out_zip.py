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


#unzipping
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

numbers, letters = zip(*pairs)

print(numbers)
print(letters)


#sorting with zip

letters1 = ['b', 'a', 'd', 'c']
numbers1 = [2, 4, 1, 3]

data1 = list(zip(letters1, numbers1))
data2 = list(zip(numbers1, letters1))

data1.sort()
data2.sort()

print("sorted by letter:", data1)
print("sorted by number:", data2)

# parallel sorting with zip

letters2 = ['b', 'a', 'd', 'c']
numbers2 = [2, 4, 3, 1]

data3 = sorted(zip(letters, numbers))
print(data3)


# calculating in pairs

total_sales = [52000.00, 51000.00, 48000.00]
prod_costs  = [46800.00, 45900.00, 43200.00]
total_profit = 0

for sales, costs in zip(total_sales, prod_costs):
  profit = sales - costs
  total_profit += profit
  print('profit =', profit)

print("total profit = ", total_profit)


# building dictionaries

fields = ['name', 'age', 'fav_color']
values = ['Bob', 2, 'blue']

a_dict = dict(zip(fields, values))
print(a_dict)


def custom_zip(iterable1, *args):

  if hasattr(iterable1, '__iter__'):
    for arg in args:
      if hasattr(arg, '__iter__'):
        for i in arg:

