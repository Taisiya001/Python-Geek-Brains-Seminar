a = [int(s) for s in input().split()]
x = int(input())
index = len(a) + 1
for i in range(len(a)):
    if x>a[i]:
        index = i+1
        break
print(index)