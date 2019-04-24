# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    maximum = 0
    previous_maximum = 0
    counters = [previous_maximum] * N
    for X in A:
        if X <= N:
            counters[X - 1] = max([previous_maximum, counters[X - 1]]) + 1
            maximum = max([maximum, counters[X - 1]])
        else:
            previous_maximum = maximum
    for K in range(N):
        if counters[K] < previous_maximum:
            counters[K] = previous_maximum
    return counters
