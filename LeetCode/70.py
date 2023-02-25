class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n_stair):
            if n_stair < 0:
                return 0
            if n_stair == 0:
                return 1
            if n_stair in memo:
                return memo[n_stair]
            
            memo[n_stair] = dfs(n_stair-1) + dfs(n_stair-2)
            return memo[n_stair]
        return dfs(n)