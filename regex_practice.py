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


"""The dot (.) metacharacter specifies a wildcard. It matches any single character except a newline:"""
p = re.search('foo.bar', 'fooxbar')
print(p) # returns: <_sre.SRE_Match object; span=(0, 7), match='fooxbar'>

print(re.search('foo.bar', 'foobar')) # prints None
print(re.search('foo.bar', 'foo\nbar')) # prints None

"""\w matches any alphanumeric character. It's essentially shorthand for [a-zA-Z0-9_] """
print(re.search('\w', '#(.a$@&')) # prints <_sre.SRE_Match object; span=(3, 4), match='a'>

"""/W (capital W) does the opposite, it matches any non-word character.  It is equivalent to [^a-zA-Z0-9_] """
print(re.search('\W', 'a_1*3Qb')) #prints <_sre.SRE_Match object; span=(3, 4), match='*'>

""" \d mathces any decimal digit character. \D is the opposite: matches any character that is not a decimal digit"""
print(re.search('\d', 'abc4def')) # prints <_sre.SRE_Match object; span=(3, 4), match='4'>
print(re.search('\D', '234Q678')) # prints <_sre.SRE_Match object; span=(3, 4), match='Q'>

"""/s matches any whitespace character (space, tab, newline, return). /S does the opposite, matching any non-whitespace character"""
print(re.search('\s', 'foo\nbar baz'))  #prints <_sre.SRE_Match object; span=(3, 4), match='\n'>
print(re.search('\S', '  \n foo  \n  ')) #prints <_sre.SRE_Match object; span=(4, 5), match='f'>

"""The above character class sequences \w, \W, \d, \D, \s, and \S can appear inside a square bracket character class as well:"""
print(re.search('[\d\w\s]', '---3---')) # prints <_sre.SRE_Match object; span=(3, 4), match='3'>
print(re.search('[\d\w\s]', '---a---')) # prints <_sre.SRE_Match object; span=(3, 4), match='a'>
print(re.search('[\d\w\s]', '--- ---')) # prints <_sre.SRE_Match object; span=(3, 4), match=' '>


"""backslash (\) Removes the special meaning of a metacharacter."""
print(re.search('.', 'foo.bar')) # prints <_sre.SRE_Match object; span=(0, 1), match='f'>
print(re.search('\.', 'foo.bar')) # prints <_sre.SRE_Match object; span=(3, 4), match='.'>


"""Specifying a backslash literal in a regex is a bit cumbersome. You cannot specify it with the regular escape character (e.g. '\\')
at least not directly. Doing so results in a sre_constants.error Error. The problem here is that the backslash escaping happens twice,
first by the Python interpreter on the string literal and then again by the regex parser on the regex it receives.

Here’s the sequence of events:
    1) The Python interpreter is the first to process the string literal '\\'. It interprets that as an escaped backslash and passes only
       a single backslash to re.search().

    2) The regex parser receives just a single backslash, which isn’t a meaningful regex, so the messy error ensues.


There are two ways around this. First, you can escape both backslashes in the original string literal:
#####################################################
# >>> re.search('\\\\', s)                          #
# <_sre.SRE_Match object; span=(3, 4), match='\\'>  #
#                                                   #
#####################################################


The second, and probably cleaner, way to handle this is to specify the <regex> using a raw string:
#####################################################
# >>> re.search(r'\\', s)                           #
# <_sre.SRE_Match object; span=(3, 4), match='\\'>  #
#                                                   #
#####################################################

This suppresses the escaping at the interpreter level. The string '\\' gets passed unchanged to the regex parser, which again sees one escaped backslash as desired.

It’s good practice to use a raw string to specify a regex in Python whenever it contains backslashes. """


