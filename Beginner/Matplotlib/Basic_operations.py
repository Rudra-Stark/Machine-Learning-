import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, 'r')
plt.xlabel('angle')
plt.ylabel('sine values')
plt.title('sine wave')
plt.show()

# for Parabola 
x = np.linspace(-10,10,20)
y = x**2
plt.plot(x,y)
plt.show()

#-------------------------------------

x = np.linspace(-5, 5, 50)
plt.plot(x, np.sin(x), 'g-')
plt.plot(x, np.cos(x), 'r--')
plt.show()

#-------------------------------------

fig = plt.figure()
ax = plt.axes(projection = '3d')
z = 20 * np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x, y, z, c = z, cmap = 'Greens' )
plt.show()
