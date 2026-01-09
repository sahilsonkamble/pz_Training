import numpy as np
def stiff_mat(E, Ifa, ele_L):
    nDOF = 3
    n = len(ele_L)  # number of elements
    Ke = np.zeros((n, 2*nDOF, 2*nDOF))

    # Loop over all elements
    for i in range(n):
        L_i = ele_L[i]
        factor = E[i] * Ifa[i] / L_i**3
        Ke[i] = factor * np.array([
            [12, 6*L_i, -12, 6*L_i],
            [6*L_i, 4*L_i**2, -6*L_i, 2*L_i**2],
            [-12, -6*L_i, 12, -6*L_i],
            [6*L_i, 2*L_i**2, -6*L_i, 4*L_i**2]
        ])

    if n == 1:
        Kg = Ke[0]
    else:
        Kg = np.zeros((n*nDOF + nDOF, n*nDOF + nDOF))
        Kg[0:2*nDOF, 0:2*nDOF] = Ke[0]
        for j in range(1, n):
            ids = slice(j*nDOF, (j+2)*nDOF)
            Kg[ids, ids] += Ke[j]

    return Kg, Ke
