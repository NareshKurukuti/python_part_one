'hello'
"hello"

company = "Aplaya Technologies"
print("Given String as company = 'Aplaya Technologies' =>"+company)

# index
print("index[0] in the string =>"+company[0]) #It will print l to r
print("string index of -1 =>"+company[-1])#It will print reverse order (nothing r to l)

# Slicing
print('Slicing')
print("Output of company[2:] =>"+company[2:])
print("Output of company[:3] =>"+company[:3])
print("Specific Position of indexes =>"+company[2:6])
print("Output of company[:] =>"+company[:]) #It will print the entire String

print("Output of company[::] =>"+company[::]) #It will print the entire String same as it is
print("Output of company[::1] =>"+company[::1])
print("Output of company[::2] =>"+company[::2]) #It will print the alternative characters from the string
print("Output of company[::-1] =>"+company[::-1]) #It will print the string in reverse order (nothing but it will print the string as mirror image)



# Replacing the String Characters (String assignment not possible in python)
#company[0] = 'a' #Its not possible in python



# String Functions
print("String Functions")
print("String convert into uppercase by using .upper() =>"+company.upper())
print("Capitalize the String =>"+company.capitalize())
print("Title case the String =>"+company.title())
print("Below Line Output for .split() for the string")
print(company.split())
print("split the string based on character")
print(company.split('e'))

# Print Formatting
insrt = "Insert another string here:{}".format("INSERT ME!")
print(insrt)

items = "Item One:{} Item Two:{}".format("Apple", "Orange")
print(items)

items = "Item One:{y} Item Two:{x}".format(x="Apple", y="Orange")
print(items)