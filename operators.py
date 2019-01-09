# Greaterthan or Equal to
1 >= 1

# Lessthan or Equal to
1 <= 4

# Equality
1 == 1

1 == "1"

'hi' == 'bye'

# Inequality
'i' != 1

# AND
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

# IF Condtions
if 1 < 2:
    print('YES')

if 1 < 2:
    print('First BLOCK')
    if 2 < 3:
        print("Second BLOCK")

# If Else
if 1 < 2:
    print('if')
else:
    print('else')

# IF ElseIf Else
if 1 < 2:
    print('if')
elif 3 == 3:
    print('elif')
else:
    print('else')

# For Loop
seq = [1,2,3,4,5,6]
for item in seq:
    print('hello')
d= {"Sam" :1, "Frank":2, "Dan":3}
for item in d:
    print(item)

print('\n')

for item in d:
    print(item)
    print(d[item])

mypairs =[(1,2), (3,4), (5,6)]
for p in mypairs:
    print(p)

for (tup1, tup2) in mypairs:
    print(tup1)
    print(tup2)

for tup1, tup2 in mypairs:
    print(tup1)
    print(tup2)

# range
range(0,5)
print(list(range(0,5)))

for item in range(10):
    print(item)

# While Loop
i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i+1

# List Comprehension
x = [1,2,3,4]

out = []
for num in x:
    out.append(num*2)
print(out)

output = [num**2 for num in x]
print(output)