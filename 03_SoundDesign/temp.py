# Global variable
f_comment = 0       # global flag to show flow comments

# Get sinusoid parameter from the user with default values
def get_sin_param():
    if f_comment: print("inside get_sin_param")
    freq = float(input("Please enter the frequency: ") or '0')
    amp = float(input("Please enter the amplitude: ") or '0')
    phi = float(input("Please enter the phase: ") or '0')
    return freq, amp, phi




freq, amp, phi = get_sin_param()
print(freq, amp, phi)