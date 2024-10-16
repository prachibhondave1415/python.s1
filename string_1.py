#Slicing

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

# Modification of Strings

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip()) 
print(a.replace("H", "J"))
print(a.split(",")) 

# Formatting of Strings

age = 36                                # Create an f-string
txt = f"My name is John, I am {age}"
print(txt)    

price = 59                              # Modifiers and Placeholders
txt = f"The price is {price} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars" # Math operation in placeholder
print(txt)

# String Methods

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
x = txt.startswith("Hello")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

txt = "50"
x = txt.zfill(10)
print(x)

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)