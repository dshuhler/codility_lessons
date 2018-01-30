
def decimal_to_binary(dec_num):
    result = ''
    while dec_num > 0:
        result = result + str(dec_num % 2)
        dec_num = dec_num // 2
    return result[::-1]


def solution(N):
    binary_n = decimal_to_binary(N)

    this_length = 0
    max_length = 0

    for c in binary_n:
        if c == '1':
            max_length = max(max_length, this_length)
            this_length = 0
        else:
            this_length += 1

    return max_length


print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
