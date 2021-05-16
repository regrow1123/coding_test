class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()

        for i in range(len(nums)):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
                
            window.append(i)
            
            if i-window[0] >= k:
                window.popleft()
                
            if i >= k-1:
                result.append(nums[window[0]])
        return result