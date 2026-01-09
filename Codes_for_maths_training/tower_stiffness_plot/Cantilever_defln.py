import numpy as np

def cantilever_deflection(Kfa,Forces):
    if(Forces.shape[0]==Kfa.shape[0]//2):
        F = np.zeros(Kfa.shape[0],Forces.shape[1])
        for i in range(Forces.shape[1]):
            F = np.zeros((2 * Forces.shape[0], Forces.shape[1]))
            for i in range(Forces.shape[1]):
                 F[0::2, i] = Forces[:, i]  
                 F[1::2, i] = 0 
    else:
        F = Forces

                
             