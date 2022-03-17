#This prints out Hello, John!
from unicodedata import name

name = "John"
print("Hello, %s!" % name)

#This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#This prints out: A list:[1, 2, 3]
mylist = [1 ,2 ,3]
print("A list: %s" % mylist)

#Exercise
#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
#Hello John Doe. Your current balance is $53.44.

#data = ("John", "Doe", 53.44)
#format_string = "Hello"
#print(format_string + " %s %s your current balance is %f" %(data))
 
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s your current balance is %s";
print(format_string %data)