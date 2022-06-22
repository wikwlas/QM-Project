#paczka gaussowska
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
from scipy.integrate import dblquad
from matplotlib.animation import PillowWriter
#constants------------------------
a = 1 #nm
b = 1
hc = 1
hbc = 1
m = 1
pi = np.pi

time  = 0


number = 2
nx = [1, 3, 2, 4]
ny = [2, 1, 1, 1]

nx = [1, 2]
ny = [2, 1]

x = np.arange(0, a, 0.01)
y = np.arange(0, b, 0.01)
xp, yp = np.meshgrid(x, y)

PSI=0
Coefficient = []
cbaractive = True

#simualtion--------------------------------------------------------------------------------------------------------------
def Psi(nxx, nyy, t):
    Ex = nxx**2*hbc**2*np.pi**2/(2*m*a**2)
    Ey = nyy**2*hbc**2*np.pi**2/(2*m*b**2)
    E = Ex + Ey
    psi = np.real((2/np.sqrt(a*b))*np.sin(nxx*pi*xp/a)*np.sin(nyy*pi*yp/b)*np.exp(-1j*E*t/(hbc**2)))
    return psi
def Coefficients():
    c2 = 1/(number+1)
    Coefficient.append(2*np.sqrt(c2))
    for i in range (number):
	    Coefficient.append(np.sqrt(c2))
def animate(i):
    global time
    global PSI
    global cbaractive
    #print(time) ok
    Coefficients()
    for i in range(number):
	    PSI = PSI+Coefficient[i]*Psi(nx[i], ny[i], time)
    cs = ax.contourf(xp, yp, PSI, levels = 20, cmap = cm.pink)
    if cbaractive:
        cbar = fig.colorbar(cs, label = 'psi')
        cbaractive = False
    time = time+0.01
    #print("show")
if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Particle in an Infinite 2D Square Well -> non-stationary states')
    ax.set_xlabel('x [nm]')
    ax.set_ylabel('y [nm]')
    ani = animation.FuncAnimation(fig, animate, frames = 600, interval = 100, blit = False)
    plt.show()
    # writer = PillowWriter(fps=60)
    # ani.save("Square_well_non_stationary_states.gif", writer=writer)


