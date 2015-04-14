__author__ = 'macuser'


def calculate_how_much_i_will_pay(how_many, price, what_are_we_buying):
    total_price = how_many * price
    return "$" + str(total_price) + " of " + what_are_we_buying

print calculate_how_much_i_will_pay(5, 10, "dolls")


