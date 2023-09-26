import random

c = 0
h = random.randint(2, 12)
m = random.randint(1, h-1)
count = 0
def find_solutions(c, m, h, steps, count):
    if m == h:
        print(steps)
        count += 1
    else:
        if c != m - 1:
            count = find_solutions(c+1, m, h, f"{steps}c", count)
        count = find_solutions(c, m+1, h, f"{steps}m", count)
    return count

print(c, m, h)
count = find_solutions(c, m, h, "", count)
print()
print(count)