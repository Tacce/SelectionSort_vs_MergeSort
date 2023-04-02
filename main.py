import sys

inf = sys.maxsize


def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)


def Merge(A, p, q, r):
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    L.append(inf)
    R.append(inf)
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




if __name__ == '__main__':
    A = [1, 4, 2, 5, 9, 3]
    print(A)
    MergeSort(A, 0, len(A) - 1)
    #SelectionSort(A)
    print(A)
