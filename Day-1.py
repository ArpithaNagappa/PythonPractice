print("Hi, this is my first python code")
# This is a single line comment

# this is multi line comment
# 
# end of comment 


if 10 > 5:
 print("This is true!")
print("I am tab indentation")

print("I have no indentation")

a =  2

if a >= 18:
    print('GeeksforGeeks...')
else:
    print('retype the URL.')
print('All set !')

j = 1
  
while(j<= 5): 
     print(j) 
     j = j + 1

print("I have no Indentation ")
print("I have tab Indentation ")

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

###
val = input("Enter your value: ")
print(val)

###
num = input("Enter number:")
print(num)
name1 = input("Enter name: ")
print(name1)

# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))

###
num = int(input("Enter a number: "))
print(num, "is of type", type(num))

###
floatNum = float(input("Enter a decimal number: "))
print(floatNum, "is of type", type(floatNum))

###
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)

###
s = "Brad"
print(s)

s = "Anjelina"
age = 25
city = "New York"
print(s, age, city)

###
s = "one,two,three"
words = s.split(',')
print(words)

###
text = 'geeks for geeks'
print(text.split())  

word = 'geeks, for, geeks'
print(word.split(',')) 

word = 'geeks:for:geeks'
print(word.split(':')) 

word = 'CatBatSatFatOr'
print(word.split('t'))

###
text = "Hello   world"
print(text.split())

###
word = 'geeks, for, geeks, hello'

print(word.split(', ', 0)) 
print(word.split(', ', 4))  
print(word.split(', ', 1))

###
text = "Hello geek, Welcome to GeeksforGeeks."

result = text.split()
print(result)