class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for zipped in zip(*strs):
            if len(set(zipped)) > 1:
                return ans
            else:
                ans += zipped[0]
        return ans