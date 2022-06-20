import numpy as np
import scipy.integrate as integrate
from matplotlib import pyplot
import matplotlib.animation as animation
import sympy as sp
import matplotlib.cm as cm
from IPython.display import HTML
import networkx as nx
from matplotlib.animation import PillowWriter
from matplotlib.animation import FuncAnimation, writers
from IPython import display
# constants-------------------------------------
L = 10 #wybrane
h_cross = 1 #hbc
m = 1
xpos = np.linspace(0, L, 50)
ypos = np.linspace(0, L, 50)

A = 0.4 #przypadkowe
sigma = np.sqrt(10)
k0 = 0.2
x0 = 2 #wybrane
y0 = 2 #wybrane
time = 0

cbaractive = True

#Initial wave function of the particle (not normalised)---------------------------------------------------
def psi0(x):
    if(x <= L and x >= 0):
        return A*np.exp(-((x-xo)**2)/2*sigma)*np.exp(complex(k0*x))
    else:
        return 0

def psi0(y):
    if(y <= L and y >= 0):
        return A*np.exp(-((y-y0)**2)/20)*np.exp(complex(k0*y))
    else:
        return 0

#stationary states (time independent part)----------------------------------------------------------
def psi_nx(x, nx):
    # stany stacjonarne niezależne
    if(x >= 0 and x <= L):
        return np.sqrt(2/L)*np.sin(nx*np.pi*x/L)
    else:
        return 0

def psi_ny(y, ny):
    # stany stacjonarne niezależne
    if(y >= 0 and y <= L):
        return np.sqrt(2/L)*np.sin(ny*np.pi*y/L)
    else:
        return 0

#coefficients (first 30 states)-----------------------------------------------------------------------
cx = np.zeros(30, dtype = np.complex_)
cy = np.zeros(30, dtype = np.complex_)

#calculate co-efficients using fourier's trick--------------------------------------------------------
for i in range(30):
    nx = i + 1
    I_Real = lambda x: psi_nx(x, nx)*np.real(psi0(x))
    I_Imag = lambda x: psi_nx(x, nx)*np.imag(psi0(x))
    cx[i] = complex(integrate.quad(I_Real, 0, L)[0],integrate.quad(I_Imag, 0, L)[0])

for i in range(30):
    ny = i + 1
    I_Real = lambda y: psi_ny(y, ny)*np.real(psi0(y))
    I_Imag = lambda y: psi_ny(y, ny)*np.imag(psi0(y))
    cy[i] = complex(integrate.quad(I_Real, 0, L)[0],integrate.quad(I_Imag, 0, L)[0])

#Wave function at time t------------------------------------------------------------------------------------------
def PSI_X(x, t):
    val = 0
    for i in range(30):
        nx = i+1
        val += cx[i]*psi_nx(x, nx)*np.exp(complex(0,-(nx**2)*(np.pi**2)*h_cross*t/(2*m*(L**2))))

    return val

def PSI_Y(y, t):
    val = 0
    for i in range(30):
        ny = i+1
        val += cy[i]*psi_ny(y, ny)*np.exp(complex(0,-(ny**2)*(np.pi**2)*h_cross*t/(2*m*(L**2))))

    return val

def sum_PSI(t):
    val = 0
    PSI_compl = []

    for i in range(0, 50):
        PSI_compl.append([])
        for j in range(0, 50):
            PSI_compl[i].append(np.abs(PSI_X(xpos[i], t)*PSI_Y(ypos[j], t))**2)
    #print(PSI_compl)
    return PSI_compl
	
def plot_probability(i):
    global cbaractive
    cs = ax.contourf(xp, yp, sum_PSI(i/10), levels = 30, cmap = cm.pink)
    if cbaractive:
        cbar = fig.colorbar(cs, label = 'psi')
        cbaractive = False
    return cs
	
if __name__ == "__main__":
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    xp, yp = np.meshgrid(xpos, ypos)
    anim = animation.FuncAnimation(fig, plot_probability, frames = 100, interval=20, blit = False)
    #writer = PillowWriter(fps=60)
    #anim.save("sine_example.gif", writer=writer)
    pyplot.show()
	
	
