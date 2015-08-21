import numpy as np


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

    A /= A.sum(axis=1)[:, np.newaxis]
    B /= B.sum(axis=1)[: ,np.newaxis]

    A = _poly_opt(A)
    B = _poly_opt(B)

    return A.dot(B)

if __name__ == '__main__':
    from alloc_norm_mul import alloc_norm_mul
    A = np.random.random((500, 20))
    B = np.random.random((20, 300))
    np.testing.assert_allclose(alloc_norm_mul(A, B),
                               alloc_norm_mul_opt(A, B))
