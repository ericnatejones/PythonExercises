import string
import random

def generate_ran():
    for i in range(1, 11):
        length = random.randint(2, 20)
        chars = (''.join(random.choice(string.ascii_uppercase) for i in range(length)))
        with open('exercise_five.dat.txt', 'a+') as f:
            f.write(chars)
            f.write("\n")

generate_ran()

letters = {}
with open('exercise_five.dat.txt', 'r+') as f:
    text = f.readlines()
    # n = 1
    # for i in range(0, len(text), n):
    for line in text:

        for letter in line:
            print letter
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    print letters
    for key, value in letters.iteritems():
        print "%s ==> %s" % (key, value)