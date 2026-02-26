color = input("What color is rose?: ")
print(color)

###
n = int(input("How many roses?: "))
print(n)

###
price = float(input("Price of each rose?: "))
print(price)

###
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

###
original = [[1, 2], [3, 4]]

import copy

shallow = copy.copy(original)

shallow[0][0] = 99

print("Original:", original)
print("Shallow :", shallow)


###
x = 5
name = "Samantha"  
print(x)
print(name)

###
age = 21
_colour = "lilac"
total_score = 90

###
# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

###
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

###
a = True
b = False
print(a and b)
print(a or b)
print(not a)

###
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

###
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

###
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

###
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

###
a, b = 10, 20
min = a if a < b else b

print(min)

###
a, b = 10, 20
min = a if a < b else b

print(min)

###
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

###
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)