import operator
number = False

def get_user_input():

    numbers = []
    while True:
        try:
            how_many_numbers = int(raw_input("how many numbers?: "))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."

    for current_number in range(0, how_many_numbers):
        while True:
            try:
                current_number = int(raw_input("Please enter a number: "))
                break
            except ValueError:
                print "Oops!  That was no valid number.  Try again..."
        numbers.append(current_number)

    return numbers

def add_numbers(numbers):
    print numbers
    numbers_added = 0
    numbers_multi = 0
    for number in numbers:
        print number
        numbers_added += number
        numbers_multi += number

    return numbers_added



numbers = add_numbers(get_user_input())
print numbers



# name = raw_input("numbers")
# first_number = ""
# second_number = ""
# is_first_number = True
# is_new_number = True
# for character in name:
#
#     if is_first_number == True:
#         if character.isdigit():
#             first_number += character
#             # print character
#             # print first_number
#             length_of_number = 1
#             is_new_number = False
#
#             # while (character + length_of_number).isdigit():
#
#     if is_new_number == False:
#         if character.isdigit() == False:
#             is_new_number = True
#             is_first_number = False
#
#     if is_new_number:
#         if character.isdigit():
#             second_number += character
#             # print character
#             # print second_number
#             # print "yo"
#             length_of_number = 1
#
# print int(first_number) + int(second_number)





