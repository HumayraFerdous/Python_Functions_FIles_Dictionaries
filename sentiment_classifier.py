# To start, define a function called strip_punctuation which takes one parameter,
# a string which represents a word, and removes characters considered punctuation from everywhere in the word.
# (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for ch in punctuation_chars:
        word = word.replace(ch,"")
    return word

# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter,
# a string which represents one or more sentences, and calculates how many words in the string are considered positive words.
# Use the list, positive_words to determine what words will count as positive.
# The function should return a positive integer - how many occurrences there are of positive words in the text.
# Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(sentence):
    counter=0
    sent1 = sentence.lower()
    sent2 = strip_punctuation(sent1)
    sent3 = sent2.split()
    for s in sent3:
        for word in positive_words:
            if s == word:
                counter+=1
    return counter

#sen = "I am better bliss benefit champ tasnu!"
#print(get_pos(sen))

# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter,
# a string which represents one or more sentences, and calculates how many words in the string are considered negative words.
# Use the list, negative_words to determine what words will count as negative. The function should return a positive integer -
# how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased,
# so you’ll need to convert all the words in the input string to lower case as well.
negative_words = []

with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):
    counter=0
    sent1 = sentence.lower()
    sent2 = strip_punctuation(sent1)
    sent3 = sent2.split()
    for s in sent3:
        for word in negative_words:
            if s == word:
                counter+=1
    return counter

#sen = "He is Dull, Dump, Dusty and Dying!"
#print(get_neg(sen))

twitter_data = open('project_twitter_data.csv','r')
result_data = open('resulting_data.csv','w')
result_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
result_data.write("\n")

lines = twitter_data.readlines()
first_out = lines.pop(0)

for ln in lines:
    lst = ln.strip().split(',')
    result_data.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))
    result_data.write("\n")


twitter_data.close()
result_data.close()

                