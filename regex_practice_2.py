#regex_practice_2

import re

test_string = r'http://www.google.com/maps/@34.0932316,-84.1839186,15z'

reg_ex = r'^(?P<protocol>http[s]{0,1}://)(?P<subdomain>\w+)\.(?P<domain>\w+)\.(?P<tld>\w+)'

r = r'(?P<username>\w+)@(?P<domain>\w+)\.(?P<tld>\w+)'

s = re.search(reg_ex, test_string)

if s:
  print(s.groups())

else: print(None)

test_email = r'someone@something.com'

t = re.search(r, test_email)

print(t.groups())
