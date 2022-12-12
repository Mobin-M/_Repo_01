import numpy as np

def Discrete_Real_Sinusoid_1(A, phi, f0, fs, t_len):

    # A     :   array of amplitudes of constructing sinusoids [] 
    # phi   :   array of phases of constructing sinusoids [rad]
    # f0    :   array of continuous-time frequencies of constructing sinusoids [cycle/sec]
    # fs    :   sampling frequency [sample/sec]
    # t_len :   time length to construct signal [sec]

    #### constructing information
    fd = [x/fs for x in f0]         # frequency array of input CT sinusoids, discretized [cycle/sample]. Note that unit of 2*pi*fd is [rad/sample]
    fd = np.array(fd)
    A = np.array(A)
    phi = np.array(phi)

    #### smapling time t -> nts
    ts = 1/fs
    t = np.arange(0, t_len, ts)     #discretized array of time [sec]
    n = t/ts                        #corresponding array of samples []

    N = len(n)      # number of samples
    m = N*max(fd)   # m should be calculated for the sinusoid with the highest rotation (max(fd)): N*fd = m

    # Constructing the sinusoid    
    x_n_array = np.zeros((len(fd), N))     # initializing an 2D array of dimension len(fd) x N: x_n has len(fd) elements in which each of them has N elements
    
    # x_t = A*exp(1j*2*pi*f0*t + phi)   ------>   x_n = A*exp(2*pi*fd*n + phi)
    for x in range(len(fd)):            #
        x_n_array[x] = A[x]*np.cos(2*np.pi*fd[x]*n + phi[x])     #x_n_array is each constucting sinusoid in discrete time before summing up all together
        
    # Summing up all the constructing sinusoids
    x_n = np.zeros((1, N))
    for x in range(len(fd)):
        x_n = x_n + x_n_array[x]
    x_n = x_n[0,:]  

    #returning constructed signal: Note that later, for a dft or a dtfs, this will be just an array of values with a length N.
    return(N, m, x_n)