import matplotlib.pyplot as plt
import numpy as np

n = 300000 #number of points to plot randomly 
#note: the graph explodes past dist > 2 or dist < 0. 
dist = 2/3 #distance away from a randomly chosen vertex 
r = 2  # side length of the hexagon 

hex_x = [0, r, 1.5*r, r, 0, -0.5*r,0]
hex_y = [0, 0, r*np.sqrt(3)/2, r*np.sqrt(3), r*np.sqrt(3), r*np.sqrt(3)/2,0] #coordinates of the hexagon

rand_point_x = np.random.rand(1)*2*r - 0.5*r #random point in the hexagon
#getting the random y-coordinate within the hexagon given the x-coordinate
if rand_point_x >= 0 and rand_point_x <= r:
    rand_point_y = np.random.rand(1) * r*np.sqrt(3)
elif rand_point_x < 0: 
    y_low = -1*np.sqrt(3)*rand_point_x 
    y_hi = np.sqrt(3)*rand_point_x + np.sqrt(3) * r
    y_len = y_hi - y_low 
    rand_point_y = np.random.rand(1)*y_len + y_low 
else: 
    y_low = np.sqrt(3)*rand_point_x - np.sqrt(3)*r
    y_hi = -1*np.sqrt(3)*rand_point_x + 2*np.sqrt(3)*r
    y_len = y_hi - y_low 
    rand_point_y = np.random.rand(1)*y_len + y_low 

print(rand_point_x, rand_point_y)

plt.plot(hex_x, hex_y) # plot the hexagon and the random point
plt.plot(rand_point_x, rand_point_y, 'o', color= 'g', markersize= 3)
xx = []
yy = []
#find length to distance between the random point and a random vertex 
#and go dist of the way there. Repeat with new point. 
for i in range(n): 
    rand_vert = np.random.randint(0,6)
    x_vert = hex_x[rand_vert]
    y_vert = hex_y[rand_vert]
    if i == 0: 
        x1 = rand_point_x
        y1 = rand_point_y
    else: 
        x1 = xx[i-1]
        y1 = yy[i-1]
    x2 = dist*(x_vert - x1) + x1 
    y2 = dist*(y_vert - y1) + y1 
    xx.append(x2)
    yy.append(y2)
#plot the points generated 
plt.plot(xx,yy,'o', color= 'r', markersize = 0.5)
plt.show()