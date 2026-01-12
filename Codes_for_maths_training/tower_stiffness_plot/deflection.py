import matplotlib.pyplot as plt
import numpy as np
from stiffness_matrix import stiff_mat
import math 
from Cantilever_defln import cantilever_deflection 
from mass_matrix import mass_mat
from scipy.linalg import eigh  
from Plot_mode_graph import plot_mode_graph


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

kfa = stiff_mat(E,Ifa,ele_L)

load = np.zeros(len(H))

thrust  = 2*1.225*math.pi*61.5*61.5*wind_speed*wind_speed*(1-0.5)

load[-1] = thrust

def plot_nodes_before_deflection():
    plt.figure()
    plt.plot(np.zeros_like(H), H, 'x-', label='Tower')
    plt.ylabel('Tower height (m)')
    plt.xlabel('Transverse Deflection (m)')
    plt.grid(True)
    plt.xlim([-2, 2])
    plt.show()

plot_nodes_before_deflection()


def plot_traverse_deflection(H, Traverse_deflection, thrust):
    plt.figure()
    plt.plot(Traverse_deflection[:, 0], H, 'x-', label='Deflected Tower')
    plt.xlabel('Transverse Deflection (m)')
    plt.ylabel('Tower Height (m)')
    plt.title(f'Transverse deflection because of thrust of {thrust:.0f} N')
    plt.grid(True)
    plt.legend()
    plt.show()

Traverse_deflection, slope = cantilever_deflection(kfa, load)
plot_traverse_deflection(H, Traverse_deflection, thrust)

m = mu[1:]  
Mg = mass_mat(m, ele_L)
kfa = kfa[2:, 2:]
Mg = Mg[2:, 2:]

# Solve eigenvalue problem
lambda_vals, V = eigh(kfa, Mg)  # kfa = stiffness, Mg = mass
print("Eigenvalues:", lambda_vals)

# Keep only positive (physical) eigenvalues
valid_indices = lambda_vals > 1e-6

lambda_valid = lambda_vals[valid_indices]
V_valid = V[:, valid_indices]   

# Convert to rad/s
omega_vals = np.sqrt(lambda_valid)

# Convert to Hz
f_natural = omega_vals / (2 * math.pi)
print("Natural frequencies (Hz):", f_natural)


modes_FA = V_valid            

# Select translational DOFs only (every 2nd DOF)
translational_dofs = np.arange(0, modes_FA.shape[0], 2)

# Tower bending frequencies (modal → no DOF indexing needed)
tower_freq = f_natural

# Translational mode shapes
mode_shapes = modes_FA[translational_dofs, :]

plot_mode_graph(mode_shapes,tower_freq,H)
