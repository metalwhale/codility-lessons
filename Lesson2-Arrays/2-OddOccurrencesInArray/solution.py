# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    unpaired = set()
    for e in A:
        if e in unpaired:
            unpaired.remove(e)
        else:
            unpaired.add(e)
    return unpaired.pop()
