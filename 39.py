class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        def dfs():
            if sum(path) == target:
                answer = sorted(path)
                if not answer in result:
                    result.append(answer)
            elif sum(path) > target:
                return
            
            for num in candidates:
                path.append(num)
                dfs()
                path.pop()
        
        result = []
        dfs()
        return result