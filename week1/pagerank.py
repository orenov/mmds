import numpy as np
import sys
from sklearn.preprocessing import normalize


class PageRank:
    # matrix -> link matrix
    # beta   -> teleport activation probability
    # sumeq  -> to identify uniq ranks solution we need
    # to know exact sum of this ranks. By default it's equal 1.
    # starting_Value -> init for power iterations
    def __init__(self, matrix, beta, sumeq = 1, starting_value = "default"):
        self.A     = normalize(matrix, axis=0, norm='l1')
        self.N     = self.A.shape[0]
        self.A     = self.dead_end_fix(self.A)
        self.beta  = beta
        self.sumeq = sumeq
        self.A_cor = beta * self.A + (1 - beta) * np.ones([self.N]*2) / self.N
        self.epsilon = 0.001
        self.starval = starting_value
        print(self.A)
        print("--------------")
        print(self.A_cor)
        
    def fit_power_iter(self):
        r0 = np.array([0] * self.N)
        if self.starval == "default":
            r1 = np.array([1./self.N] * self.N)
        else:
            r1 = np.array([self.starval] * self.N)
        dist = np.linalg.norm(r0-r1, ord = 1)
        print("--------Init ---------")
        print(dist)
        print(r1)
        i = 1
        while dist > self.epsilon:
            print("----------- Iteration #{0} ---------".format(i))
            i += 1
            temp = self.A_cor.dot(r1)
            r0 = r1
            r1 = temp.reshape((3,1))
            dist = np.linalg.norm(r0-r1, ord = 1)
            print(dist)
            print(r1)
        self.solution = r1

    def print_final_sol(self):
        print("----- Final Solution ------")
        print(self.sumeq/sum(self.solution) * self.solution)

    def dead_end_fix(self, matrix):
        x = matrix.sum(axis = 0)
        for i, ss in enumerate(x):
            if ss == 0:
                matrix[:,i] = np.ones((self.N,)) / self.N
        return(matrix)

    def print_equations(self):
        print("------ Equations ------")
        print(self.A_cor - np.eye(self.N))

if __name__ == "__main__":
    m = np.matrix([[0.,1.,1.], [0.,0.,1.], [1.,0.,0.]])
    t = PageRank(m, 1, 1, 1)
    t.fit_power_iter()
    t.print_final_sol()
    t.print_equations()

