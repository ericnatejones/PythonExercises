def working_fun():
    try:
        fh = open("new", "r")
        # fh.write("This is my test file for exception handling!!")
    except IOError:
        print "cc"
    else:
        print "Written content in the file successfully"
def only_opens():
    new = open("new", "r")

# def create_file():
#     file_name = raw_input("What should the file be called?")

# create_file()
working_fun()
only_opens()