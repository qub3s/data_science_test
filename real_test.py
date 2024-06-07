import numpy as np 


def real_test():
    array = [1, 2, 3, 4, 2, 3, 4]

    n = np.array(array)
    unique, counts = np.unique(n, return_counts=True)
    print(unique[counts == 1])