"""
## Anchors ##

Anchors are zero-width matches. They don’t match any actual characters in the search string, and they don’t
consume any of the search string during parsing. Instead, an anchor dictates a particular location in the
search string where a match must occur.

^ and \A ==> Anchor a match to the start of <string>

When the regex parser encounters ^ or \A, the parser’s current position must be at the beginning of the search
string for it to find a match. In other words, regex ^foo stipulates that 'foo' must be present not just any
place in the search string, but at the beginning:

>>> re.search('^foo', 'foobar')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> print(re.search('^foo', 'barfoo'))
None


\A functions similarly:

>>> re.search('\Afoo', 'foobar')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> print(re.search('\Afoo', 'barfoo'))
None

^ and \A behave slightly differently from each other in MULTILINE mode. You’ll learn more about MULTILINE mode
below in the section on flags.


$ and \Z ==> Anchor a match to the end of <string>.

When the regex parser encounters $ or \Z, the parser’s current position must be at the end of the search string
for it to find a match. Whatever precedes $ or \Z must constitute the end of the search string:

>>> re.search('bar$', 'foobar')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
>>> print(re.search('bar$', 'barfoo'))
None

>>> re.search('bar\Z', 'foobar')
<_sre.SRE_Match object; span=(3, 6), match='bar'>
>>> print(re.search('bar\Z', 'barfoo'))
None


As a special case, $ (but not \Z) also matches just before a single newline at the end of the search string:

>>> re.search('bar$', 'foobar\n')
<_sre.SRE_Match object; span=(3, 6), match='bar'>


In this example, 'bar' isn’t technically at the end of the search string because it’s followed by one additional
newline character. But the regex parser lets it slide and calls it a match anyway. This exception doesn’t apply to \Z.

$ and \Z behave slightly differently from each other in MULTILINE mode. See the section below on flags for more
information on MULTILINE mode.

\b ==> Anchors a match to a word boundary. Asserts that the regex parser’s current position must be at the beginning
or end of a word. A word consists of a sequence of alphanumeric characters or underscores ([a-zA-Z0-9_]), the same as
for the \w character class:

>>> re.search(r'\bbar', 'foo bar')
<_sre.SRE_Match object; span=(4, 7), match='bar'>
>>> re.search(r'\bbar', 'foo.bar')
<_sre.SRE_Match object; span=(4, 7), match='bar'>

>>> print(re.search(r'\bbar', 'foobar'))
None

>>> re.search(r'foo\b', 'foo bar')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.search(r'foo\b', 'foo.bar')
<_sre.SRE_Match object; span=(0, 3), match='foo'>

>>> print(re.search(r'foo\b', 'foobar'))
None


In the above examples, a match happens on lines 1 and 3 because there’s a word boundary at the start of 'bar'. This isn’t
the case on line 6, so the match fails there. Similarly, there are matches on lines 9 and 11 because a word boundary exists
at the end of 'foo', but not on line 14. Using the \b anchor on both ends of the <regex> will cause it to match when it’s
present in the search string as a whole word:

>>> re.search(r'\bbar\b', 'foo bar baz')
<_sre.SRE_Match object; span=(4, 7), match='bar'>
>>> re.search(r'\bbar\b', 'foo(bar)baz')
<_sre.SRE_Match object; span=(4, 7), match='bar'>

>>> print(re.search(r'\bbar\b', 'foobarbaz'))
None


This is another instance in which it pays to specify the <regex> as a raw string, as the above examples have done.

Because '\b' is an escape sequence for both string literals and regexes in Python, each use above would need to be double
escaped as '\\b' if you didn’t use raw strings. That wouldn’t be the end of the world, but raw strings are tidier.

\B ==> Anchors a match to a location that isn’t a word boundary. Does the opposite of \b. It asserts that the regex
parser’s current position must not be at the start or end of a word:

>>> print(re.search(r'\Bfoo\B', 'foo'))
None
>>> print(re.search(r'\Bfoo\B', '.foo.'))
None

>>> re.search(r'\Bfoo\B', 'barfoobaz')
<_sre.SRE_Match object; span=(3, 6), match='foo'>


In this case, a match happens on line 7 because no word boundary exists at the start or end of 'foo' in
the search string 'barfoobaz'. """


