class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        path = []
        def dfs(nums):
            if len(path) == k:
                result.append(path[:])
                
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(nums[i+1:])
                path.pop()
                
        result = []
        dfs(sorted(list(range(1,n+1))))
        return result