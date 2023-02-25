class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for num in nums:
            out.append(p)
            p *= num
        
        p = 1
        for i in range(len(nums)-1, -1 ,-1):
            out[i] *= p
            p *= nums[i]
    
        return out