__author__ = 'macuser'

The_Bible = open('The_Bible', 'r')
bible_dictionary = {}
import string

add_what = "word"

line_counter = 0


def remove_single_quotes(s):
    # Remove single quotes from s iff those single quotes occur at the beginning or end of the string.
    #add if statement to make sure its not to short
    if s[0] == "'":
        s = s[1:]

    if s[-1] == "'":
        s = s[:-2]

    return s


for line in The_Bible:

    line_counter = line_counter + 1

    if line_counter % 1000 == 0:
        print "line %s" % (line_counter)

    words = line.split()

    for word in enumerate(words):

        this_word = word[1]

        parsed_word = this_word.translate(None, string.punctuation)
        parsed_word = remove_single_quotes(parsed_word)

        finished_word = parsed_word.lower()

        # we need to run throuhg the dictionary, and if there are any matched, count it. if not, add it.
        # dasf


        if finished_word in bible_dictionary:
            add_what = "counter"

        else:
            add_what = "word"

        if add_what == "counter":
            bible_dictionary[finished_word] += 1

        else:

            bible_dictionary[finished_word] = 1


            # print bible_dictionary



sorted_bible_dictionary = sorted(bible_dictionary.items(), key=operator.itemgetter(1))
sorted(bible_dictionary.items(), key=lambda sorted_bible_dictionary: sorted_bible_dictionary[1])

# print bible_dictionary
for key, value in sorted_bible_dictionary:

    if key.isdigit() == False:
        if value == 1:
            print "There is one use of the word %s" % (key)
        else:
            print "There are %s uses of the word %s" % (value, key)






