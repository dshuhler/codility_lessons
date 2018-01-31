def solution(X, Y, D):
    distance = Y - X
    jumps = (distance // D)
    if distance % D != 0:
        jumps += 1
    return jumps


print(solution(10, 85, 30), 3)
print(solution(0, 0, 30), 0)
print(solution(10, 11, 100000), 1)
print(solution(10, 90, 30), 3)

