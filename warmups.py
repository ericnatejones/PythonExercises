def sorta_sum(a, b):
    return a + b if a + b not in range(10, 20) else 20

print sorta_sum(4, 6)
print sorta_sum(4, 62)
print sorta_sum(2, 6)
print sorta_sum(42, 6)

