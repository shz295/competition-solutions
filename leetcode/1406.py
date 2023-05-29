"""
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.
"""

class Solution:
    # DP solution with O(n) time and O(n) space
    def stoneGameIII(self, stoneValue) -> str:
        dp = [0] * len(stoneValue)
        if len(dp) >= 1: dp[-1] = stoneValue[-1]
        if len(dp) >= 2: dp[-2] = max(stoneValue[-2] + stoneValue[-1], stoneValue[-2] - dp[-1])
        if len(dp) >= 3: dp[-3] = max(stoneValue[-3] - dp[-2], stoneValue[-3] + stoneValue[-2] - dp[-1], stoneValue[-3] + stoneValue[-2] + stoneValue[-1])

        for i in range(len(stoneValue)-4, -1, -1):
            dp[i] = max([sum(stoneValue[i: i + k]) - dp[i + k] for k in range(1, 4)])
        
        if dp[0]>0: return "Alice"
        if dp[0]==0: return "Tie"
        return "Bob"

    # DP solution with O(n) time and O(1) space
    def stoneGameIII_constant(self, stoneValue):
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        if dp[0]>0: return "Alice"
        if dp[0]==0: return "Tie"
        return "Bob"

# check test cases
if __name__ == '__main__':
    sol = Solution()
    print(sol.stoneGameIII([1,2,3,7]))
    print(sol.stoneGameIII([1,2,3,-9]))
    print(sol.stoneGameIII([1,2,3,6]))