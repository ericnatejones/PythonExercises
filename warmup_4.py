counter = 1
list_of_current_prime_numbers = [3]
add_number_to_list = False
while True:
    counter += 2

    for number in range(1,len(list_of_current_prime_numbers),2):
        if number % counter == 0:
            add_number_to_list = number
            break

    if add_number_to_list:
        list_of_current_prime_numbers.append(add_number_to_list)
        add_number_to_list = False
        print list_of_current_prime_numbers




