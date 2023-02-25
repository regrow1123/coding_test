class Solution:
    def romanToInt(self, s: str) -> int:
        tab = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)-1):
            if tab[s[i]] < tab[s[i+1]]:
                ans -= tab[s[i]]
            else:
                ans += tab[s[i]]
        return ans + tab[s[-1]]