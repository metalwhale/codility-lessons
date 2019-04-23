# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sorted_A = sorted(A)
    for i in range(len(sorted_A)):
        if sorted_A[i] != i + 1:
            return 0
    else:
        return 1
