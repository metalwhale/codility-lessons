# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    import math
    distance = abs(Y - X)
    return math.ceil(distance / D)
