def solution(A):
    left_total = A[0]
    right_total = sum(A[1:])

    min_difference = abs(left_total - right_total)

    for num in A[1:len(A) - 1]:
        left_total += num
        right_total -= num
        min_difference = min(min_difference, abs(left_total - right_total))
    return min_difference


print(solution([-1000, 1000]))
