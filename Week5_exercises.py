#1
L1 = [1,7,4,-2,3]
L2 = ["Cherry","Apple","Blueberry"]

L1.sort()
print(L1)
L2.sort()
print(L2)

#2
L3 = sorted(L2)
print(L3)
print(sorted(L2))

print(L2.sort())

print(sorted("Apple"))

# Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse = True)
print(lst_sorted)

#3
L1 = [1,7,4,-2,3]
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))
    
L2 = sorted(L1,key=absolute)
print(L2)

print(sorted(L1,reverse = True, key = absolute))

# You will be sorting the following list by each element’s second letter, a to z. Create a function to use when sorting, called second_let. It will take a string as input and return the second letter of that string.
# Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.
def second_let(st):
    sec_st = st[1]
    return sec_st

sec_val = []
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
for item in ex_lst:
    sec_val.append(second_let(item))

sorted_by_second_let = sorted(sec_val)
print(sorted_by_second_let)

# Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, and returns only its last character.
# Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted.
def last_char(st):
    last_ch = st[-1]
    return last_ch

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted = sorted(nums,reverse = True, key = last_char)
print(nums_sorted)

# Once again, sort the list nums based on the last digit of each number from highest to lowest. However, now you should do so by writing a lambda function.
# Save the new list as nums_sorted_lambda.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums,reverse = True, key = lambda x: x[-1])
print(nums_sorted_lambda)
    
# 4
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
for x in d.keys():
    print("{} appears {} times".format(x,d[x]))

y = sorted(d.keys())
for k in y:
    print("{} appears {} times".format(k,d[k]))

y = sorted(d.keys(), key = lambda k: d[k], reverse = True)
for k in y:
    print("{} appears {} times".format(k,d[k]))
    
def g(k):
    return d[k]

y = sorted(d.keys(), key = g, reverse = True)
for k in y:
    print("{} appears {} times".format(k,d[k]))

for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))

# Sort the following dictionary based on the keys so that they are sorted a to z.
# Assign the resulting value to the variable sorted_keys.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted_keys = sorted(dictionary.keys())
# sorted_keys = sorted(dictionary)
print(sorted_keys)

# Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to buy at the store.
# Sort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
grocery_keys_sorted = sorted(groceries)
print(grocery_keys_sorted)

# Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted_values=sorted(dictionary,reverse = True, key= lambda x : dictionary[x]) 
print(sorted_values)

# 5
tups = [('A',3,2),
        ('C',1,4),
        ('B',3,1),
        ('A',2,4),
        ('C',1,2)]

for tup in sorted(tups):
    print(tup)
    
# 6
fruits = ['peach','kiwi','apple','blueberry','papaya','mango','pear']
new_order = sorted(fruits, key = lambda fruit_name: (len(fruit_name),fruit_name), reverse = True)
for fruit in new_order:
    print(fruit)

# 7
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse = True)
print(sorted_weather)

# 8
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
print(sorted(states, key = lambda state : len(states[state][0])))
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

print(sorted(states, key = lambda state: s_cities_count(states[state])))


    
    


