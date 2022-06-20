#simulation in 3D
from math import sin, pi,cos
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.cm as cm
from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons
from colorspacious import cspace_converter
from tkinter import *
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
#constants------------------------
#a = 1 #nm
#b = 1
hbc = 1
m = 1
pi = np.pi

time  = 0
nx = 3
ny = 3
L = 1

x = np.linspace(0, L, 100)
y = np.linspace(0, L, 100)
X,Y= np.meshgrid(x, y)

Ex = nx**2*hbc**2*np.pi**2/(2*m*L**2)
Ey = ny**2*hbc**2*np.pi**2/(2*m*L**2)
E = Ex + Ey
	
psi = np.real((2/np.sqrt(L*L))*np.sin(nx*pi*x/L)*np.sin(ny*pi*y/L)*np.exp(-1j*E*time/(hbc**2)))
#simulation-----------------------------------------------------------------------------------------------------------
def Psi_3d(a, b, t):
    psi_3d = np.real((2/np.sqrt(L*L))*np.sin(nx*pi*a/L)*np.sin(ny*pi*b/L)*np.exp(-1j*E*t/(hbc**2)))  
    return psi_3d	
	
def animate(i, Z, line):
    global time
    Z = Psi_3d(X, Y, time)
    ax.clear();
    ax.set_zlim(-2, 2)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_title('Particle in an Infinite 2D Square Well -> stationary states')
    line = ax.plot_surface(X, Y, Z, cmap = cm.twilight, linewidth =0.5)
    time = time+0.005
    return line,
	
if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-2, 2)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    Z = Psi_3d(X, Y, time)
    line = ax.plot_surface(X, Y, Z, cmap = cm.twilight, linewidth = 0.5)
    ani = animation.FuncAnimation(fig, animate, fargs = (Z, line), frames = 600, interval=100)
    #writer = PillowWriter(fps=60)
    #ani.save("Square_well_stationary_states_3D.gif", writer=writer)	
    plt.show()