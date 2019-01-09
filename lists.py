#       Lists     #
mylists =[1,2,3]
mylists = ['kjklwer', 1,2,3, 23.2, True, 'akjklje', [1,2,3]]
print(mylists)

print('\n Length of Lists')
print(len(mylists))

print("\n Output of mylists[-1] :")
print(mylists[-1])


mylists_one=['a','b','c','d','e','f']
print("\n Before reassignmnet:")
print(mylists_one)
# Replace the list items
mylists_one[0] = 'New Item'
print("\n After reassignment:")
print(mylists_one)

# Lists Functions #
# .append()
print("\n Output of Lists after appending:")
mylists_one.append("New Item Two") #It will append the item at the end of the lists
print(mylists_one)

# .extend()
mylists_two = ['x', 'y', 'z']
mylists_one.extend(mylists_two)
print("\n Output of .extend() :")
print(mylists_one)


# .pop()
mylists_three = ['a', 'b', 'c', 'd', 'e']
item = mylists_three.pop() #.pop() will removes last item from Lists and it returns that removed item
print('mylists:')
print(mylists_three)
print('using .pop() removes the last item from Lists')
print(item)

# Using .pop() remove the specific item from Lists
print('using .pop() remove the specific item from Lists')
item_one = mylists_three.pop(0)
print(item_one)

# .reverse()  => It will print the reverse order of the List Items
mylists_four = ['a', 'b', 'c', 'd']
print('\n Output of the .reverse() :')
mylists_four.reverse()
print(mylists_four)

# .sort()
mylists_five = [ 5,7, 6, 1, 2, 3]
print('\n Output of the .sort():')
mylists_five.sort()
print(mylists_five)

mylists_six = [1,2, ['x', 'y', 'z']]
print(mylists_six[2][1])

# Matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
print('\n First Column of the Matrix')
first_col = [row[0] for row in matrix]
print(first_col)