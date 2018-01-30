
def solution(A):
    missing_int = 0
    for value in A:
        new_missing_int = missing_int ^ value
        print(bin(new_missing_int), '=', bin(missing_int), '^', bin(value))
        missing_int = new_missing_int
    return missing_int


print(solution([32, 2, 1, 3, 32, 2, 3]))
