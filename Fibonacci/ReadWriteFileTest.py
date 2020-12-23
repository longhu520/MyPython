with open('Fibonacci.py','r') as f:
    # read_data = f.read()

    # read_data = f.readline()
    # print(repr(read_data))

    for line in f:
        print(line, end=' ')
    f.closed
