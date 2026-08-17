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

# String Cleaning

name= " Ayush "
print(name.strip())
print(name.lstrip())
print(name.rsplit())

# strip specific chars
print("$Ayush$".strip("$"))

# Case-insensetive compare
search= "EMAIL"
date= "email"
print(search.lower().strip()==date.lower().strip())


# Find and Match

phone= "+48-176-12345"
print(phone.startswith("+48"))

file= "date_backup.csv"
print(file.endswith(".csv"))

email= "ayush@gmail.com"
print(email.find("@"))
print("@"in email)

# user find() to slice dynamically
print(phone[phone.find("-")+1])

# check combine format

# validation
print("USA".isalpha())
print("1234".isnumeric())

# join

parts= ["2026", "05", "29"]
print("-".join(parts))

# zfill
print("42".zfill(5))                           