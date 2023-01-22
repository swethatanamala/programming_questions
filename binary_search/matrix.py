class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        n, m = len(A), len(A[0])
        left, right = 0, (n * m - 1)
        while left <= right:
            mid = (left + right) // 2
            i, j = mid // m, mid % m
            if A[i][j] == B:
                return 1
            elif A[i][j] < B:
                left = mid + 1
            else:
                right = mid - 1
        return 0
    
A = [ 
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]

    ]
B = 51
sol = Solution()
print(sol.searchMatrix(A, B))