x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple

###
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

###
a = 10.5  # Float declaration
b = -3.14 # Negative float
c = 2.0   # Even if it looks like an integer, it's a float
d = 1.23e4  # Scientific notation (1.23 × 10⁴ = 12300.0)
e = 5e-3   # Scientific notation (5 × 10⁻³ = 0.005)
print(a,b,c,d,e)


###
s1 = 'GfG'  # single quote
s2 = "GfG"  # double quote
print(s1)
print(s2)

###
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

### Access specific characters through positive indexing.
s = "GeeksforGeeks"
print(s[0])   # first character
print(s[4])   # 5th character

### Read characters from the end using negative indices.
s = "GeeksforGeeks"
print(s[-10])   # 3rd character
print(s[-5])    # 5th character from end

###
text = "Python"
print(text[-1])   
print(text[-3])

###
text = "GeeksforGeeks"

# Slicing left part of string text
left = text[:-8]

# Slicing middle part of string text
middle = text[-8:-5]

# Slicing right part of string text
right = text[-5:]

print(left)
print(middle)
print(right)

###
li = ["pen", "pencil", "eraser", "apple", "guava", "ginger","Potato", "carrot", "Chilli"]

a = li[-4:]
print(a)

b = li[slice(-6, -4)]
print(b)

###
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rev = num[::-1]
print(rev)

rev2 = num[slice(None, None, -1)]
print(rev2)

###
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

alt = num[::-2]
print(alt)

alt2 = num[slice(None, None, -2)]
print(alt2)

###
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

s = tup[-3:]
print(s)

s = tup[-5:-2]
print(s)

rev_tup = tup[::-1]
print(rev_tup)

s = tup[::-2]
print(s)

###
s = "Python"
for char in s:
    print(char)

###
s = "geeksforGeeks"
s = "G" + s[1:]   # create new string
print(s)

###
s = "GfG"
del s

###
s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)

###
s = "GeeksforGeeks"
print(len(s))

###
s = "Hello World"
print(s.upper())
print(s.lower())

###
s = "   Gfg   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))

###
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

###
s = "Hello "
print(s * 3)

###
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")


name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")

###
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

###import datetime

today = datetime.date.today()
today1 = datetime.datetime.today()
print(today)
print(today1)
print(f"{today:%B %D, %Y}")
print(f"{today:%b %d, %y}")

###
print(f"'GeeksforGeeks'")

print(f"""Geeks"for"Geeks""")

print(f'''Geeks'for'Geeks''')

###
english = 78
maths = 56
hindi = 85

print(f"Ram got total marks {english + maths + hindi} out of 300")

###(we cannot use \n for formatting)
#f"newline: {ord('\n')"

###However, we can put the backslash into a variable as a workaround though :
newline = ord('\n')

print(f"newline: {newline}")

### Comment cannot be used in side format
#f"GeeksforGeeks is {5*2 + 3 #geeks-5} characters."
                    
###
# Printing single braces
print(f"{{Hello, Geek}}")

# Printing double braces
print(f"{{{{Hello, Geek}}}}")          





