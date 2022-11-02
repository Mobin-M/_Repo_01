
def func1():
    yield 10
    yield 20
    yield 30

async def func2():
    return 1

print('////////////////////////////////////////////')
aa = func1()
print(type(aa))
print(dir(aa)) 



print('////////////////////////////////////////////')
aaa = func2()
print(type(aaa))
print(dir(aaa))

