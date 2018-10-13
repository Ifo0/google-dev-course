# Regular expressons

import re
match_object = re.search(pat, text)
match.group()

if match:

else:

def Find(pat, text):
    match = re.search(pa, text)
    if match: match.group()
    else: print("Not found")

# ... matcher any chars
# \w matcher word char
# \d digit
# \s whitespace
# \S not whitspace character

# r' ' - used to remove all special cases, stands for railway
# + and * to the right of the char matchers means +1, 2, 3


#Finding an email as a
#In square brackets we put allowed characters
Find(r'[\w.]+@[\w.]+, 'dfsdfsd nick.p@gmail.com')

m = re.search(r'([\w.])+@([\w.])+, 'dfsdfsd nick.p@gmail.com')
m.group(1) # to pull of just the nick.p part



m = re.findall(r'[\w.]+@[\w.]+, 'dfsdfsd nick.p@gmail.com gfgf foo@bar')
#Tuples
m = re.findall(r'([\w.])+@([\w.])+, 'dfsdfsd nick.p@gmail.com gfgf foo@bar')

m = re.findall(r'([\w.])+@([\w.])+, 'dfsdfsd nick.p@gmail.com gfgf foo@bar', re.DOTALL)
#To process whole text, not line by line
