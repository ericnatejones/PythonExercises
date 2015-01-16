__author__ = 'macuser'

number_of_gallons="null"
#responses to user not entering a number
desperation_phrase = ["Please enter a number. Please.","Are you entering it in numerical form?","Like, don't say 'four'","Don't make me freak out","You're awful at this","Don't make me choose a number for you!"]
desperation=0

#have user enter number and respond with progressively more desperate responses if they dont


while not number_of_gallons.isdigit():
    number_of_gallons=raw_input("Please enter the number of gallons of gasoline:")
    #this checks to see if it's a float or if there is an accidental space. Which are both acceptable
    if not number_of_gallons.replace(".", "", 1).isdigit() and not number_of_gallons.replace(" ", "", 1).isdigit() :

        if not number_of_gallons.isdigit():

            if desperation<6:

                print desperation_phrase[desperation]
                desperation=desperation+1
            else:
                print "We will go with 100 gallons then"
                number_of_gallons="100"

    else:
        break
print "Original number of gallons is:%s" %(number_of_gallons)
#the next three lines are opional. If we want all integers to become floats, we can get rid of them
if number_of_gallons.isdigit():
    gallons = int(number_of_gallons)
else:
    gallons = float(number_of_gallons)
# conversions function

def conversion (unit,conversion_rate,comparison_phrase):
    conversion = conversion_rate * gallons
    print "%s gallons %s %s %s" %(gallons, comparison_phrase, conversion, unit)



#call for conversions

conversion("liters",3.7854,"is the equivalent of")
conversion("barrels of oil", .0512820512821, "of gasoline requires" )
conversion("pounds of CO2",20.0,"of gasonline produces" )
conversion("gallons of ethanol",1.51915455746, "of gasoline is the energy equivalent to" )
conversion("US dollars",2.0, "of gasonoline requires" )
print "Thanks for playing"

#to fix. Make it work even if the user adds a space after the number


