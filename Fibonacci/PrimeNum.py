#PrimeNumber
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
#           print(n, 'equals', x, '*', n//x)
            break
        else:
            pass
#            print(n,'is prime number',n,'/',x)

# Squares Number
squares = [x**2 for x in range(10)]
#print(squares)

# create a list of 2-tuples like (number, square)
squares2 = [(x, x**2) for x in range(10)]
#print(squares2)

# flatten a list using a listcomp with two 'for'
vec = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
#print([num for ele in vec for num in ele])

# transpose les lignes et les colonnes
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
#print([[row[i] for row in matrix] for i in range(4)])

#print(list(zip(*matrix)))