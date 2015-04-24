def sum13(nums):
    total = 0
    for number in nums:
        if number == 13:
            return total
        else:
            total += number
    return total

print sum13([1, 2, 2, 1])
print sum13([1, 1])
print sum13([1, 2, 2, 1, 13])