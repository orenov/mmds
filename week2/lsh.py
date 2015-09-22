import random
import sys
import math
import numpy as np

def edit_distance(s, t):
    ''' From Wikipedia article; Iterative with two matrix rows.   '''
    ''' Thanks to Christopher P. Matthews for this implementation '''
    if s == t: return 0
    elif len(s) == 0: return len(t)
    elif len(t) == 0: return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
                
    return v1[len(t)]

def generate_random_hash_func(num, mod):
    func = []
    for i in range(num):
        fun = lambda x: (random.randint(1,10) * x + random.randint(1,10)) % mod 
        func.append(fun)
    return(func)

def min_hash(matrix, order, funcs = None):
    num        = 2
    mod        = matrix.shape[1] + 1
    if funcs == None:
        funcs      = generate_random_hash_func(num, mod)
    fin_sig    = np.empty((num, matrix.shape[1]))
    fin_sig[:] = np.inf
    for i in order:
        vals = [fun(i-1) for fun in funcs]
        sb   = [t for t, x in enumerate(matrix[i-1]) if x != 0]
        for j in sb:
            fin_sig[:,j] = [min(fin_sig[t,j], vals[t]) for t in range(num)] 
        
    return(fin_sig)


def lsh(matrix, bands = 2, bits = 10): #signature matrix
    cols_buckets  = {}
    list_of_bands = [[i, i+1] for i in range(0, matrix.shape[0], 2)]
    print(list_of_bands)
    for i in range(matrix.shape[1]):
        cols_buckets['C' + str(i+1)] = []

    for i in range(matrix.shape[1]):
        for t in range(len(list_of_bands)):
            cols_buckets['C' + str(i+1)].append(abs(hash("Band" + str(t) + "_" +  str([matrix[x,i] for x in list_of_bands[t]])))  % 2**bits) 

    return(cols_buckets)

def shingles(string, k):
    d = dict()

    for i in range(len(string)):
        if i + k > len(string):
            continue

        key    = string[i:(i+k)]         
        d[key] = d.get(key, 0) + 1

    return(d)

def l1_norm(a, b):
    s = sum([abs(a[i] - b[i]) for i in range(len(a))])
    return(s)

def l2_norm(a,b):
    s = sum([(a[i] - b[i])**2 for i in range(len(a))])
    return(math.sqrt(s))

def jaccard_similarity(s1, s2):
    union = set(s1.keys() + s2.keys())
    inter = set.intersection(*[set(s1.keys()), set(s2.keys())])

    return(len(inter) / float(len(union)))

if __name__ == '__main__':
    print("----- Question 1 ------")
    words = ['he', 'she', 'his', 'hers']
    for i in range(len(words)):
        for j in range(i, len(words)):
            if words[i] != words[j]:
                print("Edit_distance({0}, {1}) = {2}".format(words[i], words[j], edit_distance(words[i], words[j])))

    print("----- Min Hash Test -----")
    matrix = [[1,0,0,1],[0,0,1,0],[0,1,0,1],[1,0,1,1],[0,0,1,0]]
    matrix = np.array(matrix)
    print(matrix)
    print(min_hash(matrix, [1,2,3,4,5], [lambda x: (x+1) % 5, lambda x: (3*x + 1) % 5]))
    print("----- Question 2 -----")
    matrix = [[0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 0]]
    matrix = np.array(matrix)
    print(matrix)
    order  = [4, 6, 1, 3, 5, 2]
    print(min_hash(matrix, order))
    print("----- Question 3 -----")
    matrix = [[1,2,1,1,2,5,4],[2,3,4,2,3,2,2],[3,1,2,3,1,3,2],
              [4,1,3,1,2,4,4],[5,2,5,1,1,5,1],[6,1,6,4,1,1,4]]
    matrix = np.array(matrix)
    print(lsh(matrix))
    print("----- Question 4 -----")
    s1 = shingles("ABRACADABRA", 2)
    s2 = shingles("BRICABRAC", 2)
    print(s1)
    print(s2)
    print(set(s1.keys() + s2.keys()))
    print(len(set(s1.keys() + s2.keys())))
    print("Jaccard similarity = {0}".format(jaccard_similarity(s1,s2)))
    print("----- Question 6 -----")
    print("L1 From (0,0) to (53,15) = {0}".format(l1_norm([0,0], [53,15])))
    print("L2 From (0,0) to (53,15) = {0}".format(l2_norm([0,0], [53,15])))
    print("L1 From (100,40) to (53,15) = {0}".format(l1_norm([100,40], [53,15])))
    print("L2 From (100,40) to (53,15) = {0}".format(l2_norm([100,40], [53,15])))




