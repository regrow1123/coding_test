class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        refined = []
        for ch in s:
            if ch.isalnum():
                refined.append(ch.lower())
        
        return refined == refined[::-1]