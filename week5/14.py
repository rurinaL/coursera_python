n = list(map(int, input().split()))
for i in range(0, len(n)):
    if n[i] % 2 == 0:
        print(n[i], end=' ')
