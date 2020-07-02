from functools import reduce
x = ['rocks', 'ITS', 'course']
print(x)
print(reduce(lambda val1, val2: val1 + "-" + val2, sorted(x)))
