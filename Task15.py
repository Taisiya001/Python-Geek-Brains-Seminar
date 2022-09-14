def count(N):
    i = 2
    d = []
    while i*i <= N:
        if N % i == 0:
            d.append(i)
            N //= i
        else:
            d += 1
    if N > 1:
        d.append(N)
    return d
print(count(int(input())))