def solution(A):
    occurances = [0] * len(A)

    for num in A:
        if num > len(A):
            return 0
        elif occurances[num - 1] == 1:
            return 0
        else:
            occurances[num - 1] = 1
    return 1


print(solution([4, 1, 2, 3]))
print(solution([4, 1, 3]))
print(solution([4, 10, 3]))
print(solution([4, 10, 3, 1, 2, 5, 6, 7, 9, 8]))
