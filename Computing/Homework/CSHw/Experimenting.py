first = round((401**(1/2)-1)/2,2)
print(first)
probOfFour = ((1/6)**4)
probOfFive = ((1/6)**5)
print(probOfFour/probOfFive)
l = []
check = 0


def recur(lis):
    p = [[],[]]
    for x in range(2):
        for i in lis:
            p[x].append(i)
        if x == 0:
            p[x].append("Y")
        else:
            p[x].append("N")
    return p


def call_recur(lis):
    global check
    lis = recur(lis)
    if len(lis) <3:
        print(lis)
        recur(lis)
        lis = call_recur(lis)
    return lis

l = call_recur(l)
print(l)