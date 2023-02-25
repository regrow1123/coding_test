class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        st, current, ans = [], 0, 0
        while current < len(height):
            while st and height[current] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                dist = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += dist * bounded_height
            st.append(current)
            current += 1
        return ans