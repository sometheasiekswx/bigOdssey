import math


class Coin:
    def __init__(self, position: int, value: int):
        self.position = position
        self.value = value


class Solver:
    # Find maximum number of coin combination.
    # Because all coins are n=2^k with two coins, there is a pattern where three cases emerge:
    # 1. sum is odd, so Solve(2n+1) = Solve(n)
    # 2. sum is even, so Solve(2n+2) = Solve(n+1) + Solve(n)
    # 3. sum is 0, so Solve(0) = 1.
    # Notice that our array generated matches the Stern's diatomic series
    # 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3, 8, 5, 7, 2, 7, 5, 8, 3, 7, 4, 5, 1, etc...
    # With Stern's sequence property, we can see that 2^k - 1 = 1.
    # The palindrome is between two 1s, so we can find the start and end of the palindrome using that property.
    # If the start and end positions are equal, k + 1 is our solution.
    # Otherwise, we do a binary search to find the position that equals the sum.
    # Using Stern's diatomic series, its property ensures we can find the 1s, start, end, and mid-values.
    # References:
    # - https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree
    # - https://mathlesstraveled.com/2008/04/21/challenge-12-solution-part-i/
    # - https://mathlesstraveled.com/2009/09/19/challenge-12-solution-part-ii/
    # - https://mathlesstraveled.com/2008/04/24/challenge-12-solution-part-iii/
    # - https://github.com/njanardhanan/JEulerProblems/blob/aa54fbec447f1307dca0b5a73bc4539dd05e92b5/src/com/jsoft/jeuler/problems/JEulerProblem_0169.java
    # - https://github.com/BobKat99/Coin-problem
    # Time: O(logn)
    # Space: O(1)
    def solve(self, sum_to_match: int) -> int:
        """
        Find maximum number of special coins combinations using Stern's diatomic sequence.
        """
        # Find start of palindrome
        k_start = math.floor(math.log2(sum_to_match))
        position_start = (1 << k_start) - 1
        start = Coin(position_start, 1)

        # Find end of palindrome
        k_end = math.ceil(math.log2(sum_to_match))
        position_end = (1 << k_end) - 1
        end = Coin(position_end, 1)

        # If sum is already a 2^k, result will be k + 1
        if start.position == end.position:
            return k_start + 1

        # Apply binary search on Stern sequence
        return self.binary_search(sum_to_match, start, end)

    def binary_search(self, sum_to_match: int, start: Coin, end: Coin) -> int:
        """
        Perform binary search on Stern's diatomic series to find the result.
        """
        while True:
            if sum_to_match == start.position:
                return start.value
            if sum_to_match == end.position:
                return end.value

            # Find mid of palindrome
            value_mid = start.value + end.value
            position_mid = start.position + (end.position - start.position) // 2
            mid = Coin(position_mid, value_mid)

            # Search right or left side
            if sum_to_match > mid.position:
                start = mid
            else:
                end = mid


if __name__ == '__main__':
    problemsAnswers = [[1, 1], [6, 3], [47, 2], [256, 9], [8489289, 6853], [1000000000, 73411], [100, 19], [128, 8],
                       [1073741824, 31], [6370, 175], [10, 5], [2, 2], [3, 1], [4, 3], [2000000000, 81034],
                       [999999999, 7623], [1000000000000000000, 554817437], [576460752303423488, 60], [640, 23],
                       [785, 34], [1022, 10], [962, 38], [640, 23], [1099510542205, 17863], [944875173846, 1243789],
                       [672031828383, 500073], [893915235088, 243779], [1088385987371, 4634234],
                       [347905064087584832, 5150282], [309341003709448449, 19102955], [263810380166378775, 4693345949],
                       [361431780114432130, 94727263], [378311177695920400, 20702253], [290553370434404484, 146293655],
                       [423901414250789313, 292614203], [438190581230404958, 6012372582],
                       [293666568548731467, 3648043185], [392393882169705920, 3341296806],
                       [376370659955075108, 3279511256], [412658913555584867, 3498747798],
                       [999999999999999999, 29665503], [410054521552536292, 26030230909],
                       [416860608518791589, 8015276820], [393014244375683364, 16905456859],
                       [518010418436963490, 15340957057], [576460730781662959, 794365], [565764701561028461, 2186952],
                       [571954850028252927, 7287457], [558161296277634687, 1416255], [504314853196816127, 6183662],
                       [123456789, 51639], [768614336404564650, 2504730781961], [384307168202282325, 956722026041],
                       [384307168202282324, 1548008755920], [192153584101141162, 956722026041],
                       [196657183728511722, 502131822759], [193349852752161450, 484936992181],
                       [196731950519200426, 350312970581], [192153584101141166, 644603021052],
                       [10000000000000000, 17165857], [200, 26], [93459834598323452, 317400926],
                       [1717161617181871, 69493195], ]
    solver = Solver()
    corrects = []
    wrongs = []
    for i, (problem, answer) in enumerate(problemsAnswers):
        if solver.solve(problem) == answer:
            corrects.append(i)
        else:
            wrongs.append(i)
    print(f"Correct: {len(corrects)}/{len(problemsAnswers)}\n{corrects}")
    print(f"Wrongs: {len(wrongs)}/{len(problemsAnswers)}\n{wrongs}")
