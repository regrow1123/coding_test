class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str,digits)))
        num += 1
        
        ans = []
        while num:
            ans.append(num%10)
            num = num//10
        return ans[::-1]