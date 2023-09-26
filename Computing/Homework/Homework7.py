def is_square(n):
    between = [0, n + 1]
    while True:
        if between[0] == between[1] or between[0] + 1 == between[1]:
            return False
        else:
            new = (between[0] + between[1]) // 2
            if new ** 2 == n:
                return True
            elif new ** 2 < n:
                between[0] = new
            else:
                between[1] = new


wanted = []
for a in range(600):
    for b in range(600):
        if is_square(a + b) and a < b:
            for c in range(600):
                if is_square(b + c) and b < c:
                    if is_square(a + c):
                        if is_square(a + b + c):
                            wanted.append([a, b, c])

for item in wanted:
    print(item)
