__author__ = 'macuser'

print "******************************"
print "EXERCISE 4 - MENU"
print "******************************"
print "1. Write input to file"
print "2. Write input to screen"
print "3. Quit"

def get_user_input():

    global choice
    choice = raw_input("Enter your choice[1-3] : ")

the_file = open("project_4.dat", 'a+')

get_user_input()

while True:

    if choice == "1":
        the_file.write(raw_input("Enter phrase: "))
        get_user_input()
    elif choice == "2":
        to_be_printed_on_the_screen = raw_input("Enter phrase: ")
        print to_be_printed_on_the_screen
        get_user_input()
    elif choice == "3":
        #the_file.closed("project_4.dat", 'a+')
        print "This program is over"
        break
    else:
        print "Your choice should be 1, 2, or 3: "
        get_user_input()