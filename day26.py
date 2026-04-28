'''
#7. question mark
this meta character will form a searching pattern as it will take any Zero or One character for(?)
systax --> re.findall("th.?",any)
import re
any = "this metachar"
an = re.findall("th.?",any)
se = re.research("th.?",any)
print(an)
print(se)


#8.curly braces{}
-->  this meta character will form a searching pattern as we can mention the sizein the{}
systax--> re.search(".{size}",varaible)
import re
any = "this metachar"
an = re.findall(".{10}",any)
se = re.search(".{10}",any)
print(an)
print(se)


#9. pipe
this metachar will forma searching pattern as it consider right or left any sring is present or not for(|)
import re
any = "this metachar will form"
an = re.findall("that|will",any)
re = re.search("that|will",any)
print(an)
print(re)


#10.special sequence
--> A special sequence is a\follwed by one of the charcters in the list below, and has a

special meaning :
\A
returns a match if the specified characters are at the beginning of the string
Eg: "\Athe"
import re
txt = "the rain in spain"
x = re.findall("\Athe",txt)
print(x)
if x:
    print("Yes, there is a match!")
else:
    print("No match")


\B --> returns a match if the specified characters are at the beginning end of the word
Eg: r"\brain"

import re
txt = "the rain spain"
x = re.findall(r"\bspain", txt)
print(x)
if x:
   print("yes, there is at least one match!")
else:
   print("no match")

\d -- returns a match where the string contains digits (numbers from 0-9)
Eg: "\d"
import re
txt = "the rain in 56 spain"
x = re.findall("\d",txt)
print(x)
if x:
    print("yes,there is atleast one match")
else:
    print("no match")

\D >>
import re
txt = "the rain in 56 spain"
x = re.findall("\D",txt)
print(x)
if x:
    print("yes,there is atleast one match")
else:


\s- returns a match where the string contains a white space character
Eg: :\s"
import re
txt = "the rain in 56 spain"
x = re.findall("\s",txt)
print(x)
if x:
    print("yes,there is atleast one match")
else:
    print("no match")


\S--> returns a match where the string does not contain a white space character
Eg:" \S"
import re
txt = "the rain in 56 spain"
x = re.findall("\S",txt)
print(x)
if x:
    print("yes,there is atleast one match")
else:
    print("no match")

#Time and Date
--------------
%d---> day
%m---> month
%Y---> year
%H---> hour
%M---> min
%S---> sec
%p---> AM/PM
%A---> day name
%B---> month name

import datetime
now = datetime.datetime.now()
print(now)

'''
import datetime
today = datetime.date.today()
print(today.strftime("%d-%m-%y"))
print(today.strftime("%A"))
print(today.strftime("%B"))










    







