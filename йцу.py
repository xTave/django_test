def gen(start, dif, end):
    i = 1
    cur = start * 4
    a = [cur]
    while True:
        yield cur
        if cur > end:
            break
        for j in range(len(a)):
            b = a[j] / (i - j)
            c = b * (i + 1 - j)
            a[j] = c
        a.append((start + dif * i) * 4)
        cur = sum(a)
        i += 1

for i in gen(1.0, 0.05, 600):
    print(i)
