"""
Minimum Cost to Cut a Stick
Given a wooden stick of length n units. The stick is labelled from 0 to n.:

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.
"""
class Solution:
    # Recursive DP solution with O(n^3) time and O(n^2) space
    def minCost(self, n, cuts) -> int:
        cuts.extend([0, n])
        cuts.sort()
        dp = [[0] * len(cuts) for _ in cuts]

        for l in reversed(range(len(cuts))):
            for r in range(l+2, len(cuts)):
                dp[l][r] = cuts[r] - cuts[l] + min(dp[l][k] + dp[k][r] for k in range(l+1, r))
        
        return dp[0][-1]
    
# Test cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (7, [1,3,4,5]),
        (9, [5,6,1,4,2])
    ]
    for t in test_cases:
        print(sol.minCost(t[0], t[1]))