"""
## Quantifiers ##

A quantifier metacharacter immediately follows a portion of a <regex> and indicates how many times that
portion must occur for the match to succeed.

*

Matches zero or more repetitions of the preceding regex.

For example, a* matches zero or more 'a' characters. That means it would match an empty string, 'a', 'aa', 'aaa', and so on.

Consider these examples:

>>> re.search('foo-*bar', 'foobar')                     # Zero dashes
<_sre.SRE_Match object; span=(0, 6), match='foobar'>

>>> re.search('foo-*bar', 'foo-bar')                    # One dash
<_sre.SRE_Match object; span=(0, 7), match='foo-bar'>

>>> re.search('foo-*bar', 'foo--bar')                   # Two dashes
<_sre.SRE_Match object; span=(0, 8), match='foo--bar'>


On line 1, there are zero '-' characters between 'foo' and 'bar'. On line 3 there’s one, and on line 5 there are two.
The metacharacter sequence -* matches in all three cases.

You’ll probably encounter the regex .* in a Python program at some point. This matches zero or more occurrences of
any character. In other words, it essentially matches any character sequence up to a line break.
(Remember that the . wildcard metacharacter doesn’t match a newline.)

In this example, .* matches everything between 'foo' and 'bar':

>>> re.search('foo.*bar', '# foo $qux@grault % bar #')
<_sre.SRE_Match object; span=(2, 23), match='foo $qux@grault % bar'>


Did you notice the span= and match= information contained in the match object?

Until now, the regexes in the examples you’ve seen have specified matches of predictable length. Once you start using
quantifiers like *, the number of characters matched can be quite variable, and the information in the match object
becomes more useful.

You’ll learn more about how to access the information stored in a match object in the next tutorial in the series.

+ ==> Matches one or more repetitions of the preceding regex.

This is similar to *, but the quantified regex must occur at least once:

>>> print(re.search('foo-+bar', 'foobar'))              # Zero dashes
None
>>> re.search('foo-+bar', 'foo-bar')                    # One dash
<_sre.SRE_Match object; span=(0, 7), match='foo-bar'>

>>> re.search('foo-+bar', 'foo--bar')                   # Two dashes
<_sre.SRE_Match object; span=(0, 8), match='foo--bar'>


Remember from above that foo-*bar matched the string 'foobar' because the * metacharacter allows for zero occurrences
of '-'. The + metacharacter, on the other hand, requires at least one occurrence of '-'. That means there isn’t a
match on line 1 in this case.

? ==> Matches zero or one repetitions of the preceding regex.

Again, this is similar to * and +, but in this case there’s only a match if the preceding regex occurs once or not at all:

>>> re.search('foo-?bar', 'foobar')                     # Zero dashes
<_sre.SRE_Match object; span=(0, 6), match='foobar'>

>>> re.search('foo-?bar', 'foo-bar')                    # One dash
<_sre.SRE_Match object; span=(0, 7), match='foo-bar'>

>>> print(re.search('foo-?bar', 'foo--bar'))            # Two dashes
None


In this example, there are matches on lines 1 and 3. But on line 5, where there are two '-' characters, the match fails.

Here are some more examples showing the use of all three quantifier metacharacters:

>>> re.match('foo[1-9]*bar', 'foobar')
<_sre.SRE_Match object; span=(0, 6), match='foobar'>

>>> re.match('foo[1-9]*bar', 'foo42bar')
<_sre.SRE_Match object; span=(0, 8), match='foo42bar'>

>>> print(re.match('foo[1-9]+bar', 'foobar'))
None

>>> re.match('foo[1-9]+bar', 'foo42bar')
<_sre.SRE_Match object; span=(0, 8), match='foo42bar'>

>>> re.match('foo[1-9]?bar', 'foobar')
<_sre.SRE_Match object; span=(0, 6), match='foobar'>

>>> print(re.match('foo[1-9]?bar', 'foo42bar'))
None


This time, the quantified regex is the character class [0-9] instead of the simple character '-'.

*?  and  +?  and  ?? ==> The non-greedy (or lazy) versions of the *, +, and ? quantifiers.

When used alone, the quantifier metacharacters *, +, and ? are all greedy,
meaning they produce the longest possible match. Consider this example:

>>> re.search('<.*>', '%<foo> <bar> <baz>%')
<_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>

The regex <.*> effectively means:

A '<' character
Then any sequence of characters
Then a '>' character
But which '>' character? There are three possibilities:

The one just after 'foo'
The one just after 'bar'
The one just after 'baz'

Since the * metacharacter is greedy, it dictates the longest possible match, which includes everything
up to and including the '>' character that follows 'baz'. You can see from the match object that this
is the match produced.  If you want the shortest possible match instead,
then use the non-greedy metacharacter sequence *?:

>>> re.search('<.*?>', '%<foo> <bar> <baz>%')
<_sre.SRE_Match object; span=(1, 6), match='<foo>'>

In this case, the match ends with the '>' character following 'foo'.

Note: You could accomplish the same thing with the regex <[^>]*>, which means:

A '<' character
Then any sequence of characters other than '>'
Then a '>' character

This is the only option available with some older parsers that don’t support lazy quantifiers.
Happily, that’s not the case with the regex parser in Python’s re module.

There are lazy versions of the + and ? quantifiers as well:

>>> re.search('<.+>', '%<foo> <bar> <baz>%')
<_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>

>>> re.search('<.+?>', '%<foo> <bar> <baz>%')
<_sre.SRE_Match object; span=(1, 6), match='<foo>'>

>>> re.search('ba?', 'baaaa')
<_sre.SRE_Match object; span=(0, 2), match='ba'>

>>> re.search('ba??', 'baaaa')
<_sre.SRE_Match object; span=(0, 1), match='b'>


The first two examples on lines 1 and 3 are similar to the examples shown above, only using + and +? instead of * and *?.

The last examples on lines 6 and 8 are a little different.

In general, the ? metacharacter matches zero or one occurrences of the preceding regex.
The greedy version, ?, matches one occurrence, so ba? matches 'b' followed by a single 'a'.
The non-greedy version, ??, matches zero occurrences, so ba?? matches just 'b'.

{m} ==> Matches exactly m repetitions of the preceding regex.

This is similar to * or +, but it specifies exactly how many times the preceding regex
must occur for a match to succeed:

>>> print(re.search('x-{3}x', 'x--x'))                # Two dashes
None

>>> re.search('x-{3}x', 'x---x')                      # Three dashes
<_sre.SRE_Match object; span=(0, 5), match='x---x'>

>>> print(re.search('x-{3}x', 'x----x'))              # Four dashes
None


Here, x-{3}x matches 'x', followed by exactly three instances of the '-' character, followed by another 'x'.
The match fails when there are fewer or more than three dashes between the 'x' characters.

{m,n} ==> Matches any number of repetitions of the preceding regex from m to n, inclusive.

In the following example, the quantified <regex> is -{2,4}. The match succeeds when there are two, three, or
four dashes between the 'x' characters but fails otherwise:

>>> for i in range(1, 6):
...     s = f"x{'-' * i}x"
...     print(f'{i}  {s:10}', re.search('x-{2,4}x', s))
...
1  x-x        None
2  x--x       <_sre.SRE_Match object; span=(0, 4), match='x--x'>
3  x---x      <_sre.SRE_Match object; span=(0, 5), match='x---x'>
4  x----x     <_sre.SRE_Match object; span=(0, 6), match='x----x'>
5  x-----x    None


Omitting m implies a lower bound of 0, and omitting n implies an unlimited upper bound:

##############################################################################
#  Reg. Ex.    |               Matches                  |   Identical to     #
# ========================================================================== #
# <regex>{,n}  |  Any number of repetitions of <regex>  |   <regex>{0,n}     #
#              |    less than or equal to n             |                    #
# -------------------------------------------------------------------------- #
# <regex>{m,}  |  Any number of repetitions of <regex>  |     ----           #
#              |    greater than or equal to m          |                    #
# -------------------------------------------------------------------------- #
# <regex>{,}   |  Any number of repetitions of <regex>  |   <regex>{0,}      #
#              |                                        |    <regex>*        #
##############################################################################


If you omit all of m, n, and the comma, then the curly braces no longer function as
metacharacters. {} matches just the literal string '{}':

>>> re.search('x{}y', 'x{}y')
<_sre.SRE_Match object; span=(0, 4), match='x{}y'>


In fact, to have any special meaning, a sequence with curly braces must fit one of the following patterns in which m and n are nonnegative integers:

{m,n}
{m,}
{,n}
{,}

Otherwise, it matches literally:

>>> re.search('x{foo}y', 'x{foo}y')
<_sre.SRE_Match object; span=(0, 7), match='x{foo}y'>

>>> re.search('x{a:b}y', 'x{a:b}y')
<_sre.SRE_Match object; span=(0, 7), match='x{a:b}y'>

>>> re.search('x{1,3,5}y', 'x{1,3,5}y')
<_sre.SRE_Match object; span=(0, 9), match='x{1,3,5}y'>

>>> re.search('x{foo,bar}y', 'x{foo,bar}y')
<_sre.SRE_Match object; span=(0, 11), match='x{foo,bar}y'>


Later in this tutorial, when you learn about the DEBUG flag, you’ll see how you can confirm this.

{m,n}?  ==> The non-greedy (lazy) version of {m,n}.

{m,n} will match as many characters as possible, and {m,n}? will match as few as possible:

>>> re.search('a{3,5}', 'aaaaaaaa')
<_sre.SRE_Match object; span=(0, 5), match='aaaaa'>

>>> re.search('a{3,5}?', 'aaaaaaaa')
<_sre.SRE_Match object; span=(0, 3), match='aaa'>


In this case, a{3,5} produces the longest possible match, so it matches five 'a' characters. a{3,5}? produces the shortest match, so it matches three.
"""

