# Create a dictionary that keeps track of the USA’s Olympic medal count. Each key of the dictionary should be the type of medal (gold, silver, or bronze) and each key’s value should be the number of that type of medal the USA’s won. Currently, the USA has 33 gold medals, 17 silver, and 12 bronze.
# Create a dictionary saved in the variable medals that reflects this information
medals={'gold':33,'silver':17,'bronze':12}
print(medals)

#You are keeping track of olympic medals for Italy in the 2016 Rio Summer Olympics! At the moment, Italy has 7 gold medals, 8 silver metals, and 6 bronze medals.
#Create a dictionary called olympics where the keys are the types of medals, and the values are the number of that type of medals that Italy has won so far.
olympics={'gold':7}
olympics['silver']=8
olympics["bronze"]=6
print(olympics)

#Update the value for “Phelps” in the dictionary swimmers to include his medals from the Rio Olympics by adding 5 to the current value (Phelps will now have 28 total medals). 
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers['Phelps']=swimmers['Phelps']+5
print(swimmers)

#Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. 
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places['Brazil'] = 2016
print(places)

#We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. 
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events=list(medal_events.keys())
print(events)

# Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
word=sentence.split()
word_counts={}

for words in word:
    if words not in word_counts:
        word_counts[words]=0
    word_counts[words]+=1
print(word_counts)

#  Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "what can I do"
char_d={}

for key in stri:
    if key not in char_d:
        char_d[key]=0
    char_d[key]+=1
print(char_d)

# The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total.
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total=0

for country in travel:
    total=total+travel[country]
print(total)

# schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits.
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits=0

for course in schedule:
    total_credits+=schedule[course]
print(total_credits)

#  Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d={}
for x in placement:
    if x not in d:
        d[x]=0
    d[x]+=1

ks = list(d.keys())
min_value= ks[0]

for value in ks:
    if d[value] < d[min_value]:
        min_value = value
print(min_value)

#Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
product = "iphone and android phones"
lett_d ={}
for x in product:
    if x not in lett_d:
        lett_d[x]=0
    lett_d[x]+=1

ks = list(lett_d.keys())
max_value = ks[0]

for value in ks:
    if lett_d[value] > lett_d[max_value]:
        max_value = value
print(max_value)
 