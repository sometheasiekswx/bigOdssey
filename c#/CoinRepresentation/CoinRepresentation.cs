namespace CoinRepresentation;

public class Solver
{
    /// <summary>
    ///     Find maximum number of coin combination. Because all coins are n=2^k with two coins, there is a pattern where three
    ///     cases emerge:
    ///     1. sum is odd, so Solve(2n+1) = Solve(n)
    ///     2. sum is even, so Solve(2n+2) = Solve(n+1) + Solve(n)
    ///     3. sum is 0, so Solve(0) = 1.
    ///     Notice that our array generated matches the Stern's diatomic series
    ///     (https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree):
    ///     1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3, 8, 5, 7, 2, 7, 5, 8, 3, 7, 4, 5, 1, etc...
    ///     With Stern's sequence property, we can see that 2^k - 1 = 1. The palindrome is between two 1s, so we can find
    ///     the start and end of the palindrome using that property. If the start and end positions are equal, k + 1 is our
    ///     solution. Otherwise we do a binary search to find the position that equals the sum. Using Stern's diatomic series,
    ///     its property ensures we can find the 1s, start, end, and mid values.
    ///     References:
    ///     - https://mathlesstraveled.com/2008/04/21/challenge-12-solution-part-i/
    ///     - https://mathlesstraveled.com/2009/09/19/challenge-12-solution-part-ii/
    ///     - https://mathlesstraveled.com/2008/04/24/challenge-12-solution-part-iii/
    ///     -
    ///     https://github.com/njanardhanan/JEulerProblems/blob/aa54fbec447f1307dca0b5a73bc4539dd05e92b5/src/com/jsoft/jeuler/problems/JEulerProblem_0169.java
    ///     - https://github.com/BobKat99/Coin-problem
    ///     Complexity: O(logn)
    /// </summary>
    /// <param name="sum">Sum to match</param>
    /// <returns>Maximum unique combinations of special coins</returns>
    public static long Solve(long sum)
    {
        // Find start of palindrome
        // - k: nearest k of the 2^k on left side
        // - position: nearest 2^k - 1 on left side 
        // O(1)
        var kStart = (int)Math.Floor(Math.Log(sum, 2));
        var positionStart = (long)Math.Pow(2, kStart) - 1;
        var start = new Coin(positionStart, 1);

        // Find end of palindrome
        // - k: nearest k of the 2^k on right side
        // - position: nearest 2^k - 1 on right side
        // O(1)
        var kEnd = (int)Math.Ceiling(Math.Log(sum, 2));
        var positionEnd = (long)Math.Pow(2, kEnd) - 1;
        var end = new Coin(positionEnd, 1);

        // If sum is already a 2^k, result will be k + 1
        // O(1)
        if (start.Position == end.Position) return kStart + 1;

        // If sum is not a 2^k, apply binary search on Stern sequence
        // O(logn)
        return BinarySearch(sum, start, end);
    }

    /// <summary>
    ///     Find the result using binary search on Stern's diatomic series.
    ///     Complexity: O(logn)
    /// </summary>
    /// <param name="sum">Sum's whose position to find</param>
    /// <param name="start">Start element</param>
    /// <param name="end">End element</param>
    /// <returns>Unique combinations of special coins</returns>
    private static long BinarySearch(long sum, Coin start, Coin end)
    {
        // O(logn) because we half each time
        while (true)
        {
            // Return if value of the sum is calculated
            if (sum == start.Position) return start.Value;
            if (sum == end.Position) return end.Value;

            // Find mid of palindrome
            // - value: sum of end points
            // - position: middle of end points
            var valueMid = start.Value + end.Value;
            var positionMid = start.Position + (end.Position - start.Position) / 2;
            var mid = new Coin(positionMid, valueMid);

            // Continue searching a different half to find sum position with binary search on either right or left side
            if (sum > mid.Position)
            {
                // Search right side
                start = mid;
                continue;
            }

            // Search left side
            end = mid;
        }
    }

    /// <summary>
    ///     Data structure to store value and position of coin.
    /// </summary>
    private class Coin
    {
        public Coin(long position, long value)
        {
            Position = position;
            Value = value;
        }

        public long Position { get; }
        public long Value { get; }
    }
}