# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    counting = {}
    cumulated = 0
    maximum = 0
    for X in A:
        if X <= N:
            if X in counting:
                counting[X] += 1
            else:
                counting[X] = 1
            maximum = max([maximum, counting[X]])
        else:
            counting = {}
            cumulated += maximum
            maximum = 0
    counters = [cumulated] * N
    for K, count in counting.items():
        counters[K - 1] = cumulated + count
    return counters
