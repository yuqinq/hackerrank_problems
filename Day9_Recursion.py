def factorial(N):
    if N<=1:
        return 1
    else:
        for i in range(N):
            result = N * factorial(N-1)
        return result

print (factorial(int(input())))
