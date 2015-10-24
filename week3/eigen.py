import numpy as np

if __name__ == '__main__':
    matrix = [[2,-1,-1,0,0,0],
             [-1,3,0,-1,0,-1],
             [-1,0,2,-1,0,0],
             [0,-1,-1,3,-1,0],
             [0,0,0,-1,2,-1],
             [0,-1,0,0,-1,2]]
    mat = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    print("---- EigenValues ----")
    print(eigenvalues)
    print("---- EigenVectors ----")
    print(eigenvectors)

    print("Second smallest eigenvalue")
    ss = np.argmin(eigenvalues)
    eigenvalues[ss] = float("Inf")
    print(eigenvalues)
    arg_min = np.argmin(eigenvalues)
    val_min = min(eigenvalues)
    print("Value = {0}, Index = {1}".format(val_min, arg_min))
    print("EigenVector corresponding to second smallest eigenvalue")
    x2 = eigenvectors[:,arg_min]
    print(x2)
    m = sum(x2)/len(x2)
    print("Mean value = {0}".format(m))
    print(x2 < m)