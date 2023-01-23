class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def lower_num(self, A, B):
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) // 2
            if A[mid] < B:
                left = mid + 1
            else:
                right = mid
        return left
    
    def higher_num(self, A, B):
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) // 2
            if A[mid] <= B:
                left = mid + 1
            else:
                right = mid
        return left
    
    def searchRange(self, A, B):
        lower_num = self.lower_num(A, B)
        higher_num = self.higher_num(A, B)
        lower_num = lower_num if (lower_num < len(A)) and (lower_num >= 0) else -1
        #lower_num = -1 if (lower_num == 0) and (A[0] != B) else lower_num
        higher_num = higher_num - 1 if (higher_num <= len(A)) and (higher_num > 0) else -1
        if higher_num < lower_num :
            return [-1, -1]
        return [lower_num, higher_num]

sol = Solution()
A = [5, 17, 100, 111]
B = 3
print(sol.searchRange(A, B))