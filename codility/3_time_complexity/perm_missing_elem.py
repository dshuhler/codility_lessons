def solution(A):
    index_total = 0
    value_total = 0

    for index, value in enumerate(A):
        index_total += index + 1
        value_total += value

    return (index_total - value_total) + len(A) + 1


print(solution([1, 2, 3, 5, 6]), 4)
print(solution([2, 1, 3, 5]), 4)
print(solution([2, 1, 3, 5, 6, 7, 8, 10, 4]), 9)

big_list = list(range(1, 1000000))
big_list.remove(400)

print(solution(big_list), 400)

