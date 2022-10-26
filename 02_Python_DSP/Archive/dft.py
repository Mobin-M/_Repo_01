import numpy as np   
import matplotlib.pyplot as plt

print("dft imported")

def basis_func(N,k):    # calculatig basis function for each k
    basis = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        basis[n] = np.exp(-1j*k*2*np.pi*n/N)
    return basis

def dft(N, x_sum, fs):     #note: fs is not necessary for calculating dtfs. just input for the last part printing c.t frequency
    res = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        basis = basis_func(N,k)     #retuns an array of basis function with specific k and with element varying with n
        res[k] = sum(basis * x_sum)  #returns an array of complex number indicatinf magnitude and phase for specific inverstigated frequency (k)
    
    # array of magnitude(availability) of each "investigating" frequency/harminics (k) in the signal (x_sum) under investigation
    mag = np.absolute(res)
    
    # printing the bin numbers (~frequency) k with high magnitude (== m's of signal under analysis)          ToDoL:improve this part 
    for kk in range(N):
        if mag[kk] > 0.5:
            print("a harminoc found at: ", kk)
            print("Original C.T. frequency:",str(round(kk*(1/N)*fs)),"[cycle/sec]")
            #Why a pick at 2183??  2205-22 (perodicity in N) and since real signal a_-k* = a_k
    return mag,res


def basis_func_Inv(N,k):    # calculatig basis function for each k
    basis = np.zeros(N, dtype=np.complex128)
    for n in range(N):
        basis[n] = np.exp(1j*k*2*np.pi*n/N)
    return basis

def idft(N,x_k):
    res = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        basis = basis_func(N,k)     #retuns an array of basis function with specific k and with element varying with n
        res[k] = sum(basis * x_k)/N
    print(type(res[0]))
    return res
    