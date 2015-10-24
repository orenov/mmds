import math
import sys
import numpy as np
import scipy.sparse

class PageRank():
    def __init__(self, filename, num_nodes, beta, epsilon):
        self.filename  = filename
        self.num_nodes = num_nodes
        self.matrix    = scipy.sparse.coo_matrix((self.num_nodes, self.num_nodes))
        self.beta      = 0.2
        self.count     = 0
        self.d         = {}
        self.epsilon   = epsilon
        pass

    def check(self, elem):
        if elem in self.d:
            return(self.d[elem])
        self.d[elem] = self.count
        self.count += 1
        return(self.count-1)

    def readData(self):
        rows = []
        cols = []
        with open(self.filename) as f:
            next(f); next(f); next(f); next(f);
            for line in f:
                ar = line.split('\t')
                #i = int(ar[0])
                #j = int(ar[1])
                i = self.check(int(ar[0])) #d.get(key, 0)
                j = self.check(int(ar[1])) #d.get(key, 0)
                rows.append(i)
                cols.append(j)
                #print("\r--- Completed nodes {0}\t i = {1} \t j = {2} \t normaliz_coef = {3}.".format(self.count, i, j, self.normaliz_coef[i]))
        data        = [1.] * len(rows)
        self.num_nodes = max(max(rows), max(cols)) + 1
        print(self.num_nodes)
        print(max(cols))
        self.matrix = scipy.sparse.coo_matrix((data, (cols, rows)), shape=(self.num_nodes, self.num_nodes))
        
        self.in_links     = np.array(self.matrix.sum(axis = 1))[:,0]
        self.out_links    = np.array(self.matrix.sum(axis = 0))[0,:]
        ri, ci            = self.matrix.nonzero()
        self.matrix.data /= self.out_links[ci]
        print(self.matrix)
        
        #rsums = np.array(self.matrix.sum(0))[:,0]
        #print(rsums)
        #print("{0} and {1}".format(ri, ci))
        
        # Dead end Fix
        #self.out_links = np.array(self.matrix.sum(axis = 1))[:,0]
        #self.in_links  = np.array(self.matrix.sum(axis = 0))[0,:]
        #self.matrix = self.matrix / self.out_links
        #print(self.out_links)
        #print(self.in_links)
        #for i, ss in enumerate(x):
        #    if ss == 0:
        #        self.matrix[:,i] = np.ones((self.num_nodes,)) / self.num_nodes
        #print(self.matrix)
        

    def fit_power_iterations(self):
        r1   = np.array([1./self.num_nodes] * self.num_nodes, dtype = np.float32)
        dist = 1
        
        print("--------Init ---------")
        i = 1
        print(r1)

        while dist > self.epsilon:
            print("----------- Iteration #{0} ---------".format(i))
            temp =  self.beta * (self.matrix.dot(r1.T))
            temp += [ (1.-self.beta) / self.num_nodes ] * self.num_nodes
            
            r0   = r1
            r1   = temp + [(1-sum(temp))/ self.num_nodes] * self.num_nodes

            dist = np.linalg.norm(r0-r1, ord = 1)
            print(r1)
            print(dist)
            print(sum(r1))
            i += 1
            print("%.5g" % round(r1[99], 10))
            if i > 40:
                break
            
        self.solution = r1

    def print_solution(self):
        print(self.solution)
        print("%.5g" % round(self.solution[self.check(99)], 10))

if __name__ == '__main__':
    data      = "../data/web-Google.txt"
    num_nodes = 875713
    beta      = 0.2
    epsilon   = 1e-20
    
    pr = PageRank(data, num_nodes, beta, epsilon)
    pr.readData()
    pr.fit_power_iterations()
    pr.print_solution()
    pass