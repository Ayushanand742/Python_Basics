text= "Ayush"
num= 10 

# Function- work at either 
print(type(text))
print(len(text))

# Method - class specefic

print(text.upper())
print(num.bit_length())

# num.upper() -> Attribute error
# int object has no attribute 


# Comparision

x= 10
y= 3
print(x==y)
print(x!=y)
print(x>y)
print(x<=y)

# ceil()
import math
print(math.ceil(4.2))
print(math.ceil(4.8))

# floor
print(math.floor(4.2))
print(math.floor(4.8))

# round
print(round(4.2))
print(round(4.8))


# Numbers
number= [10,20,30]

# Strings
name= ["Ayush", "Bikash", "Sourav", "Navneet"]

# Boolean
status= [True, False, True]

# Mixed Data
data= ["Ayush", 26, True]
print(data)
print(data[1])

