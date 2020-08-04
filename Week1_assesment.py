#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
#Find the total number of characters in the file and save to the variable num

file=open("travel_plans.txt",'r')
contents=file.read()
num=len(contents)
print(num)
file.close()

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
#Find the total number of words in the file and assign this value to the variable num_words.

file=open("emotion_words.txt",'r')
contents=file.readlines()
num_words=0

for row in contents:
    words=row.split()
    #print(words)
    num_words+=len(words)
print(num_words)
file.close()

#Assign to the variable num_lines the number of lines in the file school_prompt.txt

file=open("school_prompt.txt",'r')
contents=file.readlines()
num_lines=len(contents)
print(num_lines)
file.close()

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars

file=open("school_prompt.txt",'r')
contents=file.read()
beginning_chars=contents[:30]
print(beginning_chars)
file.close() 

#Using the file school_prompt.txt, assign the third word of every line to a list called three

file=open("school_prompt.txt",'r')
contents=file.readlines()
three=[]

for line in contents:
    words=line.split()
    three.append(words[2])
print(three)
file.close() 

#Create a list called emotions that contains the first word of every line in emotion_words.txt

file=open("emotion_words.txt",'r')
contents=file.readlines()
emotions=[]

for line in contents:
    words=line.split()
    emotions.append(words[0])

print(emotions)
file.close() 

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars

file=open("travel_plans.txt",'r')
contents=file.read()
first_chars=contents[:33]
print(first_chars)
file.close()

#Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words

file=open("school_prompt.txt",'r')
contents=file.readlines()
p_words=[]
flag=0
for word in contents:
    val=word.split()
    for find in val:
        if 'p' in find:
            p_words.append(find)

print(p_words)
file.close()

