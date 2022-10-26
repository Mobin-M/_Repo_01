import numpy as np
# gather all fourier transform implementation (keep basis function in sinusoids?)


# constructing discrete time basis function used in dtfs and dft to investigate/find fundamental frequencies. for each specific k a basis function is constructed
# 1- looping in N for calculating basis function for each k is unnecessary and very time consuming (from 1.3 sec to 16 sec, for an x_n of length 0.1 sec)
def basis_func(N, k):
    basis = np.zeros(N, dtype=np.complex128)
    #for n in range(N):
    #        basis[n] = np.exp(-1j*k*2*np.pi*n/N)
    basis = np.exp(-1j*k*2*np.pi*np.arange(N)/N)
    return basis

# symmetric basis function (from -N/2 to N/2 instead of 0 to N)
def basis_func_symm(N, k):
    basis = np.zeros(N, dtype=np.complex128)
    #for n in range(N):
    #        basis[n] = np.exp(-1j*k*2*np.pi*n/N)
    nv = np.arange(-N/2,N/2)
    basis = np.exp(-1j*k*2*np.pi*nv/N)
    return basis

# constructing discrete time basis function used in Idtfs and Idft to construct the sinusoid from frequencies available in spectrum
# 1- looping in N for calculating basis function for each k is unnecessary and very time consuming 
def basis_func_Inv(N,k):    
    basis = np.zeros(N, dtype=np.complex128)
    #for n in range(N):
    #    basis[n] = np.exp(1j*k*2*np.pi*n/N)
    basis = np.exp(1j*k*2*np.pi*np.arange(N)/N)
    return basis

# symmetric inverse basis function
######CHANGED: SEE IN idft_symm() DESCRIPTION
def basis_func_Inv_symm(N,n):    
    basis = np.zeros(N, dtype=np.complex128)
    #for n in range(N):
    #    basis[n] = np.exp(1j*k*2*np.pi*n/N)
    kv = np.arange(-N/2,N/2)
    basis = np.exp(1j*kv*2*np.pi*n/N)
    return basis

# Calculating dtfs from a series of sample data (x_n) with a known length N (the input data x_n should be periodicalso in discrete-time in case of dtfs)
def dtfs(N, x_n):                   
    print('Calculating dtfs...')

    x_k = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        basis = basis_func(N,k)         # retuns an array of basis function with specific k as input and with element varying with n
        x_k[k] = sum(basis * x_n)/N     # res[k] is an element of complex value in array res, showing the result of investigation of basis function of sinusoid under investigation x_n
                                        # meaning if res[k] is small/zero the frequency k is not present in sinusoid under investigation (orthogonality)

    x_k_abs = np.absolute(x_k)              # array of result of investigation, with each investigating frequency (k) of basis function. showing magnitude of present sinusoid in x_n
    
    return x_k, x_k_abs                     # returning an array; for each frequency investigating k, both result (res) and magnitude of result (mag)

# Constructing the Sinusoid from available frequencies in the spectrum x_k, originally periodic in discrete-time  (idtfs)
def idtfs(N,x_k):

    print('Calculating inverse dtfs')

    x_n_constructed = np.zeros(N)                           #in case x_k is coming from a real signal (like cosine) the result should be an array of real values.
    
    for k in range(N):
        basis = basis_func(N,k)                             #retuns an array of basis function with specific k as input and with element varying with n
        x_n_constructed[k] = sum(basis * x_k)/N
    
    return x_n_constructed

# Calculating dtfs from a series of sample data (x_n) with a known length N
def dft(N, x_n):
    
    print('Calculating dft...')

    x_k = np.zeros(N, dtype=np.complex128)
    #x_k = np.array([], dtype=np.complex128)     # in case of using np.append
    for k in range(N):
        basis = basis_func(N,k)         # retuns an array of basis function with specific k as input and with element varying with n
        #basis = np.exp(-1j*k*2*np.pi*np.arange(N)/N)   # "maybe" a little faster to calculate inside instead of calling a function, but for better design keep calling baby!!
        x_k[k] = sum(basis * x_n)       # x_k[k] is an element of complex value in array x_k, showing the result of investigation of basis function of sinusoid under investigation x_n
                                        # meaning if x_k[k] is small/zero the frequency k is not present in sinusoid under investigation (orthogonality)
        
        #OR: x_k =  np.append(x_k, sum(x_n * basis))   # can be used instead of indexing but same result (in time consumption)

    x_k_abs = np.absolute(x_k)              # array of result of investigation, with each investigating frequency (k) of basis function. showing magnitude of present sinusoid in x_n
    
    return x_k, x_k_abs                     # returning an array; for each frequency investigating k, both result (res) and magnitude of result (mag)

# symmetric dft: k (and n of basis function) will go from -N/2 to N/2 instead of 0 to N. is the same concept just better fro plotting
# FOR COMPLETE EXPLANATION OF HOW DFT IS WORKING SEE THE NORMAL FUNCTION:  dft()
def dft_symm(N, x_n):

    print('Calculating dft...')

    x_k = np.array([], dtype=np.complex128)     # in case of using np.append
    kv = np.arange(-N/2, N/2, dtype=int)
    
    for k in kv:
        #basis = basis_func_symm(N,k)    # basis func symm uses -N/2, N/2 instead of 0 to N for n. I think its the same thing. to make symm only k should be -N/2 to N/2
        basis = basis_func(N, k)       # same result as symmetric basis function. since at the end the muliplication is just between two series of data basis amd x_n
        
        #!! x_k[k] = sum(basis * x_n)      # this does not work since indexing in negative does not mean anything
        x_k =  np.append(x_k, sum(x_n * basis))   # can be used instead of indexing but same result (in time consumption)

    x_k_abs = np.absolute(x_k)              # array of result of investigation, with each investigating frequency (k) of basis function. showing magnitude of present sinusoid in x_n
    
    return x_k, x_k_abs                     # returning an array; for each frequency investigating k, both result (res) and magnitude of result (mag)

# Constructing the Sinusoid from available frequencies in the spectrum x_k (idft)
def idft(N,x_k):

    print('Calculating inverse dft')

    x_n_constructed = np.zeros(N)                           #in case x_k is coming from a real signal (like cosine) the result should be an array of real values.
    
    for k in range(N):
        basis = basis_func_Inv(N,k)                             #retuns an array of basis function with specific k as input and with element varying with n
        x_n_constructed[k] = sum(basis * x_k)/N
    
    return x_n_constructed



#### The development both in main and basis function is changed!!:
###### Lets look at idft in another and maybe in a better way...
###### Instead of treting it like dft, in the basis function for each n we calculate basis function for all possible k's.
###### you can see this basis function as a circular motion of a unit length roatating with increase of k (mirror opposite of basis of dft)
###### Then in the main function for each n we calcualte the basis function and multiply it by x_k
###### THIS IS BETTER SINCE IT ALSO SHOWS WHAT IT MEANS TO PERFORM INVERSE OPERATION IN GENERAL MEANING!
# symmetric idft: in case of use of dft_symm() should be used
def idft_symm(N,x_k):

    print('Calculating inverse dft')

    x_n_constructed = np.array([], dtype=np.float32)         
    #nv = np.arange(-N/2, N/2, dtype=int)

    for n in range(N):
        basis = basis_func_Inv_symm(N,n)                             #if used dft_symm (regardless of symm or normad basis of dft), this should be used for idft
        x_n_constructed =np.append(x_n_constructed, 1.0/N * sum(basis * x_k))
    
    return x_n_constructed

