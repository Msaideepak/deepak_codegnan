'''
Regular Expression
------------------
--> This regular expression or RegEx is a sequence of characters that forms a searching pattern .
--> To use this we have to import re, which will unlock the package

Functions
---------

1.Findall --> By using this function, it will find all sequence in the string
systax--> re.findall ("metachar", variable_name)
import re
variable_name = "There is a metachar here, and another metachar over there."
results = re.findall("metachar", variable_name)
print(f"Target String: {variable_name}")
print(f"List of matches: {results}")
print(f"Total occurrences found: {len(results)}")

2.Search --> By using this functions, it will only find first sequence in the string
systax--> re.search ("metachar",variable_name)
import re
variable_name = "There is a metachar here, and another metachar over there."
match = re.search("metachar", variable_name)
if match:
    print(f"Match found: '{match.group()}'")
    print(f"Starts at index: {match.start()}")
    print(f"Ends at index: {match.end()}")
else:
    print("No match found.")


Metacharcters
-------------
--> metacharters are used to form searching pattern
--> in this method character we can search for [a-z],[A-Z],[0-9]

import re
any =  "There is a metachar here, and another metachar over there."
so = re.findall ("[]",any)
print(so)

1.[]  --> in this method character we can search for [a-z],[A-Z],[0-9]
some = "By using this function, it will only find first sequence in the string
an = re search("[a]",some)
print(an)

2.dot(.)--> this meta character will form a searching pattern as it will take any single character for(.)

import re
we = "hello"
the = re.findall("h...o",we)
thing = re.search("he..o",we)
print(the)
print(thing)

3.^  --> this is used to find the string is starting with the sequence or not
systax --> re.finall ("metachar",variable_name)

import re
how = "this is used to find the string is starting with the sequence or not"
who = re.findall("^this is",how)
then = re.search("^this" ,how)
print(who)
print(then)

4.$ --> this is used to find string is ending with the sequence or not
systax--> re.findall("$",variable_name)

import re
out = "this is used to find string is ending with the sequence or not"
one = re.findall("sequence $",out)
two = re.search("this $", out)
print(one)
print(two)

5.* --> this meta character will form a searching pattern as it will take zero
systax --> re.findall(".*",variable_name)
import re
deepak = "this meta character will form a searching pattern as it will take zero"
gk = re.findall("c.*",deepak)
nk = re.search("t.*",deepak)
print(gk)
print(nk)

6.+ --> this meta character will form a searching pattern as it will take any one or more character for (+)
systax --> re.search(".+",variable_name)
'''
import re
deepak = "this meta character will form a searching pattern as it will take any one or more character for (+)"
gk = re.findall("an.+y",deepak)
nk = re.search("t.*",deepak)
print(gk)
print(nk)












