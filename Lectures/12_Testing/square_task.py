import numpy as np

def expensive_square(x):
    x = x.copy()
    for i in range(x.size):
        x[i] = x[i] ** 2

    return x

def cheap_square(x):
    return x**2

square = expensive_square
#square = cheap_square

def execute():
    print("Squaring some numbers...")
    x = np.arange((500000))
    x = (x + 0.3) / 4

    y = square(x)


if __name__ == "__main__":
    execute()
