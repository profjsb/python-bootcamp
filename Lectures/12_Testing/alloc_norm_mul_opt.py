def _poly_opt(X):
    # (X + (3 * X))**2
    X *= 4
    X **= 2
    return X

def alloc_norm_mul_opt(A, B):
    """Take two matrices, A and B,

    - normalize their rows by dividing with their sums
    - do a polynomial transformation on each
    - multiply them and return the result.

    """
    A = A.copy()
    B = B.copy()

    A /= A.sum(axis=0)
    B /= B.sum(axis=0)

    return A.dot(B)
