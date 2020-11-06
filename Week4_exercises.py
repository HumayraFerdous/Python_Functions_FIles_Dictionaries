#1
def sumTo(aBound):
    theSum = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))
print(sumTo(1000))

# Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
counter = 0
eve_nums = []

while counter <= 15:
    if counter % 2 == 0:
        eve_nums.append(counter)
    counter += 1
print(eve_nums)

# Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop.
# Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

accum = 0
idx = 0

while idx < len(list1):
    accum += list1[idx]
    idx += 1

print(accum)

# Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears.
# The function should return the new list.

def stop_at_four(old_list):
    new_list = []
    idx = 0
    
    while (idx < len(old_list)) and (old_list[idx] !=4):
        val = old_list[idx]
        new_list.append(val)
        idx += 1
        
    return new_list

old_list=[]
print(stop_at_four(old_list))

# 2
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up(enter 0 if no more numbers)"))
    theSum = theSum + x
    
print(theSum) 

# 3
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item(0 when done): '))
        if price != 0:
            count = count+1
            total = total+price
            print('Subtotal: $',total)
        else:
            moreItems = False
    average = total/count
    print('Total items:',count)
    print('Total $',total)
    print('Average price per item: $',average)
    
checkout() 
    

def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer
response = get_yes_or_no('Do you like lima beans? Yes or No: ')
if response == 'Y':
    print('Great! They are very healthy. ')
else:
    print('Too bad. If cooked right, they are quite tasty.')
# 4
import random
import turtle

def isInScreen(w,t):
    if random.random() > 0.1:
        return True
    else:
        return False

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)
    t.forward(50)
    
wn.exitonclick() 

# 5
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: "+str(x))

# 6
initial = 7
def f(x,y=3,z=initial):
    print("x,y,z, are: "+str(x)+", "+str(y)+", "+str(z))
    
f(2)
f(2,5)
f(2,5,8) 

# Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3.
# The function should return the string multiplied by the integer parameter.
def str_mult(st,num = 3):
    return st*num

st="Hello"
print(str_mult(st))

# 7
names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name,scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
    
# 8
# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

# Define a function called multiply. It should have one required parameter, a string.
# It should also have one optional parameter, an integer, named mult_int, with a default value of 10.
# The function should return the string multiplied by the integer.
# (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)

def multiply(st,mult_int = 10):
    return st*mult_int

# Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work.
# Fix the code so that it passes the test. This should only require changing one line of code.
def waste(mar,var = "Water", marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string

# 9
func = lambda x : x-2
print(func(5))

# 10
last_char = lambda s: s[-1]
print(last_char('hello'))