# How generator works

def gen(n):
    for i in range(n):
        yield i             # Pauses the loop and saves all of its information, resturts when next is evecuted on this function

def gen2():
    yield 1
    print('Pause 1')        #Notice that this will be printed with the "next" call since the function pauses on yield 1.
    yield 3
    print('Pause 3')
    yield 7

print('------------------------')
for i in gen(5):        # which behindis like :  i = next(gen(5))
    print(i)
print('')

print('------------------------')
x = gen(5)
print(hash(x))
print('')

print('------------------------')
print(next(x))
print(next(x))
print(next(x))
print('')

print('------------------------')
y = gen2()

print(type(y))

print(next(y))
print('Next')
print(next(y))
print('Next')
print(next(y))