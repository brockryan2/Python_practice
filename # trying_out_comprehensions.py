# trying_out_comprehensions

from pprint import pprint as pp

from math import factorial, sqrt

# list comprehension

#Example 1
words = "here are some words".split()
pp([len(word) for word in words])

def multiply(i):
  i *= 3
  return i


a = "abc"
b = [multiply(x) for x in a]
c = ""
for z in b:
  c += (z + " ")

pp(c)

# Example 2
def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True


print([multiply(x) for x in range(101) if is_prime(x)])


# Set comprehension

set_comprehension_example = {len(str(factorial(x))) for x in range(20)}

pp(set_comprehension_example)


# dictionary comprehension

country_to_capital = {"United States": "Washington D.C.",
                      "Canada": "Ottawa",
                      "Mexico": "Mexico City"
                     }

capital_to_country = {capital: country for country, capital in country_to_capital.items()}

pp(capital_to_country)
