class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums_map = {}
        for i, num in enumerate(nums):
            
            complement = target - num
            if complement in nums_map and nums_map[complement] != i:
                return [nums_map[complement], i]

            nums_map[num] = i
            