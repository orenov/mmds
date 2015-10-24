import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine

if __name__ == '__main__':
    matrix = [ [1,2,3,4,5],
               [2,3,2,5,3],
               [5,5,5,3,2]]
    matrix = np.array(matrix)
    
    row_sums = matrix.mean(axis = 1)
    print(row_sums)
    matrix   = matrix - row_sums[:, np.newaxis]
    print(matrix)
    col_sums = matrix.mean(axis = 0)
    print(col_sums)
    matrix   = matrix - col_sums[np.newaxis, :]
    print("-------Question 1 ---------")
    print(matrix)

    matrix = [[1,0,1,0,1,2],
              [1,1,0,0,1,6],
              [0,1,0,1,0,2]]
    matrix = np.array(matrix)
    alphas = [0, 0.5, 1, 2]
    mapping = {0 : 'A', 1 : 'B', 2 : 'C'}

    for alpha in alphas:
        print("Alpha = {0}".format(alpha))
        new_matrix = matrix.copy()
        new_matrix[:,5] = alpha * new_matrix[:,5]
        #print(new_matrix)
        for i in range(matrix.shape[0]):
            for j in range(i+1, matrix.shape[0]):
                print("d({0},{1}) = {2}".format(mapping[i], mapping[j], cosine(new_matrix[i,:], new_matrix[j,:])))