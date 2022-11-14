
# this function returns a sinusoid of time length len (in second), not necessarily periodic in discrete-time
# the input parameters are the intended continuous-time sinusoid information to be constructed in discrete-time
# this function also returns correcsponding N and m of constructed signal, in case they are both integer, returned signal is periodic in discrete-time 
# in the input parameter there is also the option to continue the signal in discrete-time (ignoring len), to return a periodic discrete-time signal
import numpy as np
def Discrete_Real_Sinusoid_1(A, phi, f0, fs, t_len, request_periodic=0):

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

    #### DT sinusoid parameter calculation based on periodicity request
    
    ## if NOT requested to return DT periodic sinusoid
    if(request_periodic == 0):
        print('Not required to be periodic')
        
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

    ## requested to return periodic DT sinusoid
    elif(request_periodic == 1):
        print('Required to be periodic')

        ts = 1/fs
        " Method #1 finding N and calculating m "
        N = 1   # initializing N; neglecting the DC value (N=0)
        m = 0   # initializing m
        # constructing a period of discrete-time signal (calculating N and m) 
        isInt_m = False
        while (isInt_m == False):
            isInt_m = True
            for x in range(len(fd)):
                if ((N*fd[x]).is_integer() == False):
                    isInt_m = False
                    break
            if (isInt_m == False):
                #print("m is not an integer")
                N = N+1
            else:
                #print("m is an integer")
                m = int(N*max(fd))    # m will be number of rotations of the constructing sinusoid with the highest frequency 

        """ 2nd method -- Finding m and calculating N
        N = 0
        m = 1                                       # number of rotation index
        isInt_N = False                             # Check if N in integer-- initialization
        while (isInt_N == False):
            isInt_N = True
            for x in range(len(fd)):
            if ((m/fd[x]).is_integer() == False):
                isInt_N = False
                break
            if (isInt_N == False):
            #print("N = not integer")
            m = m + 1
            else:
            #print("N in an integer")
            N = int(m/fd[0])
        """
        
        n = np.arange(0,N)

        # Constructing the sinusoid    
        x_n_array = np.zeros(len(fd), N)         # initializing an 2D array of dimension len(fd) x N: x_n has len(fd) elements in which each of them has N elements
        
        # x_t = A*exp(1j*2*pi*f0*t + phi)   ------>   x_n = A*exp(2*pi*fd*n + phi)
        for x in range(len(fd)):            #
            x_n_array[x] = A[x]*np.cos(2*np.pi*fd[x]*n + phi[x])
            
        # Summing up all the constructing sinusoids
        x_n = np.zeros((1, N))
        for x in range(len(fd)):
            x_n = x_n + x_n_array[x]
        x_n = x_n[0,:]    
    
    ## else
    else:
        print('What the fuck is going on?')   


    #returning constructed signal: Note that later, for a dft or a dtfs, this will be just an array of values with a length N.
    return(N, m, x_n)