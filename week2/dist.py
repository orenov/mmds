import math

def l1_norm(a, b):
    # Vectors
    s = sum([abs(a[i] - b[i]) for i in range(len(a))])
    return(s)

def l2_norm(a, b):
    # Vectors
    s = sum([(a[i] - b[i])**2 for i in range(len(a))])
    return(math.sqrt(s))

def lr_norm(a, b, r= 2):
    # Vectors
    s = sum([(a[i] - b[i])**r] for i in range(len(a)))
    return(s**(1./r))

def l_infin(a, b):
    # Vectors
    s = [abs([a[i] - b[i]]) for i in range(len(a))]
    return(max(s))

def jaccard_distance(a,b):
    # Sets
    union = set(a + b)
    inter = set.intersection(*[set(a), set(b)])

    return(1. - (len(inter) / float(len(union))))

def cosine_distance(a, b):
    # Vectors
    origin  = [0.] * len(a)
    top     = sum([a[i]*b[i]  for i in range(len(a))])
    return(top / (l2_norm(a, origin) * l2_norm(b, origin)))

if __name__ == '__main__':
    print("--- Exercise 3.5.2 ----")
    







