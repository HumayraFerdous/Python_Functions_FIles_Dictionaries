# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list.
#The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(ori_list):
    new_list = []
    idx = 0
    
    while (idx < len(ori_list)) and (ori_list[idx] !=5):
        val = ori_list[idx]
        new_list.append(val)
        idx += 1
        
    return new_list

o_list=[2,3,4,1,5,7]
print(sublist(o_list))

# Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7.
# What is returned is a list of all of the numbers up until it reaches 7.

def check_nums(alist):
    new_list = []
    idx = 0
    while idx < len(alist):
        if alist[idx] != 7:
            val = alist[idx]
            new_list.append(val)
        else:
            break
        idx += 1
    return new_list

lst = [1,2,3,4,5]
print(check_nums(lst))

# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).


def sublist(o_lst):
    idx = 0
    n_list = []
    while idx < len(o_lst):
        val = o_lst[idx]
        if val != "STOP":
            n_list.append(val)
        else:
            break
        idx += 1
    return n_list

o_list = ["item","apple","STOP","red"]
print(sublist(o_list))

# Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. 
#The function should return the new list.

def stop_at_z(o_lst):
    idx = 0
    n_list = []
    while idx < len(o_lst):
        val = o_lst[idx]
        if val != "z":
            n_list.append(val)
        else:
            break
        idx += 1
    return n_list

o_list = ["item","apple","z","red"]
print(stop_at_z(o_list))

# Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2.
# Once complete, sum2 should equal sum1
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
print(sum1)

idx = 0
sum2 = 0
while idx < len(lst):
    sum2 += lst[idx]
    idx += 1
    
print(sum2)

#  Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops.
# (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing.

def beginning(o_lst):
    idx = 0
    n_list = []
    while idx <= 9:
        val = o_lst[idx]
        if val != 'bye':
            n_list.append(val)
        else:
            break
        idx += 1
    return n_list

ori_list = ['a','b','c','d','bye','f','g','h','9','w']
print(beginning(ori_list)) 

# Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
def mult(num1,numb2 = 6):
    return num1*numb2

n = 10
print(mult(10))

#The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.
def greeting(name,greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

# Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.
def sum(intx, intz=5):
    return intz + intx

x = 10
print(sum(x))

# Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}.
# If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”

def test(num, bol = True, dict1={2:3,4:5,6:8}):
    if bol == True:
        for idx,item in dict1.items():
            if num == idx:
                return item
            
    elif bol == False:
        return bol

n = 5
print(test(n,bol= True,dict1={5:4,2:1}))

# Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn
# so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False. But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.


def checkingIfIn(st,direction = True, d ={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        found = 0
        for idx in d.keys():
            if st == idx:
                found = 1
        if found == 1:
            return True
        else:
            return False
    else:
        nfound = 0
        for idx in d.keys():
            if st == idx:
                nfound = 1
        if nfound == 1:
            return False
        else:
            return True

   
s = 'app'   
print(checkingIfIn(s,direction=False))


# We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False.
#Follow the instructions in the active code window for specific variable assignmemts.
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]
        
# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('app')
print(c_false)

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('app',direction = False)
print(c_true)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit')
print(fruit_ans)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('sweet',d={'sweet':8})
print(param_check)
    
    