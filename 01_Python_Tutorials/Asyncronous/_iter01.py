# Old school way of implemententing iter

class Iter:
    def __init__(self, n):
        self.n = n
    
    def __iterr__(self):
        self.current = -1
        return self

    def __nextt__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current


print('=========================')

#x0 = Iter(5)
#for i in x0:         # for loop for iter objects only work with naming convention of "iter" and "next"
#    print(i)

print('-------------------------')

x1 = Iter(5)
itr_x1 = x1.__iterr__()

#print(nextt(itr_x1))       This does not work it only works for the namin convention iter and next
print(itr_x1.__nextt__())
print(itr_x1.__nextt__())