class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, st = collections.Counter(s), []
        
        for char in s:
            counter[char] -= 1
            if char in st:
                continue
            
            while st and char < st[-1] and counter[st[-1]] > 0:
                st.pop()
            st.append(char)
        
        return ''.join(st)