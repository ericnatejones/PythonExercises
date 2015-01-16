__author__ = 'macuser'
#recieve user number of gallons and only a number
miles_per_hour="null"

while not miles_per_hour.isdigit():
    miles_per_hour=raw_input("Please enter a speed in miles/hour:")

    if not miles_per_hour.isdigit():
        print "Please enter a number. Please. "

print "Original speed in mph is:%s" %(miles_per_hour)

m_p_h = int(miles_per_hour)*1.0

#conversions loop

units = ["barleycorn/day","furlongs/fortnight","Mach number","the percentage of the speed of light"]
conversions = [4547009.496,0.00059115777,(.00129789357065/2688),0.00000114891]
current_conversion = m_p_h
for u, c  in zip(units,conversions) :
    current_conversion = c * current_conversion
    print "Converted to %s is %s" %(u,current_conversion)




print "Thanks for playing"