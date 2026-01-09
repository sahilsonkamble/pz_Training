import matplotlib.pyplot as plt
import numpy as np
from stiffness_matrix import stiff_mat
import math 
from Cantilever_defln import cantilever_deflection 

# Data
H = [0, 8.76, 17.52, 26.28, 35.04, 43.8, 52.56, 61.32, 70.08, 78.84, 87.6]
mu = [5590.87, 5232.43, 4885.76, 4550.87, 4227.75, 3916.41, 3616.83, 3329.03, 3053.01, 2788.75, 2536.27]
E = [2.1E+11, 2.1E+11, 2.1E+11, 2.1E+11, 2.1E+11 ,2.1E+11, 2.1E+11, 2.1E+11, 2.1E+11 ,2.1E+11 ,2.1E+11] 
Ifa = [2.925428571 ,2.546761905 ,2.206047619, 1.900619048 ,1.628, 1.385761905, 1.171571429, 0.983142857, 0.818333333, 0.675142857 ,0.55152381]

#numerical integration method to find the total mass
def trapezoidal_integral(x, y):
    integral = 0
    for i in range(len(x) - 1):
        base = x[i+1] - x[i]
        integral += base * (y[i] + y[i+1]) / 2
    return integral

def total_mass(mu, H):
    return trapezoidal_integral(H, mu)  # integrate mu over height

def mu_vs_H(H, mu):
    fig, ax = plt.subplots()
    ax.plot(H, mu, label=f"Total Mass = {total_mass(mu, H):.2f} kg")
    ax.set_title("Height vs Mass Density of the Tower")
    ax.set_ylabel("Mass per unit height (kg/m)") 
    ax.set_xlabel("Height (m)")
    ax.legend() 
    plt.show()

mu_vs_H(H, mu)


ele_L = []
for i in range(len(H) - 1):  # loop from 0 to len(H)-2
    length = H[i+1] - H[i]    # difference between consecutive nodes
    ele_L.append(length)      # add length to the list


wind_speed = 10

kfa = stiff_mat(E[2:],Ifa[2:],ele_L[2:])

load = np.zeros(len(H))

thrust  = 2*1.225*math.pi*61.5*61.5*wind_speed*wind_speed*(1-0.5)

load[-1] = thrust

def plot_nodes_before_deflectiom():
    plt.figure()
    plt.plot(np.zeros_like(H), H, 'x-', label='Tower')
    plt.ylabel('Tower height (m)')
    plt.xlabel('Transverse Deflection (m)')
    plt.grid(True)
    plt.xlim([-2, 2])
    plt.show()

plot_nodes_before_deflectiom()


def plot_traverse_deflection():
    Traverse_deflection = cantilever_deflection(kfa,load)
    plt.plot(Traverse_deflection,H,'x-')
    plt.title(f"Traverse deflection because of thrust of %0.0f N",load(len(load)))




