class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(perm, digits):
            if not digits:
                result.append(perm[:])
                
            for d in digits:
                perm.append(d)
                dfs(perm, [num for num in digits if d != num])
                perm.pop()
        
        result = []
        dfs([], nums)
        return result