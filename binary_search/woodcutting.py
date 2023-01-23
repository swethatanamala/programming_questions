class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def get_sum(self, A, val):
        n = len(A)
        sum = 0
        for i in range(n - 1, -1, -1):
            if A[i] > val:
                sum += (A[i] - val)
            else:
                break
        return sum

    def solve(self, A, B):
        A.sort()
        left, right = 1, A[-1]
        while left <= right:
            mid = (left + right)//2
            total_height = self.get_sum(A, mid)
            print(left, right, mid, total_height)
            if total_height == B:
                return mid
            elif total_height > B:
                left = mid + 1
            else:
                right = mid - 1
        return right
sol = Solution()
A = [ 117, 84, 50, 119, 74, 128 ]
B = 58
print(sol.solve(A, B))