from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    counts = Counter(a)
    std = list(counts.values())
    k = 0

    i = 0
    for _ in range(len(std)):
        if std[i] % 2 == 1:
            k += 1
            std.remove(std[i])
            i -= 1
        else:
            std[i] = 2
        i += 1

    k += len(std)
    if len(std) % 2 == 1:
        k -= 1
    print(k)