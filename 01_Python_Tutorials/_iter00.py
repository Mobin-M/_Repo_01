x = range(1, 11)
print('')
print(x)
print('')
print(iter(x))
print('')
y = iter(x)
print(next(y))
print(next(y))
print('')
for i in y:         ## what it does is at each step:   i = y.__next__()  OR  i =next(y)
    print(i)