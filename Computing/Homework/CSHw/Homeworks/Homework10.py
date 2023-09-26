def num_to_str(val):
    num = ""
    for x in range(1, 7):
        try:
            num += (val[-x])
        except IndexError:
            num += "0"
    return num[::-1]


number = [0,0,0,0,0,0]
total = 0
for a in range(10):
    number[0] = a
    for b in range(10):
        number[1] = b
        for c in range(10):
            number[2] = c
            for d in range(10):
                number[3] = d
                for e in range(10):
                    number[4] = e
                    for f in range(10):
                        number[5] = f
                        current = str(number[0]) + str(number[1]) + str(number[2]) + str(number[3]) + str(number[4]) + str(number[5])
                        value = int(current)
                        if current[2:5] == current[5:2:-1]:
                            value += 1
                            current = num_to_str(str(value))
                            if current[1:5] == current[5:1:-1]:
                                value += 1
                                current = num_to_str(str(value))
                                if current[1:4] == current[4:1:-1]:
                                    value += 1
                                    current = num_to_str(str(value))
                                    if current == current[::-1]:
                                        value += 1
                                        current = num_to_str(str(value))
                                        print(number)






