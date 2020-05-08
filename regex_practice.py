#regex_practice

import re

#match an exact string
a = re.search('123', 'foo123bar')
print(a)

#match a single character from a list of options
b = re.search('ba[artz]', 'foobarqux') # matches any single instance of 'a', 'r', 't', or 'z'
print(b)
c = re.search('ba[artz]', 'foobarqux')
print(b)

# match a single character in a range
d = re.search('[a-z]', 'FOObar') #matches the first lowercase letter
print(d)

e = re.search('[0-9]', 'foo123bar') #mathces on '1'
print(e)

f = re.search('[0-9][0-9]', 'foo123bar') #matches on '12'
print(f)

g = re.search('[0-9a-fA-f]', '--- a0 ---') # matches first hexadecimal character
print(g)


h = re.search('[^0-9]', '12345foo') # matches first instance of string that is NOT in the set[0-9]
#this only works if '^' is the first character in the regelar expresssion, otherwise it matches the '^' literal
print(h)

"""As you’ve seen, you can specify a range of characters in a character class by separating characters with a hyphen. What if you want the character class to include a literal hyphen character? You can place it as the first or last character or escape it with a backslash ('\''):"""
i = re.search('[-abc]', '123-456')# matches '-'
j = re.search('[abc-]', '123-456')# matches '-'
k = re.search('[ab\-c]', '123-456')# matches '-'
print(i,j,k)

"""If you want to include a literal ']' in a character class, then
you can place it as the first character or escape it with backslash:"""
l = re.search('[]]', 'foo[1]')
m = re.search('[ab\]cd]', 'foo[1]')
print(l,m)

#Other regex metacharacters lose their special meaning inside a character class:
n = re.search('[)*+|]', '123*456')
o = re.search('[)*+|]', '123+456')
print(n,o)

"""As you saw in the table above, * and + have special meanings in a regex in Python
They designate repetition, which you’ll learn more about shortly. But in this example,
they’re inside a character class, so they match themselves literally."""
