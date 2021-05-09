class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_len = 0
        used = {}
        start = 0
        for i, ch in enumerate(s):
            if ch in used and used[ch] >= start:
                start = used[ch]+1
            else:
                max_len = max(max_len, i - start + 1)
            used[ch] = i
        return max_len