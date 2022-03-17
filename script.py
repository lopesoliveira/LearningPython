from re import I


print("Thil line will be printed")
x=1
if x == 1:
  #indented four spaces
  print("x is 1.")
print("Goodbye World!")

myint = 7
print(myint)
myfloat=7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

a,b = 3,4
print(a,b)

#This will not work
one = 1
two = 2
hello = "hello"
#print(one + two + hello)
#This will work
print(str(one) + str(two) + hello)

#Change this code
#mystring = None
#myfloat = None
#myint = None

mystring = "hello"
myfloat = 10.0
myint = 20

#testing code
if mystring == "hello":
  print("String %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
  print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
  print("Integer: %d" % myint)
  
#lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
  print(x)
  
#
numbers = [6,7,8,9]
strings = ["Joao", "Carlos", "Soares"]

second_name = "Oliveira"

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

number = 1 + 2 * 3 / 4.0
print(number)

#Exercise
x = object()
y = object()

#TODO: Change this code
#x_list = ([x] * 10)
#y_list= ([y] * 10)
#big_list = ([x,y]*10)

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

#testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
  print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
  print("Great!")


  
