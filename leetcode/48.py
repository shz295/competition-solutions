"""
Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""
class Solution:
    def rotate(self, matrix) -> None:
        # Transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]

# Test cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
        [[1]]
    ]
    for t in test_cases:
        sol.rotate(t)
        print(t)