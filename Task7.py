n = int(input())
res = 0
if n <= 0:
    for i in range(n, 2):
        res += i
else:
    for i in range(1, n+1):
        res += i
print(res)