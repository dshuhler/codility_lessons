def solution(X, A):
    leaf_coverage = [False] * X
    frog_position = -1
    for time, fallen_leaf_position in enumerate(A):
        leaf_coverage[fallen_leaf_position - 1] = True

        for num in range(frog_position, X):
            if leaf_coverage[frog_position + 1]:
                frog_position += 1
                if frog_position + 1 == X:
                    return time
            else:
                break

    return -1


print(solution(5, [1, 3, 2, 4, 3, 3, 5, 2]))
print(solution(5, [1, 3, 2, 4, 3, 3, 4, 2]))
print(solution(5, [5, 5, 4, 3, 2, 2, 2, 1]))

