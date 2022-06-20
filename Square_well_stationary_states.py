#Schrodinger solution plot stationary states 2D
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
from matplotlib.animation import PillowWriter
#constants------------------------
a = 1 #nm
b = 1
hbc = 1
m = 1
pi = np.pi

time  = 0
#quantum_numbers-------------------------------------------------------------------------------------------------------
nx = 3
ny = 3

x = np.arange(0, a, 0.01)
y = np.arange(0, b, 0.01)
xp, yp = np.meshgrid(x, y)

Ex = nx**2*hbc**2*np.pi**2/(2*m*a**2)
Ey = ny**2*hbc**2*np.pi**2/(2*m*b**2)
E = Ex + Ey
	
psi = np.real((2/np.sqrt(a*b))*np.sin(nx*pi*xp/a)*np.sin(ny*pi*yp/b)*np.exp(-1j*E*time/(hbc**2)))

#simualtion--------------------------------------------------------------------------------------------------------------
def animate(i):
    global time
    psi = np.real((2/np.sqrt(a*b))*np.sin(nx*pi*xp/a)*np.sin(ny*pi*yp/b)*np.exp(-1j*E*time/(hbc**2)))
    cs = ax.contourf(xp, yp, psi, levels = 20, cmap = cm.pink)
    time = time+0.005

if __name__ == "__main__":
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(111)
    cs = ax.contourf(xp, yp, psi, levels = 20, cmap = cm.pink)
    cbar = fig.colorbar(cs, label = 'psi')
    ax.set_title('Particle in an Infinite 2D Square Well -> stationary states')
    ax.set_xlabel('x [nm]')
    ax.set_ylabel('y [nm]')
	
    ani = animation.FuncAnimation(fig, animate, frames = 600, interval=100, blit = False)
    #writer = PillowWriter(fps=60)
    #ani.save("Square_well_stationary_states.gif", writer=writer)
    plt.show()
