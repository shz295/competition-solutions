"""
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
class Solution:
    # Sliding window solution with O(n) time and O(1) space
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minsize = len(nums)+1
        i = 0
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                minsize = min(minsize, j - i + 1)
                target += nums[i]
                i += 1
        if minsize > len(nums): return 0
        return minsize


# Test cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (7, [2,3,1,2,4,3]),
        (4, [1,4,4]),
        (11, [1,1,1,1,1,1,1,1])
    ]
    for t in test_cases:
        print(sol.minSubArrayLen(t[0], t[1]))