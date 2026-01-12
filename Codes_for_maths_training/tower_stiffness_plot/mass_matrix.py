import numpy as np

def mass_mat(m,ele_L):
    n = len(ele_L)
    nDOf= 2
    Me = np.zeros((n, 2*nDOf, 2*nDOf))
    for i in range(n):
        L_i = ele_L[i]
        factor = m[i] * ele_L[i] / 420
        Me[i] = factor * np.array([
            [156, 22*L_i, 54, -13*L_i],
            [22*L_i, 4*L_i**2, 13*L_i, 2*L_i**2],
            [54, 13*L_i, 156, -22*L_i],
            [-13*L_i, -3*L_i**2, -22*L_i, 4*L_i**2]
        ])
    m = m[:]
    ele_L = ele_L[:]
    if(len(m)==1):
        m = np.tile(m, (len(ele_L), 1))

    Me = np.zeros((n, 4, 4))  # initialize array for element mass matrices

    #building each element mass matrix

    for i in range(n):
        factor = m[i] * ele_L[i] / 420
        Me[i, :, :] = factor * np.array([
        [156, 22*ele_L[i], 54, -13*ele_L[i]],
        [22*ele_L[i], 4*ele_L[i]**2, 13*ele_L[i], -3*ele_L[i]**2],
        [54, 13*ele_L[i], 156, -22*ele_L[i]],
        [-13*ele_L[i], -3*ele_L[i]**2, -22*ele_L[i], 4*ele_L[i]**2]
    ])
        
    #building the assembled global matrix
        if n == 1:
             Mg = Me[0, :, :]  # squeeze in MATLAB is automatic in Python indexing
        else:
           size = n * nDOf + nDOf
           Mg = np.zeros((size, size))  
           Mg[0:2*nDOf, 0:2*nDOf] = Me[0, :, :]

           for j in range(1, n):
             ids = slice((j)*nDOf, (j+2)*nDOf)  
             Mg[ids, ids] += Me[j, :, :]

    return Mg


