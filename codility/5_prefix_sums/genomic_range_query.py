import unittest


def impact_factor(type):
    impact_factors = {"A": 1, "C": 2, "G": 3, "T": 4}
    return impact_factors[type]


def build_nucleotide_sums(nucleotides):
    nucleotide_sums = [[0] * 4 for x in range(len(nucleotides))]
    for i, nucleotide_char in enumerate(nucleotides):
        if nucleotide_char == "A":
            nucleotide_sums[i][0] = 1
        if nucleotide_char == "C":
            nucleotide_sums[i][1] = 1
        if nucleotide_char == "G":
            nucleotide_sums[i][2] = 1
        if nucleotide_char == "T":
            nucleotide_sums[i][3] = 1

    for i in range(1, len(nucleotides)):
        for j in range(4):
            nucleotide_sums[i][j] += nucleotide_sums[i-1][j]

    return nucleotide_sums


def solutions(S, P, Q):
    results = []

    nucleotide_sums = build_nucleotide_sums(S)
    for i in range(len(P)):
        start_idx = P[i]
        end_idx = P[i]

        for j in range(4):
            sub = 0
            if start_idx - 1 >= 0:
                sub = nucleotide_sums[start_idx - 1][j]
            if nucleotide_sums[end_idx][j] - sub > 0:
                results.append(j + 1)

    return results


class TestGenomicRangeQuery(unittest.TestCase):

    def test_sample(self):
        self.assertEqual([2, 4, 1], solutions("CAGCCTA", [2, 5, 0], [4, 5, 6]))
