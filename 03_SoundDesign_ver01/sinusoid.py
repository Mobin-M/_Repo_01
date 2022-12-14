import numpy as np

def Discrete_Real_Sinusoid_1(A, phi, f0, fs=44100, t_len=1):

    # A     :   (float) amplitudes of constructing sinusoids [] 
    # phi   :   (float) phases of constructing sinusoids [rad]
    # f0    :   (float) continuous-time frequencies of constructing sinusoids [cycle/sec]
    # fs    :   (int) sampling frequency [sample/sec]
    # t_len :   (float) time length to construct signal [sec]

    #### constructing information
    fd = f0/fs         # frequency of input CT sinusoids, discretized [cycle/sample]. Note that unit of 2*pi*fd is [rad/sample]


    #### smapling time t -> nts
    ts = 1/fs
    t = np.arange(0, t_len, ts)     #discretized array of time [sec]
    n = t/ts                        #corresponding array of samples []

    N = len(n)      # number of samples
    m = N*fd        # m should be calculated 
    
    # x_t = A*exp(1j*2*pi*f0*t + phi)   ------>   x_n = A*exp(2*pi*fd*n + phi)
    x_n = A*np.cos(2*np.pi*fd*n + phi)     #x_n_array is each constucting sinusoid in discrete time before summing up all together
    
    #returning constructed signal: Note that later, for a dft or a dtfs, this will be just an array of values with a length N.
    return(N, m, x_n)