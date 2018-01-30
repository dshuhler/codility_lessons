
def solution(A, K):
    if len(A) == 0:
        return []

    defacto_shift = K % len(A)
    new_array = A[:len(A) - defacto_shift]
    new_array = A[len(A) - defacto_shift:] + new_array
    return new_array


print(solution([3, 8, 9, 7, 6], 3))
print(solution([1, 2, 3, 4, 5], 1))
print(solution([], 1))

