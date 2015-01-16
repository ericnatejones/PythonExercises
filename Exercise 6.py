try:
    fh = open("new", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "cc"
else:
    print "Written content in the file successfully"

def create_file():
    file_name = raw_input("What should the file be called?")

create_file()