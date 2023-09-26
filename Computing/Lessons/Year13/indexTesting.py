import math as maths

def hex_indexes(n):
    valRange = [a for a in range(-n, n+1)]
    hexList=[[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
    for s in valRange:
        for q in valRange:
            if abs(s+q) <= n:
                index = (s + n) * (2 * n + 1) + q + n - (n*(n+1))//2
                if s < 0:
                    a = abs(s) - 1
                    index += (a*(a+1))//2
                b = (abs(s-1)+s-1)//2
                index -= (b*(b+1))//2
                hexList[s+n][q+n] = index
            else:
                hexList[s + n][q + n] = -1
    return hexList


def rect_indexes(h, w):
    return [[y*w+x for x in range(w)] for y in range(h)]


def circ_indexes(n, starting):
    circList = []
    cells = starting
    for y in range(n):
        if (starting//2+1) * (y+1) / cells > 1:
            cells *= 2
        circList.append([y*n+x for x in range(cells)])
    return circList

# print()
# for item in hex_indexes(int(input())):
#     print(item)
# print()
# for item in rect_indexes(int(input()), int(input())):
#     print(item)
c = 0
i = 500
j = 2
N = [1]
#print(*(len(item) for item in circ_indexes(int(i))))
print(sum(N), end=", ")
for x in range(16):
    n = j * (2**x)
    N.append(sum(1 if len(item) == n else 0 for item in circ_indexes(i, j)))
    #print(n, sum(1 if len(item) == n else 0 for item in circ_indexes(i, j)))
    print(sum(N), end=", ")
print()


