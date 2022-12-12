# Understanding generators : next() and send()

def test():
    print("---> Function/generator called for the first time ")
    for i in range(10):
        print("---> Inside for loop --- before yield")
        x = yield i     # Returns/yields  i and pause/saves  here for a sent value (.send()) to assign to x (else None)
        print("---> Inside for loop --- after yield")
        print("sent:",x)



print('--------- Created a generator -------')
_generator = test()
print(type(_generator))
print('')

print('---------- Calling .next() #1----------')
_next = _generator.__next__()
print('---> Value returned (yielded) by calling next:', _next)
print('')

print('---------- Calling .next() #2 ----------')
_next = _generator.__next__()
print('---> Value returned (yielded) by calling next:', _next)
print('')

print('---------- Calling .next() #3 ----------')
_next = _generator.__next__()
print('---> Value returned (yielded) by calling next:', _next)
print('')

print('-----------------------------------------------')
print("(i)(i)(i) Calling .next method #1 (i)(i)(i)")
print("---> Generator: \nA) starts from top and into the for loop and \nB) yields value of i and \nC) pauses there with i == None")
print('')
print('-----------------------------------------------')
print("(i)(i)(i) Calling .next method for #2,3,.. (i)(i)(i)")
print("---> Generator: \nA) Replays from pause point \nB) Since already yielded i, assigns None to x \nC) Get a new i at top of the loop and yields it again \nD) pauses there with i == None")
print('')

print('---------- Calling send() method #3 ----------')
_next_s = _generator.send(5)
print('---> Value returned (yielded) by calling send:', _next_s)
print('')

print('-----------------------------------------------')
print("(i)(i)(i) Calling send method (i)(i)(i)")
print("---> Generator: \nA) sent value is gets assigned to x\nB) Get a new i at top of the loop and yields it again \nC) pauses there with i == None")

print('')


# send() method works like next() method just that at restart of generator it 
# replaces the already yielded value with the sent calue
