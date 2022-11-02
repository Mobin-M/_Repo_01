
def func1(i):
    x = yield i

aa = func1(8)

print(type(func1))
print(type(aa))