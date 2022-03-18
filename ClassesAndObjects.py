#class MyClass:
#  variable = "blah"
#  
#  def function(self):
#    print("This is a message inside the class")
#    
#class MyClass2:
#  variable = "blah"
#  
#  def function(self):
#    print("This is a message inside the class")
#myobjectx = MyClass2()
#var = myobjectx.variable
#print(var)
#myobjectx.function()

#class MyClass:
#    variable = "blah"
#
#    def function(self):
#        print("This is a message inside the class.")
#
#myobjectx = MyClass()
#myobjecty = MyClass()
#
#myobjecty.variable = "yackity"
#
# Then print out both values
#print(myobjectx.variable)
#print(myobjecty.variable)

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()

#The __init__() function, is a special function that is called when the class is being initiated. It's used for asigning values in a class
class NumberHolder:
  
   def __init__(self, number):  #like constructor ???
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

#Exercise
#We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
    def __init__(self, Name, Color, Kind, Value):
        self.name = Name
        self.kind = Kind
        self.color = Color
        self.value = Value
    
car1 = Vehicle("Fer", "red", "convertible", 60000)
#desc1 = car1.description()
#print(desc1)

car2 = Vehicle("Jump", "blue", "van", 10000)
#desc2 = car2.description()
#print(desc2)

# test code
print(car1.description())
print(car2.description())
