class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort(reverse=True)
        n = len(A)
        hashmap = {A[0]: 0}
        for i in range(1, n):
            hashmap[A[i]] = hashmap[A[i - 1]] + i * (A[i - 1] - A[i])
        print(hashmap)
        i = 1
        while i < n:
            print(i, hashmap[A[i]], (hashmap[A[i]] > B) and (hashmap[A[i - 1]] < B))
            if hashmap[A[i]] == B:
                return A[i]
            elif (hashmap[A[i]] > B) and (hashmap[A[i - 1]] < B):
                max_ = 0
                for j in range(A[i] + 1, A[i - 1]):
                    result = 0
                    for k in range(i):
                        result += (A[k] - j)
                    if result >= B:
                        max_ = j
                    else:
                        return max_
                    print(j, result, B, result >= B, max_)
                return max_
            else:
                i += 1 

sol = Solution()
A = [ 62, 117, 149, 85, 144, 53, 61, 72, 83, 123, 114, 91, 61, 103 ]
B = 68
print(sol.solve(A, B))