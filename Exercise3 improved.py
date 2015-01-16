__author__ = 'macuser'

miles_per_hour = "1..0"

while not miles_per_hour.replace(".", "", 1).isdigit() and not miles_per_hour.replace(" ", "", 1).isdigit() :

    miles_per_hour = raw_input("Please enter your number")

    if not miles_per_hour.replace(".", "", 1).isdigit() and not miles_per_hour.replace(" ", "", 1).isdigit() :
        print "Please enter numbers only"



#conversions loop
miles_per_hour = float(miles_per_hour)
m_p_h = miles_per_hour * 1.0
units = [
    "mile per hour in feet per second"
    "barleycorn/day",
    "furlongs/fortnight",
    "Mach number",
    "the percentage of the speed of light"
]
conversions = {5280: 3600,
               36: 86400,
               660: 1209600,
               1130: 1,
               983571087.9: 1,
}
current_conversion = m_p_h * 5280 * 3600
sequence = -1
for u, c  in conversions.items() :
    current_conversion = u/c * (5280/ 3600) * current_conversion
    print "Converted to %s is %s" %(units[sequence],current_conversion)
    sequence = sequence + 1

#call for conversions


print "Thanks for playing"

