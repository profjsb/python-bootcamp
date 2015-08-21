import numpy as np


def _norm_rows(X):
    X = X.copy()
    m, n = X.shape

    for i in range(m):
        row_sum = 0

        for j in range(n):
            row_sum += X[i, j]

        for j in range(n):
            X[i, j] /= row_sum

    return X


def _polynomial(X):
    return (X + (3 * X))**2



def _matmul(A, B, out):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    # Take each row in A
    for i in range(rows_A):

        # And multiply by every column in B
        for j in range(cols_B):
            s = 0
            for k in range(cols_A):
                s = s + A[i, k] * B[k, j]

            out[i, j] = s


@profile
def alloc_norm_mul(A, B):
    """Take two matrices, A and B,

    - normalize their rows by dividing with their sums
    - do a polynomial transformation on each
    - multiply them and return the result.

    """
    m, n = A.shape
    p, q = B.shape

    if not (n == p):
        raise ValueError('Matrix dimensions are incompatible')

    # Output shape
    M, N = m, q

    # Step 1: allocate output memory
    out = []
    for i in range(M):
        row = [[0]] * N
        out.append(row)

    out = np.array(out, dtype=np.float64).squeeze()

    # Step 2: normalize arrays by dividing each row by its sum
    A = _norm_rows(A)
    B = _norm_rows(B)

    A = _polynomial(A)
    B = _polynomial(B)

    _matmul(A, B, out)

    return out
