import numpy as np

def cantilever_deflection(K, F_inp):
   
    n_DOF = K.shape[0]
    n_nodes = n_DOF // 2

    F_inp = np.atleast_2d(F_inp)
    if F_inp.shape[0] != n_nodes:
        if F_inp.shape[1] == n_nodes:
            F_inp = F_inp.T
        else:
            raise ValueError("F_inp shape does not match number of nodes in K.")

    n_cases = F_inp.shape[1]

    F = np.zeros((n_DOF, n_cases))
    for i in range(n_cases):
        # place transverse forces at even DOFs (0,2,4,...)
        F[::2, i] = F_inp[:, i]

    K_red = K[2:, 2:]
    F_red = F[2:, :]

    results = np.linalg.solve(K_red, F_red)
    print(results)

    defln = np.zeros((n_nodes, n_cases))
    slope = np.zeros((n_nodes, n_cases))

    for i in range(1, n_nodes):  # start from 1 because node 0 is fixed
        defln[i, :] = results[2*(i-1), :]    # transverse displacement
        slope[i, :] = results[2*(i-1)+1, :]  # rotation
 

    return defln, slope
