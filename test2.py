def get_user_input():
    while True:
        try:
            return float(raw_input("Enter gallons of Gasonline"))
        except:
            print "try entering a simple number, with or without a decimal, and no spaces"
    return gallons_of_gasoline

gallons_of_gasoline = get_user_input()



