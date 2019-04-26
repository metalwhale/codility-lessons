def solution(A):
    FARTHEST_MOVE = 6
    pending = [A[0]] * FARTHEST_MOVE
    for i in range(1, len(A)):
        pending[i % FARTHEST_MOVE] = max(pending) + A[i]
    return pending[(len(A) - 1) % 6]
