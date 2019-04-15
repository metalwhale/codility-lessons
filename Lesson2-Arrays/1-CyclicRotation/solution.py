# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    k = K % len(A) if len(A) != 0 else K
    return A[-k:] + A[:-k]
