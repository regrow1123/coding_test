class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        num, rev = x, 0
        while True:
            if x == 0:
                break
                
            rev = rev*10 + x%10
            x = x // 10
        
        return num == rev