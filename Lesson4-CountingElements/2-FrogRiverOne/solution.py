# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    pos = [0] * X
    all_sum = (1 + X) * X // 2
    cur_sum = 0
    for i in range(len(A)):
        cur = A[i]
        if pos[cur - 1] == 0:
            pos[cur - 1] = 1
            cur_sum += cur
        if cur_sum == all_sum:
            return i
    else:
        return -1
