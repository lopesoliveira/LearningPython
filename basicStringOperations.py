astring = "Hello world!"
astring2 = "Hello world!"

astring = "Hello world!"
print("single quotes are '  '")
print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

astring = "Hello world!"
print("--------------")
print(astring[3:7:2]) #skip 2 characters Hello world!
print("--------------")                #    _ _       l e espaço
print(astring[3:7:3])                  #    _   _     l e w  

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

astring = "Hello world!"
print(astring[::-1])

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

astring = "Hello world!"
afewwords = astring.split("w")
print(afewwords)

#Exercise
#Try to fix the code to print out the correct information by changing the string.

s = "Hey there! what should this string be?"
# Length should be 20

s = "Hey there! what shou"
print("Length of s = %d" % len(s))

s="here! wha"
# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

s="Hey there! what Joao"
# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

s = "Hey there! what should this string be?"
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())
s="String"
# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
s="Some!"
# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
#print("Split the words of the string: %s" % s.split(" "))
s = "Hey there! what"
print("Split the words %s" % s.split(" "))