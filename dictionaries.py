#            dictionaries          #
# It has Key, Value Pair

my_dctry = {"key1":"value1", "key2" : "value2"}
print(my_dctry['key1'])

# dictionaries keys having lists
my_dctry_one = {"key1":"value1", "key2": "value2", "key3": {'123':[1,2,3]}, "key4":"ATLP"}
print(my_dctry_one['key3']['123'])

print(my_dctry_one['key3']['123'][2])

# .upper
print(my_dctry_one['key4'].upper())

# reassigning
my_dctry_two = {'launch':'pizza', 'bkft':'eggs'}
my_dctry_two['bkft'] = 'Biriyani'
print(my_dctry_two)

# adding extra elements to Dictionary
my_dctry_two['dinner'] = 'pasta'
print(my_dctry_two)
