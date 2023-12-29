import numpy as np
import matplotlib.pyplot as plt

a_const = -0.744 + 0.148*1j
DIMENSIONS= 2000
MAX_ITERATIONS= 300


def julia_set(h_range, w_range, iterations, a): 
    '''
    Function that returns when the complex number diverges in the julia set
    Inputs: 
    h_range: float for the range of the height in pixels 
    w_range: float for the range of the width in pixels
    a: complex number in the julia set a  
    iterations: int for the number of iterations
    Output: 
    array of integers with the number of iterations before becoming unbounded 
    '''

    y, x = np.ogrid[1.4:-1.4:h_range*1j, -1.4:1.4:w_range*1j]

    z_array = x + y*1j #complex numbers

    iter_til_diverge = iterations + np.zeros(z_array.shape)

    #truth array
    not_diverge = iter_til_diverge < (100 + iterations) 
    #false array 
    already_diverge = iter_til_diverge > (100+ iterations)

    for  i in range(iterations):
        z_array = z_array**2 + a #julia set equation 
        z_size = z_array * np.conj(z_array) #finding out if z_array is getting bigger
        diverge_check = z_size > 4  #check for divergence, happens when complex * conjugate > 4

        diverged_here = diverge_check & not_diverge #which diverged in this iteration

        iter_til_diverge[diverged_here] = i         #set the number that it iterated

        not_diverge = np.invert(diverged_here) & not_diverge #update not_diverged

        already_diverge = already_diverge | diverged_here #update diverged

        z_array[already_diverge] = 0 #reset to zero

    return iter_til_diverge

plt.imshow(julia_set(DIMENSIONS,DIMENSIONS, MAX_ITERATIONS, a_const), cmap= 'twilight_shifted', extent=[-1.4, 1.4, -1.4, 1.4])

plt.axis('off')
plt.show()
