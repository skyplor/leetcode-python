class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        '''
        Hint:
        - Without loss of generality, there is a triangle that uses adjacent vertices A[0] and A[N-1] (where N = A.length).
        - Depending on your choice K of it, this breaks down the triangulation into two subproblems A[1:K] and A[K+1:N-1].
        
        This means that we can try recurrence and treat K as 1 or 2 since we can maximum have 3 vertices
        
        E.g
        For A = [3, 7, 4, 5] (indices 0, 1, 2, 3):
            We know one triangle must use the edge A[0]-A[3] (vertices 3 and 5).
            Choice 1: K = 1

            Triangle: A[0], A[1], A[3] = 3 * 7 * 5 = 105
            Left subproblem: A[0:1] = [3, 7] - only 2 vertices, no triangulation needed
            Right subproblem: A[1:3] = [7, 4, 5] - this needs triangulation!

            Choice 2: K = 2

            Triangle: A[0], A[2], A[3] = 3 * 4 * 5 = 60
            Left subproblem: A[0:2] = [3, 7, 4] - needs triangulation!
            Right subproblem: A[2:3] = [4, 5] - only 2 vertices, no triangulation needed
            
        Polygon: [3, 7, 4, 5]
         
                 7(1)----4(2)
                /          \
               /            \
             3(0)----------5(3)

            Option K=1: Use triangle (0,1,3)
            Option K=2: Use triangle (0,2,3)
        '''
        n = len(values)
        # dp[i][j] = minimum score to triangulate polygon from vertex i to j
        dp = [[0] * n for _ in range(n)]
        
        # length is the number of vertices in the subproblem
        for length in range(3, n + 1):  # Need at least 3 vertices for a triangle
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                # Try all possible third vertices k for the triangle (i, k, j)
                for k in range(i + 1, j):
                    # Score of triangle (i, k, j) + scores of two subproblems
                    score = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    dp[i][j] = min(dp[i][j], score)
        
        return dp[0][n - 1]


sol = Solution()
print(f'output: {sol.minScoreTriangulation([1, 2, 3])}, expected: 6')
print(f'output: {sol.minScoreTriangulation([3, 7, 4, 5])}, expected: 144')
print(f'output: {sol.minScoreTriangulation([1, 3, 1, 4, 1, 5])}, expected: 13')
