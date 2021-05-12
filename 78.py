class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        def dfs(idx):
            result.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        
        result = []
        dfs(0)
        return result