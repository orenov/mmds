import numpy as np
import math

def jaccard(a,b):
    a = a.keys()
    b = b.keys()

    return len(set(a).intersection(b)) / float(len(set(a + b)))

def cosine(a,b):
    fields = set(a.keys() + b.keys())
    dot_pr = 0.
    for field in fields:
        dot_pr += a.get(field, 0) * b.get(field, 0)
    norm_a = math.sqrt(sum([a[field] * a[field] for field in a.keys()]))
    norm_b = math.sqrt(sum([b[field] * b[field] for field in b.keys()]))

    return dot_pr / (norm_a * norm_b)


if __name__ == '__main__':
    A = {'a' : 4., 'b' : 5., 'd' : 5., 'e' : 1., 'g' : 3., 'h' : 2.}
    B = {'b' : 3., 'c' : 4., 'd' : 3., 'e' : 1., 'f' : 2., 'g' : 1.}
    C = {'a' : 2., 'c' : 1., 'd' : 3., 'f' : 4., 'g' : 5., 'h' : 3.}
    users = {'A' : A, 'B' : B, 'C' : C}

    print ("--------- Part a) --------")
    for user1 in users.keys():
        for user2 in users.keys():
            if user1 != user2:
                print("JaccardSimilarity({0}, {1}) = {2}".format(user1, user2, jaccard(users[user1], users[user2])))

    print("--------- Part b) --------")
    for user1 in users.keys():
        for user2 in users.keys():
            if user1 != user2:
                print("CosineDistance({0}, {1}) = {2}".format(user1, user2, cosine(users[user1], users[user2])))

    # Normalize

    norm   = lambda s : 1 if s >= 3 else 0 
    A_norm = {}
    B_norm = {}
    C_norm = {}
    for key in A.keys():
        A_norm[key] = norm(A[key])

    for key in B.keys():
        B_norm[key] = norm(B[key])

    for key in C.keys():
        C_norm[key] = norm(C[key])

    users_norm = {'A' : A_norm, 'B' : B_norm, 'C' : C_norm}


    print(A_norm)

    pass