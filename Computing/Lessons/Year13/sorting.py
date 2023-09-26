import random

myList = [random.randint(1, 100) for x in range(64)]

def bubble_sort(l):
    passMade=True # Has a swap been made
    largestIndex = len(l)
    while passMade:
        passMade = False
        prev = l[0]
        for x in range(1, largestIndex):
            if prev > l[x]:
                l[x-1] = l[x]
                l[x] = prev
                passMade = True
            else:
                prev = l[x]
        largestIndex -= 1
    return l

def merge_two_sorted_lists(sortedLeft, sortedRight):
    leftIndex, rightIndex = 0, 0
    sortedList = []
    while True:
        leftItem = sortedLeft[leftIndex]
        rightItem = sortedRight[rightIndex]
        if leftItem < rightItem:
            sortedList.append(leftItem)
            leftIndex += 1
        else:
            sortedList.append(rightItem)
            rightIndex += 1
        if leftIndex == len(sortedLeft):
            for item in sortedRight[rightIndex:]:
                sortedList.append(item)
            break
        elif rightIndex == len(sortedRight):
            for item in sortedLeft[leftIndex:]:
                sortedList.append(item)
            break
    return sortedList


def merge_sort(l):
    if len(l) != 1:
        mid = len(l) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge_two_sorted_lists(left, right)
    else:
        return l

def binary_search_for_insertion(l, value):
    pass


def library_sort(l):
    pass