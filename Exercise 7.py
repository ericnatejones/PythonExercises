__author__ = 'macuser'

temperatures_of_cities = {
"Boston": "0 C",
"Boise": "48 F",
"Phoenix": "85 F",
"Miami": "40 C",
"Riverside": "30 C",
"Baltimore": "32 F"
}

conversion_temperature = []
for key in temperatures_of_cities:
    un_converted_temerpatures = temperatures_of_cities.get(key[0:])
    f_or_c = un_converted_temerpatures[-1:]

    number = un_converted_temerpatures[:-1]
    number = int(number)

    city = key
    if f_or_c == "F":
        convert_it = (number-32)*5.0/9
        print "In %s it is %s degrees Fahrenheit, which is equivalent to %s degrees Celsius" %(city,number, convert_it)
    else:
        convert_it = number * 9.0/5 + 32
        print "In %s it is %s degrees Celsius, which is equivalent to %s degrees Fahrenheit" %(city,number, convert_it)


