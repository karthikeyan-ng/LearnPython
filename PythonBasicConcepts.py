Python
------
Python.exe - 3.x
Editor - PyCharm Community Editon

#Ex:1
print("Hello World!")

=======================================================================================

#Ex:2
my_age = 30
print("My age is " + 30)

=======================================================================================

#Ex:3 - Read input from console
value_a = input("Enter value a : ")
value_b = input("Enter value b : ")
sum = int(value_a) + int(value_b)
#--OR
sum = float(value_a) + float(value_b)
print("Sum of A+B " + sum)

=======================================================================================

Ex:4 - Math functions
import math from

=======================================================================================
#Ex:5 - Lists
lucky_numbers = [4,6,87,45,345]
friends = ["Sara", "Rek", "Krish", "Maddy"]
print(lucky_numbers)
print(friends)

print(friends[3])	#--> "Maddy"
print(friends[0])	#--> "Sara"
print(friends[-1])	#--> from last and -1 is a last element "Maddy"
print(friends[0:2]) #--> Range: starting:end-1 --> "Sara", "Rek"
print(friends[1:])	#--> Range: starting:	  --> "Rek", "Krish", "Maddy"

friends.extend(lucky_numbers)

print(friends) #--> ["Sara", "Rek", "Krish", "Maddy", 4,6,87,45,345]

friends.append("Shewag")	#--> add item at the end of the list

print(friends)	#--> ["Sara", "Rek", "Krish", "Maddy", "Shewag"]

friends.insert(1, "Tendulkar")

print(friends)	#--> ["Sara", "Tendulkar", "Rek", "Krish", "Maddy"]

friends.remove("Rek")

print(friends)	#--> ["Sara", "Krish", "Maddy"]

friends.clear() #--> remove everything from the list

print(friends)	#--> []

friends.pop()	#--> removes the last element from the list

print(friends)	#--> ["Sara", "Rek", "Krish"]

print(friends.index("Rek"))	#--> return the position of the element: 1

print(friends.index("unknown"))	#--> ValueError: 'unknown' is not in list

friends = ["Sara", "Rek", "Krish", "Krish", "Maddy"]
print(friends.count("Krish"))	#--> returns 2.

friends.sort()
print(friends)	#--> sort the list in an ascending order;

lucky_numbers.reverse()
print(lucky_numbers)	#--> it will reverse the order of the list.

friends2 = friends.copy()
print(friends2)		#--> friends2 is same as friends. it's just a copy of exiting to new variable

=======================================================================================

#Ex:6 Tuples

#Type of data structure. It's a kind of list.

#Tuples - are immutable. Once it's created we can't modify.

coordinates = (5,9)	#--> here (5,9) is a Tuples. It's index based. Index starts at 0..N
print(coordinates[1]) #--> 9

coordinates[1] = 15	#--> Python would throw an error. 'tuple' object does not support item assignment.

 
coordinates_list = [(5,9), (12,8), (23,45)]		#--> this is mutable tuple.

=======================================================================================

#Ex: Functions

#Function - is a collection of code. It performs a specific tasks.
#'def' is keyword for function in python

def say_greet():
	print("Welcome to Python world!")
	
def say_greet1(name):
	print(name + ", Welcome to Python world!")
	
def say_greet2(name, age):
	print("Hello " + name + ", you are " + str(age))

#-->How to call a function?
print("Top")
say_greet() #--> "Welcome to Python world!"
print("Bottom")

say_greet1("Mike")

say_greet2("Thomas", 55)


Function with return statement
------------------------------
def cube(value):
	return value*value*value

print(cube(2))	#--> 8
result = cube(3)
print(result)

=======================================================================================

#Ex: If Statements

is_male = True
if is_male:
	print("You are a male")

is_male = False
if is_male:
	print("You are a male")
	

#If-else

is_male = False
if is_male:
	print("You are a male")
else:
	print("You are not a male")


is_male = True
is_tall = True
if is_male or is_tall:
	print("You are a male or tall or both")
else:
	print("You neither male nor tall")
	
is_male = False
is_tall = False
if is_male and is_tall:
	print("You are a tall male")
else:
	print("You are either not male or not tall")
	
is_male = False
is_tall = False
if is_male and is_tall:
	print("You are a tall male")
elif is_male and not(is_tall):
	print("You are a short male")
else:
	print("You are either not male or not tall")


#If statement and comparisions
#  >= <= == != > <

def max_num(num1, num2, num3):
	if num1 >= num2 and num1 >= num3:
		return num1
	elif num2 >= num1 and num2 >= num3:
		return num2
	else
		return num3
	
print(max_num(3,4,5))

	
=======================================================================================
#Dictionaries
# stores information in a key-value pair

# {} -> is Dictionary
# { key: value, } -> entry

monthConversions = {
	"Jan": "January",
	"Feb": "February",
	"Mar": "March"
}

print(monthConversions["Mar"]) #--> March

print(monthConversions.get("Luv", "Not a valid Key")) #--> Not a valid key

monthConversions = {
	1: "January",
	2: "February",
	3: "March"
}

print(monthConversions.get(3)) #--> March

=======================================================================================
#While Loop

i = 1
while i <= 10:
	print(i)
	i = i + 1 # i += 1

print("Done with loop")

----- guessing game ---
secret_word = "test"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
	if guess_count < guess_limit:
		guess = input("Enter Guess: ")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Out of guesses, you lost!")
else: 
	print("You are in.")
	
=======================================================================================
#For Loop

for letter in "Twinkle Twinkle Little Star":	#this would iterate a letter by letter
	print(letter)
