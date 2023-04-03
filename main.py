import sys
import matplotlib.pyplot as plt
import numpy as np
import time
import random

inf = sys.maxsize


def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)


def Merge(A, p, q, r):
    L = np.array(A[p:q + 1])
    R = np.array(A[q + 1:r + 1])
    L = np.append(L, inf)
    R = np.append(R, inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def SelectionSort(A):
    n = len(A)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if A[j] < A[minimum]:
                minimum = j
        A[i], A[minimum] = A[minimum], A[i]


def plotSortGraph(algType, insertType):
    x, y = [], []
    for i in range(10, 1000, 10):
        x.append(i)
        A = np.arange(i) if insertType == 0 else random.sample(range(i), i)
        if algType == 0:
            start = time.perf_counter()
            SelectionSort(A)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            MergeSort(A, 0, len(A) - 1)
            end = time.perf_counter()
        z = y[-1] if (len(y) != 0) else 0
        y.append((end - start) / i + z)
    plt.plot(x, y)
    title = 'Selection-Sort' if algType == 0 else 'Merge-Sort'
    title += ' on Ordered List' if algType == 0 else ' on Randomized List'
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    [[plotSortGraph(i, j) for i in range(2)] for j in range(2)]
