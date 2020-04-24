#default_dict_examples


dict_a = {}
#dict_a['missing_key']  # raises KeyError

dict_a.setdefault('missing_key', 'default value')
dict_a['missing_key']

"""
if you call .setdefault() on an existing key, then
the call won’t have any effect. Your key will hold
the original value instead of the new default value.
"""
dict_a.setdefault('missing_key', 'another default')
print(dict_a)


#On the other hand, if you use .get():
dict_b = {}
z = dict_b.get('missing_key', 'default value') #default value specified (optional, default= None)

#then you can code something like this:
print(z) # returns default value,
print(dict_b) # but default value is NOT added to the dictionary

"""
You can also use conditional statements to handle missing keys
in dictionaries. Below example, uses the key in dict idiom: """
a_dict = {}

if 'key' in a_dict:

  # Do something with 'key'
  a_dict['key']

else:
  a_dict['key'] = 'default value'

print(a_dict)


"""
You can also get around the KeyError by using a try and except block
to handle the exception.:"""
b_dict = {}
try:
     # Do something with 'key'
     b_dict['key']

except KeyError:
  b_dict['key'] = 'default value'

print(b_dict)



"""Alternatively, you can use the defaultdict type"""
from collections import defaultdict

# Correct instantiation
def_dict = defaultdict(list)  # Pass list to .default_factory

def_dict['one'] = 1  # Add a key-value pair

def_dict['missing']  # Access a missing key returns an empty list
[]

def_dict['another_missing'].append(4)  # Modify a missing key
def_dict

"""
You must pass a valid callable object, so remember not to call it
using the parentheses at initialization time. This is a common issue
example: """

# Wrong instantiation
def_dict = defaultdict(list()) #


"""
Sometimes, you’ll use a mutable built-in collection (a list, dict, or set)
as values in your Python dictionaries. In these cases, you’ll need to init-
ialize the keys before first use, or you’ll get a KeyError. You can either
do this process manually or automate it using a Python defaultdict. In this
section, you’ll learn how to use the Python defaultdict type for solving
some common programming problems:

Grouping the items in a collection
Counting the items in a collection
Accumulating the values in a collection

You’ll be covering some examples that use list, set, int, and float to per-
form grouping, counting, & accumulating operations in an efficient way.

Grouping Items
A typical use of the Python defaultdict type is to set .default_factory to
list and then build a dictionary that maps keys to lists of values.
With this defaultdict, if you try to get access to any missing key, then
the dictionary runs the following steps:

  Call list() to create a new empty list
  Insert the empty list into the dictionary using the missing key as key
  Return a reference to that list

This allows you to write code like this:"""
dd = defaultdict(list)
dd['key'].append(1)
dd # prints: defaultdict(<class 'list'>, {'key': [1]})

dd['key'].append(2)
dd # prints: defaultdict(<class 'list'>, {'key': [1, 2]})

dd['key'].append(3)
dd # prints: defaultdict(<class 'list'>, {'key': [1, 2, 3]})

"""
You can use defaultdict along with list to group the items in a sequence
or a collection. Suppose that you’ve retrieved the following data from
your company’s database:

Department  Employee Name
Sales         John Doe
Sales         Martin Smith
Accounting    Jane Doe
Marketing     Elizabeth Smith
Marketing     Adam Doe

With this data, you create an initial list of tuple objects
like the following:"""
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]
"""
Now, you need to create a dictionary that groups the employees
by department. To do this, you can use a defaultdict as follows:"""
dep_dd = defaultdict(list)

for department, employee in dep:
    dep_dd[department].append(employee)

"""
Here, you create a defaultdict called dep_dd and use a for loop
to iterate through your dep list.
The statement dep_dd[department].append(employee) creates the keys
for the departments, initializes them to an empty list, and then
appends the employees to each department. Once you run this code,
your dep_dd will look something like this:

defaultdict(<class 'list'>, {'Sales': ['John Doe', 'Martin Smith'],
                             'Accounting' : ['Jane Doe'],
                             'Marketing': ['Elizabeth Smith', 'Adam Doe']})


Counting Items
If you set .default_factory to int, then your defaultdict will be
useful for counting the items in a sequence or collection. When you
call int() with no arguments, the function returns 0, which is the
typical value you’d use to initialize a counter.

To continue with the example of the company database, suppose you
want to build a dictionary that counts the number of employees per
department. In this case, you can code something like this: """

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

dd = defaultdict(int) # calling int() with no argument returns 0

for department, _ in dep:
    dd[department] += 1

dd # prints: defaultdict(<class 'int'>, {'Sales': 2, 'Accounting': 1, 'Marketing': 2})

"""
Another example of counting items is the mississippi example,
where you count the number of times each letter in a word is
repeated. Take a look at the following code: """
s = 'mississippi'
dd = defaultdict(int)

for letter in s:
    dd[letter] += 1


"""
As counting is a relatively common task in programming,
the Python dictionary-like class collections.Counter is
specially designed for counting items in a sequence.
With Counter, you can re-write the above mississippi
example as follows:"""
counter = Counter('mississippi')
print(counter) # prints: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


"""
Accumulating Values
Sometimes you’ll need to calculate the total sum of the
values in a sequence or collection. Let’s say you have
the following Excel sheet with data about the sales of
your Python website:

Products  July      August    September
Books     1250.00   1300.00   1420.00
Tutorials  560.00    630.00    750.00
Courses   2500.00   2430.00   2750.00

Next, you process the data using Python and get the
following list of tuple objects: """
incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

"""
With this data, you want to calculate the total income
per product. To do that, you can use a Python defaultdict
w/ float as .default_factory; something like this: """
dd = defaultdict(float)

for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')
