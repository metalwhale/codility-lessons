# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    FARTHEST_MOVE = 6
    pending = []
    result = 0
    for i, square in enumerate(A):
        if square >= 0 or i == 0 or i == len(A) - 1:
            negative_sum = 0 if len(pending) < FARTHEST_MOVE else max(pending)
            result += negative_sum + square
            pending.clear()
        else:
            if len(pending) < FARTHEST_MOVE:
                pending.append(square)
            else:
                last = max(pending) + square
                pending.pop(0)
                pending.append(last)
    return result
