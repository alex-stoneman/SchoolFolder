def linear_search(myList, wanted):
    for item in myList:
        if item == wanted:
            return True
    return False

def non_recursive_binary_search(myList, wanted):
    smallest = 0
    largest = len(myList) - 1
    while True:
        middle = (largest + smallest) // 2
        value = myList[middle]
        if value == wanted:
            return True
        elif value > wanted:
            largest = middle - 1
        else:
            smallest = middle + 1
        if smallest > largest:
            return False

def recursive_binary_search(myList, wanted):
    middle = (len(myList) - 1) // 2
    value = myList[middle]
    if value == wanted:
        return True
    elif value > wanted:
        return recursive_binary_search(myList[:middle], wanted)
    else:
        return recursive_binary_search(myList[middle + 1:], wanted)


testList = [1, 6, 8, 19, 42, 108, 694, 999, 1000]
