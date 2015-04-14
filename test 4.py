
def word_to_integer():

    user_input = raw_input("how fast can you run?: ")


    if user_input.isdigit():
        if int(user_input) >= 10:
            print "You can't run that fast!"
            word_to_integer()

        elif user_input.isdigit():

            return float(user_input)
    elif user_input == "zero":
        return 0
    elif user_input ==  "one":
        return [1]
    elif user_input == "two":
        return [2]
    elif user_input == "three":
        return [3]
    elif user_input == "four":
        return [4]
    elif user_input == "five":
        return [5]
    elif user_input == "six":
        return [6]
    elif user_input == "seven":
        print "yo"
        user_input = int(7)
        return user_input
    elif user_input == "eight":
        return [8]
    elif user_input == "nine":
        return [9]
    elif user_input == "ten":
        return [10]
    word_to_integer()



print float(word_to_integer())

