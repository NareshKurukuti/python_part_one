def my_func(param1='default'):
    print("my first python function! {}".format(param1))

my_func()

def hello():
    return('hello')

result = hello()
print(result)

def addNum(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers"

result = addNum("2","8")
print(result)

# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2==0

evens = filter(even_bool, mylist)
print(evens)

# Lambda
evens = filter(lambda num:num%2 == 0, mylist)
print(list(evens))


st = 'hello'
st.lower()
st.upper()
st.split()

tweet = "Go Sports! #Sports"
result_split = tweet.split('#')

print(result_split)

