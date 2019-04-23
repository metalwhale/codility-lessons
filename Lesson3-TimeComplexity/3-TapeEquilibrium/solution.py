# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    all_sum = sum(A)
    cur_sum = A[0]
    diff = abs(all_sum - 2 * cur_sum)
    i = 1
    while i < len(A) - 1:
        cur_sum += A[i]
        cur_diff = abs(all_sum - 2 * cur_sum)
        if cur_diff < diff:
            diff = cur_diff
        i += 1
    return diff
