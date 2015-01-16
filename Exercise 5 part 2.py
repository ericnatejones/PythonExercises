__author__ = 'macuser'

The_Bible = open('The_Bible', 'r')
word = ""
bible_dictionary ={"ERICN":0}
import re
#function to replace puctution with nothing

def pun_delete():
    def each_one(punctuation):
        global word
        word = word.replace(punctuation, "", 1)
    each_one(".")
    each_one(" ")
    each_one(",")
    each_one("?")
    each_one(":")
    each_one("?")
    each_one(";")
    each_one("!")
    each_one("(")
    each_one(")")



#i will build the dictionary
counter = 0
for line in The_Bible:
    for letter in line:
        word = word + letter

        word = word.lower()

        if letter == " " or letter == "," or letter == "." or letter == ":" or letter == ";":
#at this point, there is a completed word, so we will check our dictionary to see if it's a new word. If it
#is, we will add a counter to that word. If it's not, we will create a new counter and word.

            # print word
            #if the word in not in the dictionary already, add it

            pun_delete()



            if word == bible_dictionary.keys():
                print "success"
                success = raw_input("success")
            else:
                bible_dictionary[word] = 0
                # print bible_dictionary



            word = ""
#our dicitonary is built. Now we are going to run every word in the bible through it and the value of each key will
#be increased by one on every occurance
# print bible_dictionary
import string
The_Bible = open('The_Bible', 'r')
word = ""



for line in The_Bible:
    for letter in line:

        word = word + letter

        word = word.lower()

        if letter == " " or letter == "," or letter == "." or letter == ":" or letter == ";" or letter == "?":
            #need to remove the space, or period, or comma ect from word
            #word = word.translate(none, ' .,!?"')---------- this does not seem to work
            # from string import maketrans   # Required to call maketrans function.

            pun_delete()

            for word_in_dictionary in bible_dictionary:

                if word == word_in_dictionary:
                    bible_dictionary[word] += 1


            word = ""
list = sorted(bible_dictionary)
tuple = sorted(bible_dictionary)

# print our product in most occcurances to least

import operator

sorted_bible_dictionary = sorted(bible_dictionary.items(), key=operator.itemgetter(1))
sorted(bible_dictionary.items(), key=lambda sorted_bible_dictionary: sorted_bible_dictionary[1])

# print bible_dictionary
for key, value in sorted_bible_dictionary:

    print "%s %s" %(key,value)