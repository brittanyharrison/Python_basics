"""
Create a variable called age and display age in the same line as James Bond
"""
#first_name = "James"
#last_name = "Bond"
#age = int(input("How old are you?"))

#Greeting = "Hi " + first_name + " " + last_name + "! You are " + str(age) + " years old."
#print(Greeting)


# String slicing and indexing

greetings = "Hello World!   "
# length of string
print(len(greetings))
# Slicing
print(greetings[6:11])

#reverse string
print(greetings[::-1])

#remove white spaces
greetings.strip()
print(len(greetings.strip()))

#count()
print(greetings.count("Hello"))

#lower()
print(greetings.lower())

#upper()
print(greetings.upper())
#capatalize first letter
print(greetings.capitalize())
#replace
print(greetings.replace(" ", ","))

