# Without variable
print("My name is Ayush Anand")
print("Ayush loves python")

# with variable 
name= "Ayush"
language= "Python"
print(f"My name is {name}")
print(f"{name}loves{language}")

print("Line1\nLine2")
print("Hi\tEveryone")
print("Path:C:\\Users\ITZAY\Desktop\college python")
print("She said\"Hi\"")

# RESHAPE STRINGS

date= "2026/08/14"
print(date.replace("/","-"))

first= "Ayush"; last= "Anand"
print(f"{first}{last}")

csv= "Ayush,25,USA"
print(csv.split(","))
print("="*20)


# Indexing

code= "Ayush-25"
print(code[0])     # A
print(code[-1])    # 5
print(code[0:])    # Ayush 
print(code[-2:])   # 25

date= "2026-05-29"
print(date[0:4], date[5:7], date[-2:])

print(code[0:9:2])  # stride

