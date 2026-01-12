import matplotlib.pyplot as plt
import numpy as np
#plotting the FA modes of the tower at various eigen vectors
mode_nos = [0, 1]

def plot_mode_graph(mode_shapes,tower_freq,H):
    plt.figure()
    plt.grid(True)

    for i, mode in enumerate(mode_nos):
       mode_shape_full = np.concatenate(([0.0], mode_shapes[:, mode]))

       plt.plot(
        H,
        mode_shape_full,
        linewidth=2,
        label=f"{tower_freq[mode]:.3f} Hz"
        )

    plt.legend(loc="upper left")
    plt.xlabel("Tower Height (m)")
    plt.ylabel("Eigen Vectors")
    plt.title("Tower FA Mode Shapes")
    plt.show()





