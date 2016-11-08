import sys

__all__ = ["fib2"]

def fib(n=None):    # escribe la serie Fibonacci hasta n
    if n is None:
        n = int(sys.argv[1])
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # devuelve la serie Fibonacci hasta n
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado

main = fib

if __name__ == "__main__":
    sys.exit(main())