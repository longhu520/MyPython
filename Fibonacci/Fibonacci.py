def fib(n):
    """Print Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

# call the function
fib(100)

def fib2(n):
    """Return Fib serires in a list"""
    resulat = []
    a, b = 0, 1
    while a < n:
        resulat.append(a)
        a, b = b, a + b
    return resulat

#f100 = fib2(100)
#print(f100)

# if __name__ == "__main__":
#     import sys
#
#     fib(int(sys.argv[1]))
