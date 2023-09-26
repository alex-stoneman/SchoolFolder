import time


def tri_a(n):
    total = 0
    for x in range(1, n + 1):
        total += x
    return total


def tri_b(previous, n):
    return previous + n


def tri_c(n):
    return int(0.5 * n * (n + 1))


def squ_a(n):
    total = 0
    for x in range(1, 2 * n + 1, 2):
        total += x
    return total


def squ_b(previous, n):
    return previous + 2 * n - 1


def squ_c(n):
    return n * n


def polygonal_c(poly, n):
    return int(0.5 * ((poly - 2) * n ** 2 + (4 - poly) * n))


number = 10000000
found = 0
total = 0
print("Method B - Cumulative")
first = time.perf_counter_ns()
x = 0
y = 0
xVal = 0
yVal = 0
while found != 8:
    total += 1
    if xVal > yVal:
        y += 1
        yVal = squ_b(yVal, y)
    else:
        x += 1
        xVal = tri_b(xVal, x)
    if xVal == yVal:
        print(xVal)
        found += 1

second = time.perf_counter_ns()
diff = round((second - first) / 10 ** 9, 5)
print(diff, "s\n")
print(total)
print()

# Searching
total = 0
found = 0
print("New method - searching")
first = time.perf_counter_ns()
x = 1
sqrt2 = 1.41
while found != 7:
    total += 1
    #print("x =",x)
    new = int(sqrt2 * x)
    triangle = tri_c(new)
    if triangle == x * x:
        print(triangle)
        found += 1
    else:
        if triangle > x * x:
            diff = -1
        else:
            diff = 1
        prev = diff
        while True:
            total += 1
            if diff == prev:
                if diff:
                    triangle += new + diff
                else:
                    triangle -= new
                new += diff
                if triangle > x * x:
                    prev = -1
                elif triangle == x * x:
                    print(triangle)
                    found += 1
                    break
                else:
                    prev = 1
            else:
                break
    x += 1
second = time.perf_counter_ns()
diff = round((second - first) / 10 ** 9, 5)
print(diff, "s\n")
print(total)