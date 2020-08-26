#1
def square(x):
    y=x*x
    return y

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare,result))

#2
def longer_than_five(list_of_names):
    for name in list_of_names:
        if len(name)>5:
            return True

    return False

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))

#  Write a function named same that takes a string as input, and simply returns that string.
def same(s):
    return s
name="Humayra"
print(same(name))

# Write a function called same_thing that returns the parameter, unchanged.
def same_thing(p):
    return p

number=2
print(same_thing(number))

# Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.
def subtract_three(number):
    return number-3

number = 4
print(subtract_three(number))

# Write a function called change that takes one number as its input and returns that number, plus 7
def change(number):
    return number+7

num = 4
print(change(num))

#Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(name):
    return "Hello, my name is {} and I love SI 106.".format(name)

st = "Becky"
print(intro(st))

# Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.
def s_change(name):
    return name+" for fun."

st = "Music"
print(s_change(st))

#Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters,
# return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
def decision(word):
    if len(word) > 17:
        return "This is a long string"
    elif len(word) <= 17:
        return "This is a short string"
    
word = "abcdefghijklmnopqrstuvwxyz"
word1 = "abcdefgh"

print(decision(word))
print(decision(word1))

#3
def mylen(seq):
    c = 0
    for _ in seq:
        c = c+1
    return c
print(mylen("hello"))
print(mylen([1,2,7]))

# Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.

def total(list_of_numbers):
    acc = 0
    for number in list_of_numbers:
        acc= acc + number
    return acc

numbers = [1, 3, 5, 7, 9]
print(total(numbers))

# Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(list_of_numbers):
    c = 0
    for _ in list_of_numbers:
        c = c+1
    return c

numbers = [2,4,5,6,9,0,1]
print(count(numbers))

#4
def square(x):
    y = x*x
    return y
def sum_of_squares(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)
    
    return a+b+c

a = -5
b = 2
c = 10
result = sum_of_squares(a,b,c)
print(result)

# 5
def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c]=0
        d[c]=d[c]+1
    return d

def best_key(dictionary):
    ks=dictionary.keys()
    best_key_so_far= list(ks)[0]
    for k in ks:
        if dictionary[k]>dictionary[best_key_so_far]:
            best_key_so_far=k
    return best_key_so_far

print(most_common_letter("abbbbbbbbbbbccccddddd"))
    
# Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.

def addit(number):
    return number+5

def mult(num):
    val = num * addit(num)
    return val

n = 10
print(mult(n))
# 6
def double(y):
    y = 2*y
def changeit(lst):
    lst[0]="Michigan"
    lst[1]="Wolverines"

y=5
double(y)
print(y)
mylist=['our','students','are','awesome']
changeit(mylist)
print(mylist) 
    
# tuple packing
julia = ("Julia","Roberts",1967,"Duplicity",2009,"Actress","Atlanta,Georgia")
julia =  "Julia","Roberts",1967,"Duplicity",2009,"Actress","Atlanta,Georgia"
print(julia[4])

# Create a tuple called practice that has four elements: ‘y’, ‘h’, ‘z’, and ‘x’.
practice = ('y','h','z','x')
print(practice[2]) 

# Create a tuple named tup1 that has three elements: ‘a’, ‘b’, and ‘c’.
tup1 = ('a','b','c')
# Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check=[]
for item in lst_tups:
    val = item[2]
    t_check.append(val)
    
print(t_check)
    
#  Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds=[]
for item in tups:
    val = item[1]
    seconds.append(val)
print(seconds)

# 7
def circleInfo(r):
   
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)

# Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown. It should return a tuple of these variables in this order.
def information(name,birth_year,fav_color,hometown):
    return name,birth_year,fav_color,hometown

print(information("Humayra",1997,"Blue","Dhaka"))

# Define a function called info with the following required parameters: name, age, birth_year, year_in_college, and hometown. The function should return a tuple that contains all the inputted information.
def info(name,age,birth_year,year_in_college,hometown):
    return name,age,birth_year,year_in_college,hometown 

#Unpacking
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia

# swap with tuple

a = 1
b = 2
(a, b) = (b, a)
print(a, b)

# unpacking into iterable variables
authors = [('Paul','Resnick'),('Brad','Miller'),('Lauren','Murphy')]
for first_name,last_name in authors:
    print("first name: ",first_name,"last_name:",last_name)

#enumaerate
fruits = ['apple','pear','appricot','cherry','peach']
for idx,fruit in enumerate(fruits):
    print(idx,fruit)
    
# With only one line of code, assign the variables water, fire, electric, and grass to the values “Squirtle”, “Charmander”, “Pikachu”, and “Bulbasaur”
(water,fire,electric,grass)=("Squirtle", "Charmander", "Pikachu", "Bulbasaur")

# With only one line of code, assign four variables, v1, v2, v3, and v4, to the following four values: 1, 2, 3, 4.
(v1,v2,v3,v4)=(1,2,3,4)

# If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names=[]
p_number=[]

for idx,num in pokemon.items():
    p_names.append(idx)
    p_number.append(num)

print(p_names)
print(p_number)

# The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create a list of keys from the dictionary track_medal_counts and assign the list to the variable name track_events. Do NOT use the .keys() method.
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events=[]

for idx,item in track_medal_counts.items():
    track_events.append(idx)
print(track_events)

#unpacking tuples as arguments
def add(x,y):
    return x+y
print(add(3,4))
z = (5,4)
print(add(*z))