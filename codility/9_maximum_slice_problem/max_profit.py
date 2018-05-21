import unittest

# Convert array of prices into array of price changes, then use max slice

def solution(A):

    daily_profits = []
    for i in range(len(A) - 1):
        daily_profits.append(A[i + 1] - A[i])

    max_profit = 0
    ending_profit = 0
    for daily_profit in daily_profits:
        ending_profit = max(0, ending_profit + daily_profit)
        max_profit = max(max_profit, ending_profit)

    return max_profit


class TestMaxProfit(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(356, solution([23171, 21011, 21123, 21366, 21013, 21367]))


if __name__ == '__main__':
    unittest.main()