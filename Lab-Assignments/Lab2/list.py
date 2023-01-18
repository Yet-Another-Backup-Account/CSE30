def list_comprehension(A):
    return [(lambda i:A[i] + A[i+1])(i) for i in range(len(A) -1)]
