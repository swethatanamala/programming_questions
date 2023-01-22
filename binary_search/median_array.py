class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        result = []
        m, n = len(A), len(B)
        total_length = m + n
        i, j = 0, 0
        while (i < m) and(j < n):
            if A[i] < A[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(A[j])
                j += 1
        if i < m:
            result += A[i:]
        if j < n:
            result += A[j:]
        if total_length % 2 == 0:
            return (result[total_length // 2] + result[total_length // 2 + 1]) // 2
        else:
            return result[total_length // 2]

