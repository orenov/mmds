import numpy as np

if __name__ == '__main__':
    print("------ Question 1 ------")
    v = [2./7, 3./7, 6./7]

    c1 = [.954, .728, -.682]
    c2 = [-.937, .312, .156]
    c3 = [.429, .857, .286]
    c4 = [.485, -.485, .728]
    c = [c1, c2, c3, c4]

    for vec in c:
        print(vec)
        print("Norm = {0}, Dot = {1}".format(np.dot(vec,vec), np.dot(vec,v)))

    print("----- Question 2 ------")
    print("----- On white paper -----")
    print("----- Question 3 ------")

    matrix = [[1,1],
              [2,2],
              [3,4]]
    matrix = np.array(matrix)
    print(np.dot(matrix, matrix.T))
    eigenvalue, eigenvectors = np.linalg.eig(np.dot(matrix, matrix.T))
    print(eigenvalue)
    print(eigenvectors)
    print("----- Question 4 ------")
    v = [1., 2., 3.]

    c1 = [-2, 3, -1]
    c2 = [1, -2, 1]
    c3 = [1, 0, 0]
    c4 = [1, 1/2, 1/3]
    c = [c1,c2,c3,c4]
    for vec in c:
        print(vec)
        print("Dot = {0}".format(np.dot(vec,v)))






