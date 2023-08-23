from click import pause
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 1000) # movement time
theta = np.linspace(0, np.pi , 200)  #only half of the circle

r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #values for our radii 
speed = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5] #the speed of each semi-circle

rmax = max(r)+3 #maximum radius plus 3 to zoom out in the axis

#interactive plot initialization
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

#plot the semi-circles 
for i in t: #movement time
    for j in range(len(r)): #create each semi-circle 
        tempx = r[j]*np.cos(theta + i * speed[j]) 
        tempy = r[j]*np.sin(theta + i * speed[j])
        ax.plot(tempx, tempy, color = 'black', linewidth=5)
        plt.draw()    
    plt.pause(0.01)
    plt.cla()
    plt.xlim((-rmax , rmax ))
    plt.ylim((-rmax , rmax ))


    
    